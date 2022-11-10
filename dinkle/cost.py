import matplotlib.pyplot as plt
import dinkle.data as data
import dinkle.detail_image as detail_image
import matplotlib.animation as animation
from flask import url_for
#用來計算成本的code
dataall=data.data1
data20=data.data1[0:20]
success_cost=95000#設成功的成本
fail_cost=225000#失敗的成本
#計算所有資料的合格率
def yield_Machine(data200):
    pass_rate=0
    for i in data200:
        if data.status(i):
            pass_rate+=1
    return (pass_rate/len(data200))*100

def success(dataa,datab):
    ndata=dataa
    usedata=datab
    successratio=[yield_Machine(usedata)]
    for i in ndata[20:]:
        usedata.append(i)
        usedata.pop(0)
        successratio.append(yield_Machine(usedata))
    return successratio
success_list=success(dataall,data20)
#計算成本
def machine_cost(successlist,su_cost,fa_cost):
    cost_list=[]
    for i in successlist:
        scost=i*su_cost
        fcost=(100-i)*fa_cost
        total_cost=scost+fcost
        cost_list.append(total_cost)
    return cost_list
totalcost=machine_cost(success_list,success_cost,fail_cost)
get_Date=detail_image.getdemo_Date(dataall)

def acu(adata):
    aculist=[]
    for i in adata:
        if data.status(i):
            aculist.append(0)
        else:
            aculist.append(1)
    return aculist
dalist=acu(dataall)
def acucost(dlist,fcost):
    tocost=0
    tocostlist=[]
    for i in dlist:
        if i==1:
            tocost=tocost+(fcost)
        tocostlist.append(tocost)
    return tocostlist

tcl=acucost(dalist,fail_cost)



def costani(ma):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    fig=plt.figure(ma)
    ax1=plt.gca()
    ax1.set_title('預測機台成本')
    ax1.set_xlabel('良率')
    ax1.set_ylabel('機台成本')
    ax1.axes.xaxis.set_visible(False)
    x=get_Date[0:20]
    y=totalcost[0:20]
    art=[]
    for i in range(80):
        y.pop(0)
        y.append(totalcost[i+20])
        b=plt.plot(x,y,'black',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    url='dinkle/static/image/'+'cost.png'
    ani.save(url,writer='pillow')
def acuani(ma):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    fig=plt.figure(ma)
    ax1=plt.gca()
    ax1.set_title('累積不良品成本')
    ax1.set_xlabel('良率')
    ax1.set_ylabel('累積成本')
    ax1.axes.xaxis.set_visible(False)
    x=get_Date[0:20]
    y=tcl[0:20]
    art=[]
    for i in range(80):
        y.pop(0)
        y.append(tcl[i+20])
        b=plt.plot(x,y,'black',label='data')
        art.append(b)
    ani = animation.ArtistAnimation(fig, art, interval=500, blit=False,repeat=False)
    url='dinkle/static/image/'+'totalcost.png'
    ani.save(url,writer='pillow')
#ta=acuani(34)