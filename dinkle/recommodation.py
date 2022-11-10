from turtle import title
import requests
import matplotlib.pyplot as plt
import time
import csv
import numpy as np
from matplotlib import animation 
#摳api
body = {'username': 'AirCenterQC', 'password': '@irQc12#'}
r = requests.post('http://192.168.21.33:11767/api/extract_predict_data?Machine=D-001&Product=0162B00100&Work_type=Stampers', data=body)
#轉json
data = r.json()
#由小到大排序
data1=data[::-1]
standard={
"detail_1up":3.35,
"detail_1down":3.25,
"detail_2up":2.3,
"detail_2down":2.2,
"detail_3up":6.3,
"detail_3down":6.14,
"detail_4up":2.77,
"detail_4down":2.63,
"detail_5up":2.3,
"detail_5down":2.1,
"detail_6up":3.37,
"detail_6down":3.23,
"detail_7up":2.54,
"detail_7down":2.34,
"detail_8up":0.42,
"detail_8down":0.38,
"detail_9up":0.63,
"detail_9down":0.53,
"detail_10up":0.63,
"detail_10down":0.53,
"detail_11up":0.63,
"detail_11down":0.53,
"detail_12up":0.63,
"detail_12down":0.53,
"detail_13up":0.63,
"detail_13down":0.53
}
ck={
"detail_1p":6.6,
"detail_1m":0.1,
"detail_2p":4.5,
"detail_2m":0.1,
"detail_3p":12.44,
"detail_3m":0.16,
"detail_4p":5.4,
"detail_4m":0.14,
"detail_5p":4.4,
"detail_5m":0.2,
"detail_6p":6.6,
"detail_6m":0.14,
"detail_7p":4.88,
"detail_7m":0.2,
"detail_8p":0.8,
"detail_8m":0.04,
"detail_9p":1.16,
"detail_9m":0.1,
"detail_10p":1.16,
"detail_10m":0.1,
"detail_11p":1.16,
"detail_11m":0.1,
"detail_12p":1.16,
"detail_12m":0.1,
"detail_13p":1.16,
"detail_13m":0.1
}
file=open('dinkle/static/csv/test.csv')
rows = csv.reader(file)
datalist=list(rows)
untitle=datalist[1:]
clearndata=[]#test data的43,093筆資料去掉不合格變成41,758筆資料
for i in range(len(untitle)):
    if untitle[i][-1]=='1':
        clearndata.append(untitle[i])



def cleaninput(inp):
    a='detail_'
    err={'max':[],'min':[]}
    for i in range(13):
        if float(inp[a+str(i+1)])>standard[a+str(i+1)+'up'] or float(inp[a+str(i+1)])<standard[a+str(i+1)+'down']:
            err["max"].append(i+1)
        elif   float(inp[a+str(i+14)])>standard[a+str(i+1)+'up'] or float(inp[a+str(i+14)])<standard[a+str(i+1)+'down']:
            err["min"].append(i+1)
    return err

#ck表單
def ckformula(detail,a,b):
    return abs(float(detail)-(float(a)/2))/(float(b)/2)
#算一行的CKMAX
def getck(rowdata):
    ckdata=rowdata
    a='detail_'
    for i in range(13):
        num=str(a+str(i+1))
        ckdata.append(round(ckformula(ckdata[301+i],ck[num+'p'],ck[num+'m']),5))
    for i in range(13):
        num=str(a+str(i+1))
        ckdata.append(round(ckformula(ckdata[314+i],ck[num+'p'],ck[num+'m']),5))
    return ckdata
#全部CK
def calck(clearndata):
    newd=[]
    for i in range(len(clearndata)):
        newd.append(getck(clearndata[i]))
    return newd

cklist=calck(clearndata)
#相關係數公式
def r(x, y):
    xm = np.mean(x)
    ym = np.mean(y)
    numerator = np.sum(((x - xm) * (y - ym)))
    denominator = np.sqrt(np.sum((x - xm) ** 2)) * np.sqrt(np.sum((y - ym) ** 2))
    return numerator / denominator  

def ckfilter(inp,inputlist):
    finallist=cklist
    if (len(inp['max'])==0) and (len(inp['min'])==0):#若沒異常取所有的平均
        for i in range(len(finallist)):
            s=0
            for j in range(26):
               s=s+finallist[i][329+j]
            finallist[i].append(round((s/26),5))
        finallist.sort(key=lambda s:s[-1])
        list30=finallist[0:30]
        #先把inputlist的轉速、狀態、沖壓次數全部合成一筆list
        inputtra=[]
        for i in range(len(inputlist)):
            inputtra.append(inputlist[i]['Speed'])
            inputtra.append(inputlist[i]['Status'])
            inputtra.append(inputlist[i]['frequency'])
        #再去算相關係數
        corrlist=[]
        for i in range(len(list30)):
            b_list=list30[i][1:271]
            a_normal= np.array(inputtra)
            b_normal=np.array(b_list)
            b_normal=b_normal.astype(float)
            corr = round(r(a_normal,b_normal), 4)
            list30[i].append(corr)
            corrlist.append(corr)
        close=min(corrlist, key=lambda x: abs(x-1))
        for i in range(len(list30)):
            if list30[i][-1]==close:
                return list30[i][271:301]
                
    else:#超過兩筆異常 取其平均
        s=0
        c=0
        for j in range(len(finallist)):
            for i in range(len(inp['max'])):
                s=s+finallist[j][329+inp['max'][i]]
                c=c+1
            for i in range(len(inp['min'])):
                s=s+finallist[j][342+inp['min'][i]]
                c=c+1
            finallist[j].append(s/c)
        finallist.sort(key=lambda s:s[-1])
        list30=finallist[0:30]
        #先把inputlist的轉速、狀態、沖壓次數全部合成一筆list
        inputtra=[]
        for i in range(len(inputlist)):
            inputtra.append(inputlist[i]['Speed'])
            inputtra.append(inputlist[i]['Status'])
            inputtra.append(inputlist[i]['frequency'])
        #再去算相關係數
        corrlist=[]
        for i in range(len(list30)):
            b_list=list30[i][1:271]
            a_normal= np.array(inputtra)
            b_normal=np.array(b_list)
            b_normal=b_normal.astype(float)
            corr = round(r(a_normal,b_normal), 4)
            list30[i].append(corr)
            corrlist.append(corr)
        close=min(corrlist, key=lambda x: abs(x-1))
        for i in range(len(list30)):
            if list30[i][-1]==close:
                return list30[i][271:301]
'''
input90=data[0:90]
nowdata=input90[-1]
test=cleaninput(nowdata)                
cktest=ckfilter(test,input90)
print(getspeed(cktest))
'''

def getspeed(ckdata):
    lis=ckdata[::3]
    float_lst = [float(item) for item in lis]
    return float_lst
def getStatus(ckdata):
    lis=ckdata[1::3]
    return lis
def getfrequency(ckdata):
    lis=ckdata[2::3]
    float_lst = [float(item) for item in lis]
    return float_lst

def spi(ma):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    fig=plt.figure(ma)
    ax1=plt.gca()
    ax1.set_title('最適機台參數',fontsize=20)
    ax1.set_xlabel('時間')
    ax1.set_ylabel('速度')
    x=[i for i in range(100)]
    y = [data1[i]['Speed'] for i in range(90)]
    input90=data[0:90]
    nowdata=input90[-1]
    test=cleaninput(nowdata)  
    cktest=ckfilter(test,input90)

    y=y+getspeed(cktest)
    plt.axvline(x=90, ymin=0, ymax=1,linestyle='--')
    art=[]
    for frame in range(100):
        y = [data1[i+frame]['Speed'] for i in range(90)]
        input90=data[frame:90+frame]
        nowdata=input90[-1]
        test=cleaninput(nowdata)  
        cktest=ckfilter(test,input90)
        y=y+getspeed(cktest)
        b=plt.plot(x,y,'black',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    url='dinkle/static/image/'+'reSpeed.png'
    ani.save(url,writer='pillow')
spi(50)
def fri(ma):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    fig=plt.figure(ma)
    ax1=plt.gca()
    ax1.set_title('最適機台參數',fontsize=20)
    ax1.set_xlabel('每秒沖壓次數')
    ax1.set_ylabel('速度')
    x=[i for i in range(100)]
    y = [data1[i]['frequency'] for i in range(90)]
    input90=data[0:90]
    nowdata=input90[-1]
    test=cleaninput(nowdata)  
    cktest=ckfilter(test,input90)
    y=y+getfrequency(cktest)
    plt.axvline(x=90, ymin=0, ymax=1,linestyle='--')
    art=[]
    for frame in range(100):
        y = [data1[i+frame]['frequency'] for i in range(90)]
        input90=data[frame:90+frame]
        nowdata=input90[-1]
        test=cleaninput(nowdata)  
        cktest=ckfilter(test,input90)
        y=y+getfrequency(cktest)
        b=plt.plot(x,y,'black',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    url='dinkle/static/image/'+'refre.png'
    ani.save(url,writer='pillow')
#fri(55)
'''
def im():
    fig = plt.figure(50)
    ax = fig.add_subplot(1, 1, 1)
    x = [i for i in range(100)]
    y = [data1[i]['Speed'] for i in range(90)]
    input90=data[0:90]
    nowdata=input90[-1]
    test=cleaninput(nowdata)  
    cktest=ckfilter(test,input90)
    y=y+getspeed(cktest)
    line, = ax.plot(x, y, label='actual',color="black",lw=3 )
    ax.legend(loc="lower left")
    # 清空当前帧
    def init():
        return line

    # 更新新一帧的数据
    def update(frame):
        y = [data1[i+frame+1]['Speed'] for i in range(90)]
        input90=data[frame+1:90+frame+1]
        nowdata=input90[-1]
        test=cleaninput(nowdata)  
        cktest=ckfilter(test,input90)
        y=y+getspeed(cktest)
        line.set_ydata(y)
        return line

    # 调用 FuncAnimation
    ani = animation.FuncAnimation(fig
                    ,update
                    ,init_func=init
                    ,frames=60
                    ,interval=1000
                    ,blit=True
                    )


    ani.save("dinkle/reSpeed1.png")
im()
'''
'''
def getallspeed(da):
    speedlist=[]
    for i in range(len(da)-90):
        input90=da[i:90+i]
        nowdata=input90[-1]
        test=cleaninput(nowdata) 
        cktest=ckfilter(test,input90)
        a=[int(getspeed(cktest)[s]) for s in range(len(getspeed(cktest)))]

        speedlist.append(a)
    return speedlist

def splitspeed(speedlist,nu):
    speedl=speedlist[nu]
    for i in range(1,10):
        speedl=speedl+speedlist[10*i+nu]
    return speedl

splist=getallspeed(data1)
split1=splitspeed(splist,0)
split2=splitspeed(splist,1)
split3=splitspeed(splist,2)
split4=splitspeed(splist,3)
split5=splitspeed(splist,4)
split6=splitspeed(splist,5)
split7=splitspeed(splist,6)
split8=splitspeed(splist,7)
split9=splitspeed(splist,8)
split10=splitspeed(splist,9)

def im():
    fig = plt.figure(50)
    ax = fig.add_subplot(1, 1, 1)
    x = [i for i in range(10)]
    y = [data1[90+i]['Speed'] for i in range(10)]
    z1=split1[0:10]
    z2=split2[0:10]
    z3=split3[0:10]
    z4=split4[0:10]
    z5=split5[0:10]
    z6=split6[0:10]
    z7=split7[0:10]
    z8=split8[0:10]
    z9=split9[0:10]
    z10=split10[0:10]
    line, = ax.plot(x, y, label='actual',color="black",lw=3 )
    line1, = ax.plot(x, z1, color="blue", linestyle='--',lw=1)
    line2, = ax.plot(x, z2, color="yellow", linestyle='--',lw=1)
    line3, = ax.plot(x, z3, color="green", linestyle='--',lw=1)
    line4, = ax.plot(x, z4, color="red", linestyle='--',lw=1)
    line5, = ax.plot(x, z5, color="brown", linestyle='--',lw=1)
    line6, = ax.plot(x, z6, color="gray", linestyle='--',lw=1)
    line7, = ax.plot(x, z7, color="pink", linestyle='--',lw=1)
    line8, = ax.plot(x, z8, color="purple", linestyle='--',lw=1)
    line9, = ax.plot(x, z9, color="silver", linestyle='--',lw=1)
    line10, = ax.plot(x, z10, color="wheat", linestyle='--',lw=1)
    ax.legend(loc="lower left")
    # 清空当前帧
    def init():
        return line,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10

    # 更新新一帧的数据
    def update(frame):
        x = [i for i in range(10)]
        y = [data1[i+91+frame]['Speed'] for i in range(10)]
        z1 = split1[1+frame:11+frame]
        z2 = split2[1+frame:11+frame]
        z3 = split3[1+frame:11+frame]
        z4 = split4[1+frame:11+frame]
        z5 = split5[1+frame:11+frame]
        z6 = split6[1+frame:11+frame]
        z7 = split7[1+frame:11+frame]
        z8 = split8[1+frame:11+frame]
        z9 = split9[1+frame:11+frame]
        z10 = split10[1+frame:11+frame]
        line.set_data(x, y)
        line1.set_data(x, z1)
        line2.set_data(x, z2)
        line3.set_data(x, z3)
        line4.set_data(x, z4)
        line5.set_data(x, z5)
        line6.set_data(x, z6)
        line7.set_data(x, z7)
        line8.set_data(x, z8)
        line9.set_data(x, z9)
        line10.set_data(x, z10)
        return line,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10

    # 调用 FuncAnimation
    ani = animation.FuncAnimation(fig
                    ,update
                    ,init_func=init
                    ,frames=100
                    ,interval=15000
                    ,blit=True
                    )


    ani.save("dinkle/static/image/reSpeed.png",  writer="imagemagick")
#im()


def getallfre(da):
    frelist=[]
    for i in range(len(da)-90):
        input90=da[i:90+i]
        nowdata=input90[-1]
        test=cleaninput(nowdata) 
        cktest=ckfilter(test,input90)
        a=[float(getfrequency(cktest)[s]) for s in range(len(getfrequency(cktest)))]
        frelist.append(a)
    return frelist

def splitfre(frelist,nu):
    frel=frelist[nu]
    for i in range(1,10):
        frel=frel+frelist[10*i+nu]
    return frel
    

frlist=getallfre(data1)
split1=splitfre(frlist,0)
split2=splitfre(frlist,1)
split3=splitfre(frlist,2)
split4=splitfre(frlist,3)
split5=splitfre(frlist,4)
split6=splitfre(frlist,5)
split7=splitfre(frlist,6)
split8=splitfre(frlist,7)
split9=splitfre(frlist,8)
split10=splitfre(frlist,9)

def img():
    fig = plt.figure(51)
    ax = fig.add_subplot(1, 1, 1)
    x = [i for i in range(10)]
    y = [data1[90+i]['frequency'] for i in range(10)]
    z1=split1[0:10]
    z2=split2[0:10]
    z3=split3[0:10]
    z4=split4[0:10]
    z5=split5[0:10]
    z6=split6[0:10]
    z7=split7[0:10]
    z8=split8[0:10]
    z9=split9[0:10]
    z10=split10[0:10]
    line, = ax.plot(x, y, label='actual',color="black",lw=3 )
    line1, = ax.plot(x, z1, color="blue", linestyle='--',lw=1)
    line2, = ax.plot(x, z2, color="yellow", linestyle='--',lw=1)
    line3, = ax.plot(x, z3, color="green", linestyle='--',lw=1)
    line4, = ax.plot(x, z4, color="red", linestyle='--',lw=1)
    line5, = ax.plot(x, z5, color="brown", linestyle='--',lw=1)
    line6, = ax.plot(x, z6, color="gray", linestyle='--',lw=1)
    line7, = ax.plot(x, z7, color="pink", linestyle='--',lw=1)
    line8, = ax.plot(x, z8, color="purple", linestyle='--',lw=1)
    line9, = ax.plot(x, z9, color="silver", linestyle='--',lw=1)
    line10, = ax.plot(x, z10, color="wheat", linestyle='--',lw=1)
    ax.legend(loc="lower left")
    # 清空当前帧
    def init():
        return line,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10

    # 更新新一帧的数据
    def update(frame):
        x = [i for i in range(10)]
        y = [data1[i+91+frame]['frequency'] for i in range(10)]
        z1 = split1[1+frame:11+frame]
        z2 = split2[1+frame:11+frame]
        z3 = split3[1+frame:11+frame]
        z4 = split4[1+frame:11+frame]
        z5 = split5[1+frame:11+frame]
        z6 = split6[1+frame:11+frame]
        z7 = split7[1+frame:11+frame]
        z8 = split8[1+frame:11+frame]
        z9 = split9[1+frame:11+frame]
        z10 = split10[1+frame:11+frame]
        line.set_data(x, y)
        line1.set_data(x, z1)
        line2.set_data(x, z2)
        line3.set_data(x, z3)
        line4.set_data(x, z4)
        line5.set_data(x, z5)
        line6.set_data(x, z6)
        line7.set_data(x, z7)
        line8.set_data(x, z8)
        line9.set_data(x, z9)
        line10.set_data(x, z10)
        return line,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10

    # 调用 FuncAnimation
    ani = animation.FuncAnimation(fig
                    ,update
                    ,init_func=init
                    ,frames=100
                    ,interval=15000
                    ,blit=True
                    )


    ani.save("dinkle/static/image/refre.png",  writer="imagemagick")
img()
'''