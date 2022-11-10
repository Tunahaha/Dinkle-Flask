from tkinter import font
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dinkle.data as data
import numpy as np
from matplotlib.font_manager import FontProperties
import statistics
body = {'username': 'AirCenterQC', 'password': '@irQc12#'}
r = requests.post('http://192.168.21.33:11767/api/extract_predict_data?Machine=D-001&Product=0162B00100&Work_type=Stampers', data=body)
data = r.json()
#實際採400筆資料
datademo=data[::-1]
#預測先採用最新的一百筆資料
predata=datademo[300:400]

standard={
"detail_1up":"3.35",
"detail_1down":"3.25",
"detail_2up":"2.3",
"detail_2down":"2.2",
"detail_3up":"6.3",
"detail_3down":"6.14",
"detail_4up":"2.77",
"detail_4down":"2.63",
"detail_5up":"2.3",
"detail_5down":"2.1",
"detail_6up":"3.37",
"detail_6down":"3.23",
"detail_7up":"2.54",
"detail_7down":"2.34",
"detail_8up":"0.42",
"detail_8down":"0.38",
"detail_9up":"0.63",
"detail_9down":"0.53",
"detail_10up":"0.63",
"detail_10down":"0.53",
"detail_11up":"0.63",
"detail_11down":"0.53",
"detail_12up":"0.63",
"detail_12down":"0.53",
"detail_13up":"0.63",
"detail_13down":"0.53"
}
def status(new_d):
    new_data=new_d
    quality_status=True
    if (float(new_data["detail_1"])>float(standard["detail_1up"])) or (float(new_data["detail_2"])>float(standard["detail_2up"])) or (float(new_data["detail_3"])>float(standard["detail_3up"])) or (float(new_data["detail_4"])>float(standard["detail_4up"])) or (float(new_data["detail_5"])>float(standard["detail_5up"])) or (float(new_data["detail_6"])>float(standard["detail_6up"]))or (float(new_data["detail_7"])>float(standard["detail_7up"]))or (float(new_data["detail_8"])>float(standard["detail_8up"]))or (float(new_data["detail_9"])>float(standard["detail_9up"]))or (float(new_data["detail_10"])>float(standard["detail_10up"]))or (float(new_data["detail_11"])>float(standard["detail_11up"]))or (float(new_data["detail_12"])>float(standard["detail_12up"]))or (float(new_data["detail_13"])>float(standard["detail_13up"])):
        quality_status=False
    elif (float(new_data["detail_14"])<float(standard["detail_1down"])) or (float(new_data["detail_15"])<float(standard["detail_2down"])) or (float(new_data["detail_16"])<float(standard["detail_3down"])) or (float(new_data["detail_17"])<float(standard["detail_4down"])) or (float(new_data["detail_18"])<float(standard["detail_5down"])) or (float(new_data["detail_19"])<float(standard["detail_6down"]))or (float(new_data["detail_20"])<float(standard["detail_7down"]))or (float(new_data["detail_21"])<float(standard["detail_8down"]))or (float(new_data["detail_22"])<float(standard["detail_9down"])) or (float(new_data["detail_23"])<float(standard["detail_10down"])) or (float(new_data["detail_24"])<float(standard["detail_11down"])) or (float(new_data["detail_25"])<float(standard["detail_12down"])) or (float(new_data["detail_26"])<float(standard["detail_13down"])):
        quality_status=False
    return quality_status
def yield_Machine(data200,num):
    pass_rate=0
    for i in data200:
        if status(i):
            pass_rate+=1
    return (pass_rate/num)*100
now_sta=yield_Machine(predata,100)
his_sta=yield_Machine(datademo,400)

def get_Donut(correct,mistake):
    fig=plt.figure(31)
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    size_of_groups=[correct,mistake]
    plt.pie(size_of_groups,colors=['#09A63E','#FB8700'])
    plt.title("預測良品率",{"size":20,"color":"black"},x=-0.1)
    my_circle=plt.Circle( (0,0), 0.7, color='#FEE1E1')
    kw=dict(arrowprops=dict(arrowstyle='-'),va='center')
    a='預測良率:'+'\n'+str(size_of_groups[0])+'%'
    b='預測不良率:'+'\n'+str(size_of_groups[1])+'%'
    recipe=[a,b]
    wedges,texts=plt.pie(size_of_groups,startangle=40)
    for i,p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment,fontsize=15,**kw)
    plt.text(0., 0.,str(correct)+'%', horizontalalignment='center', verticalalignment='center',color='black',size=30)
    fig.patch.set_facecolor('#FEE1E1')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('dinkle/static/image/sta_donut.png')
#get_Donut_image=get_Donut(now_sta,100-now_sta)
def bar_chart(pre_data,real_data):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    labels = ['良品數比率', '功能不良品數比率']  
    q1 = [pre_data,100-pre_data] 
    q2 = [real_data,100-real_data] 
    results={
        '預測':q1,
        '實際':q2
    }
    label = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = ['green','red']
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(labels, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(label, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(float(c))+'%', ha='center', va='center',fontsize=10,color='white')
    ax.legend(ncol=len(labels), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='15')
    plt.yticks(fontsize=15)
    ax.set_facecolor('#EEEEEE')
    fig.set_facecolor('#EEEEEE')
    plt.savefig('dinkle/static/image/sta_abar.png')


#bar_chart(now_sta,his_sta)
#計算各detail超出上屆次數
def sta_countup(data1):
    count={'detail_1':0,'detail_2':0,'detail_3':0,'detail_4':0,'detail_5':0,'detail_6':0,'detail_7':0,'detail_8':0,'detail_9':0,'detail_10':0,'detail_11':0,'detail_12':0,'detail_13':0}
    for new_data in data1:
        if (float(new_data["detail_1"])>float(standard["detail_1up"])) or (float(new_data["detail_2"])>float(standard["detail_2up"])) or (float(new_data["detail_3"])>float(standard["detail_3up"])) or (float(new_data["detail_4"])>float(standard["detail_4up"])) or (float(new_data["detail_5"])>float(standard["detail_5up"])) or (float(new_data["detail_6"])>float(standard["detail_6up"]))or (float(new_data["detail_7"])>float(standard["detail_7up"]))or (float(new_data["detail_8"])>float(standard["detail_8up"]))or (float(new_data["detail_9"])>float(standard["detail_9up"]))or (float(new_data["detail_10"])>float(standard["detail_10up"]))or (float(new_data["detail_11"])>float(standard["detail_11up"]))or (float(new_data["detail_12"])>float(standard["detail_12up"]))or (float(new_data["detail_13"])>float(standard["detail_13up"])):
            for i in range(13):
                d='detail_'+str(i+1)
                u='detail_'+str(i+1)+'up'
                if (float(new_data[d])>float(standard[u])):
                    a=count[d]+1
                    count.update({d:a})
    return count
def sta_countdown(data1):
    count={'detail_1':0,'detail_2':0,'detail_3':0,'detail_4':0,'detail_5':0,'detail_6':0,'detail_7':0,'detail_8':0,'detail_9':0,'detail_10':0,'detail_11':0,'detail_12':0,'detail_13':0}
    for new_data in data1:
        if (float(new_data["detail_14"])<float(standard["detail_1down"])) or (float(new_data["detail_15"])<float(standard["detail_2down"])) or (float(new_data["detail_16"])<float(standard["detail_3down"])) or (float(new_data["detail_17"])<float(standard["detail_4down"])) or (float(new_data["detail_18"])<float(standard["detail_5down"])) or (float(new_data["detail_19"])<float(standard["detail_6down"]))or (float(new_data["detail_20"])<float(standard["detail_7down"]))or (float(new_data["detail_21"])<float(standard["detail_8down"]))or (float(new_data["detail_22"])<float(standard["detail_9down"])) or (float(new_data["detail_23"])<float(standard["detail_10down"])) or (float(new_data["detail_24"])<float(standard["detail_11down"])) or (float(new_data["detail_25"])<float(standard["detail_12down"])) or (float(new_data["detail_26"])<float(standard["detail_13down"])):
            for i in range(13):
                d='detail_'+str(i+14)
                w='detail_'+str(i+1)
                u='detail_'+str(i+1)+'down'
                if (float(new_data[d])<float(standard[u])):
                    a=count[w]+1
                    count.update({w:a})
    return count

def sta_bar(staup,stadown):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    fig=plt.figure(32)
    labels=[]
    for i in range(1,14):
        labels.append(i)
    up=[]
    for i in staup.values():
        up.append(i)
    down=[]
    for i in stadown.values():
        down.append(i)
    x = np.arange(len(labels))
    width = 0.3
    plt.bar(x, up, width, color='#3074B4', label='超過上界次數')
    plt.bar(x + width, down, width, color='#DB7B22', label='超過下界次數')
    plt.xticks(x + width / 2, labels)
    plt.ylabel('次數')
    plt.xlabel('detail')
    plt.legend(ncol=len(labels), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='10')
    plt.savefig('dinkle/static/image/sta_bar.png')
#sta_bar(sta_countup(datademo),sta_countdown(datademo))
def max_up(staup):
    max=0
    lst={'max':0,'detail':'-'}
    count=0
    for i in staup:
        count=count+1
        if staup[i]> max:
            max=staup[i]
            lst.update({'max':max,'detail':count})
    return lst
def max_all(staup,stadown):
    max=0
    count=0
    lst={'max':0,'detail':'-'}
    for i in staup:
        count=count+1
        if staup[i]+stadown[i]> max:
            max=staup[i]+stadown[i]
            lst.update({'max':max,'detail':count})
    return lst
def min_all(staup,stadown):
    min=0
    lst={'max':0,'detail':'1'}
    for i in staup:
        if staup[i]+stadown[i]< min:
            min=staup[i]+stadown[i]
            lst.update({'max':min,'detail':i})
    return lst
def ave_all(staup,stadown):
    up=staup.values()
    down=stadown.values()
    aver=round((sum(up)+sum(down))/13,2)
    lst={'aver':aver,'detail':'-'}
    return lst    
def mid_num(staup,stadown):
    lst=[]
    lis={}
    for i in staup:
        lst.append(staup[i]+stadown[i])
    lst=sorted(lst)
    num=len(lst)
    val=lst[round(num*0.5)]
    ind=np.where(np.array(lst)==val)[0][0]

    lis.update({'mid':val,'detail':str(ind+1)})
    return lis
def outter(staup,stadown):
    lst=[]
    lis={}
    for i in staup:
        lst.append(staup[i]+stadown[i])
    ave=statistics.mean(lst)
    std=np.std(lst)
    for i in range(len(lst)):
        if lst[i]>(ave+3*std):
            lis.update({'outter':lst[i],'detail':str(i+1)})
    if lis=={}:
        lis.update({'mid':'-','detail':'-'})
    return lis



maxup=max_up(sta_countup(datademo))
maxdown=max_up(sta_countdown(datademo))
maxall=max_all(sta_countup(datademo),sta_countdown(datademo))
minall=min_all(sta_countup(datademo),sta_countdown(datademo))
averange=ave_all(sta_countup(datademo),sta_countdown(datademo))
midd=mid_num(sta_countup(datademo),sta_countdown(datademo))
outer=outter(sta_countup(datademo),sta_countdown(datademo))



