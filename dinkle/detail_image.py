import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dinkle.data as data

body = {'username': 'AirCenterQC', 'password': '@irQc12#'}
r = requests.post('http://192.168.21.33:11767/api/extract_predict_data?Machine=D-001&Product=0162B00100&Work_type=Stampers', data=body)
data = r.json()
data1=data[::-1]
def get_Detail(Detail):
    detaillist=[]
    for i in data:
        detaillist.append(float(i[Detail]))
    return detaillist[::-1]
def get_Date():
    datelist=[]
    for i in data:
        datelist.append((i['time']))
    return datelist[::-1]
#以下為Demo
def demo_data(data100):
    data100list=[]
    for i in range(50):
        data100list.append(data100[i])
    return data100list
catch=data1
del catch[0:50]
def catch_New(catch_data):
    a=catch_data[0]
    catch_data.pop(0)
    return a
new_data=catch_New(catch)
d_data=demo_data(data1)
def getdemo_Detail(demodata,Detail):
    detaillist=[]
    for i in demodata:
        detaillist.append(float(i[Detail]))
    return detaillist[::-1]
def getdemo_Date(demodata):
    datelist=[]
    for i in demodata:
        datelist.append((i['time']))
    return datelist[::-1]
get_Date1=getdemo_Date(d_data)
'''
get_Detail1=getdemo_Detail(d_data,'detail_1')
get_Detail2=getdemo_Detail(d_data,'detail_2')
get_Detail3=getdemo_Detail(d_data,'detail_3')
get_Detail4=getdemo_Detail(d_data,'detail_4')
get_Detail5=getdemo_Detail(d_data,'detail_5')
get_Detail6=getdemo_Detail(d_data,'detail_6')
get_Detail7=getdemo_Detail(d_data,'detail_7')
get_Detail8=getdemo_Detail(d_data,'detail_8')
get_Detail9=getdemo_Detail(d_data,'detail_9')
get_Detail10=getdemo_Detail(d_data,'detail_10')
get_Detail11=getdemo_Detail(d_data,'detail_11')
get_Detail12=getdemo_Detail(d_data,'detail_12')
get_Detail13=getdemo_Detail(d_data,'detail_13')
'''
'''
get_Date1=get_Date()
get_Detail1=get_Detail('detail_1')
get_Detail2=get_Detail('detail_2')
get_Detail3=get_Detail('detail_3')
get_Detail4=get_Detail('detail_4')
get_Detail5=get_Detail('detail_5')
get_Detail6=get_Detail('detail_6')
get_Detail7=get_Detail('detail_7')
get_Detail8=get_Detail('detail_8')
get_Detail9=get_Detail('detail_9')
get_Detail10=get_Detail('detail_10')
get_Detail11=get_Detail('detail_11')
get_Detail12=get_Detail('detail_12')
get_Detail13=get_Detail('detail_13')
'''
def cat_Data(Detail):
    catlst=[]
    for i in data:
        dic={(i['time']):(i[Detail])}
        catlst.append(dic)
    return catlst
get_cat1=cat_Data('detail_1')
'''
def get_image1(up,down):
    plt.figure(1)
    plt.plot(get_Date1,get_Detail1,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d1.png')
def get_image2(up,down):
    plt.figure(2)
    plt.plot(get_Date1,get_Detail2,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d2.png')
def get_image3(up,down):
    plt.figure(3)
    plt.plot(get_Date1,get_Detail3,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d3.png')
def get_image4(up,down):
    plt.figure(4)
    plt.plot(get_Date1,get_Detail4,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d4.png')  
def get_image5(up,down):
    plt.figure(5)
    plt.plot(get_Date1,get_Detail5,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d5.png')  
def get_image6(up,down):
    plt.figure(6)
    plt.plot(get_Date1,get_Detail6,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d6.png')  
def get_image7(up,down):
    plt.figure(7)
    plt.plot(get_Date1,get_Detail7,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d7.png') 
def get_image8(up,down):
    plt.figure(8)
    plt.plot(get_Date1,get_Detail8,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d8.png')   
def get_image9(up,down):
    plt.figure(9)
    plt.plot(get_Date1,get_Detail9,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d9.png')   
def get_image10(up,down):
    plt.figure(10)
    plt.plot(get_Date1,get_Detail10,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d10.png')   
def get_image11(up,down):
    plt.figure(11)
    plt.plot(get_Date1,get_Detail11,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d11.png')  
def get_image12(up,down):
    plt.figure(12)
    plt.plot(get_Date1,get_Detail12,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d12.png')   
def get_image13(up,down):
    plt.figure(13)
    plt.plot(get_Date1,get_Detail13,label='data')
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    plt.legend()
    plt.savefig('dinkle/static/image/d13.png')
d1=get_image1(3.35,3.25)
d2=get_image2(2.3,2.2)
d3=get_image3(6.3,6.14)
d4=get_image4(2.77,2.63)
d5=get_image5(2.3,2.1)
d6=get_image6(3.37,3.23)
d7=get_image7(2.54,2.34)
d8=get_image8(0.42,0.38)
d9=get_image9(0.63,0.53)
d10=get_image10(0.63,0.53)
d11=get_image11(0.63,0.53)
d12=get_image12(0.63,0.53)
d13=get_image13(0.63,0.53)
'''
def get_Fre(ues_data):
    frelist=[]
    for i in ues_data:
        frelist.append(float(i['frequency']))
    return frelist[::-1]
fre100=get_Fre(data1[0:50])
def get_freimage(use_data):
    fig=plt.figure(15)
    ax1=plt.gca()
    ax1.axes.xaxis.set_visible(False)
    x=getdemo_Date(data1)[0:50]
    y=use_data
    art=[]
    for i in data1[50:100]:
        y.pop(0)
        y.append(i['frequency'])
        b=plt.plot(x,y,'#3074B4',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    ani.save('dinkle/static/image/fre.png',writer='pillow')
def get_Speed(ues_data):
    spelist=[]
    for i in ues_data:
        spelist.append(float(i['Speed']))
    return spelist[::-1]
speed100=get_Speed(data1[0:50])

def get_speimage(use_data):
    fig=plt.figure(16)
    ax1=plt.gca()
    ax1.axes.xaxis.set_visible(False)
    x=getdemo_Date(data1)[0:50]
    y=use_data
    art=[]
    for i in data1[50:100]:
        y.pop(0)
        y.append(i['Speed'])
        b=plt.plot(x,y,'#3074B4',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    ani.save('dinkle/static/image/speed.png',writer='pillow')

def ani(up,down,detail,ma):
    fig=plt.figure(ma)
    plt.axhline(up,color='red',label='up')
    plt.axhline(down,color='blue',label='down')
    ax1=plt.gca()
    ax1.set_title('Detail')
    ax1.set_xlabel('time')
    ax1.axes.xaxis.set_visible(False)
    x=get_Date1
    y=getdemo_Detail(d_data,detail)
    art=[]
    for i in data1[50:100]:
        y.pop(0)
        y.append(i[detail])
        b=plt.plot(x,y,'black',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    url='dinkle/static/image/'+detail+'.png'
    ani.save(url,writer='pillow')
'''
d1=ani(3.35,3.25,'detail_1',18)
d2=ani(2.3,2.2,'detail_2',19)
d3=ani(6.3,6.14,'detail_3',20)
d4=ani(2.77,2.63,'detail_4',21)
d5=ani(2.3,2.1,'detail_5',22)
d6=ani(3.37,3.23,'detail_6',23)
d7=ani(2.54,2.24,'detail_7',24)
d8=ani(0.42,0.38,'detail_8',25)
d9=ani(0.63,0.53,'detail_9',26)
d10=ani(0.63,0.53,'detail_10',27)
d11=ani(0.63,0.53,'detail_11',28)
d12=ani(0.63,0.53,'detail_12',29)
d13=ani(0.63,0.53,'detail_13',30)
'''
cost=60000