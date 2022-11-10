from flask import render_template
import dinkle.data as data
import dinkle.cost as cost
import dinkle.detail_image as detail_image
import dinkle.sta as sta
from urllib import request
counter=0
def index():
    return render_template('index.html')

def hp1():
    return render_template('hp1.html')

def monitor1():
    new=data.new_data
    status=data.status(new)
    regular=str(data.regular())[1:-1]
    yield_mac=data.yield_Machine(data.data)
    now_speed=data.get_Speed()
    now_frequency=data.get_Frequency()
    max_speed=data.max_speed()
    min_speed=data.min_speed()
    max_fre=data.max_Frequency()
    min_fre=data.min_Frequency()
    y1=data.yield_each('detail_1')
    y2=data.yield_each('detail_2')
    y3=data.yield_each('detail_3')
    y4=data.yield_each('detail_4')
    y5=data.yield_each('detail_5')
    y6=data.yield_each('detail_6')
    y7=data.yield_each('detail_7')
    y8=data.yield_each('detail_8')
    y9=data.yield_each('detail_9')
    y10=data.yield_each('detail_10')
    y11=data.yield_each('detail_11')
    y12=data.yield_each('detail_12')
    y13=data.yield_each('detail_13')
    return render_template('monitor1.html',sta=status,reg=regular,yie=yield_mac,nonyie=100-yield_mac,y1=y1,y2=y2,y3=y3,y4=y4,y5=y5,y6=y6,y7=y7,y8=y8,y9=y9,y10=y10,y11=y11,y12=y12,y13=y13,now_speed=now_speed,now_frequency=now_frequency,max_speed=max_speed,min_speed=min_speed,max_fre=max_fre,min_fre=min_fre)
def image():
    y1=data.yield_each('detail_1')
    y2=data.yield_each('detail_2')
    y3=data.yield_each('detail_3')
    y4=data.yield_each('detail_4')
    y5=data.yield_each('detail_5')
    y6=data.yield_each('detail_6')
    y7=data.yield_each('detail_7')
    y8=data.yield_each('detail_8')
    y9=data.yield_each('detail_9')
    y10=data.yield_each('detail_10')
    y11=data.yield_each('detail_11')
    y12=data.yield_each('detail_12')
    y13=data.yield_each('detail_13')
    max1=data.get_max('detail_1')
    max2=data.get_max('detail_2')
    max3=data.get_max('detail_3')
    max4=data.get_max('detail_4')
    max5=data.get_max('detail_5')
    max6=data.get_max('detail_6')
    max7=data.get_max('detail_7')
    max8=data.get_max('detail_8')
    max9=data.get_max('detail_9')
    max10=data.get_max('detail_10')
    max11=data.get_max('detail_11')
    max12=data.get_max('detail_12')
    max13=data.get_max('detail_13')
    min1=data.get_min('detail_1')
    min2=data.get_min('detail_2')
    min3=data.get_min('detail_3')
    min4=data.get_min('detail_4')
    min5=data.get_min('detail_5')
    min6=data.get_min('detail_6')
    min7=data.get_min('detail_7')
    min8=data.get_min('detail_8')
    min9=data.get_min('detail_9')
    min10=data.get_min('detail_10')
    min11=data.get_min('detail_11')
    min12=data.get_min('detail_12')
    min13=data.get_min('detail_13')
    color_lstmax={}
    color_lstmin={}
    for i in range(1,14):
        color_lstmax.update({('detail_'+str(i)):(data.get_colormax(('detail_'+str(i))))})
    for i in range(1,14):
        color_lstmin.update({('detail_'+str(i)):(data.get_colormin(('detail_'+str(i))))})
    return render_template('image.html',y1=y1,y2=y2,y3=y3,y4=y4,y5=y5,y6=y6,y7=y7,y8=y8,y9=y9,y10=y10,y11=y11,y12=y12,y13=y13,max1=max1,max2=max2,max3=max3,max4=max4,max5=max5,max6=max6,max7=max7,max8=max8,max9=max9,max10=max10,max11=max11,max12=max12,max13=max13,min1=min1,min2=min2,min3=min3,min4=min4,min5=min5,min6=min6,min7=min7,min8=min8,min9=min9,min10=min10,min11=min11,min12=min12,min13=min13,color_lstmax=color_lstmax,color_lstmin=color_lstmin)
def fix():
    err_lst=data.errorlst(data.data1)
    error_lst=data.error_list(err_lst)
    err1=str(error_lst[0]['error'])[1:-1]
    err2=str(error_lst[1]['error'])[1:-1]
    err3=str(error_lst[2]['error'])[1:-1]
    err4=str(error_lst[3]['error'])[1:-1]

    return render_template('fix.html',error_lst=error_lst,err1=err1,err2=err2,err3=err3,err4=err4)
def form():    
    if request.method=='POST':
        number=request.form['form_num']
        fixed=request.form['form_fix']
        reason=request.form['form_re']
        matter=request.form['form_port']
        marker=request.form['form_mark']
        global counter
        counter +=1
        
    return render_template('form.html')
def information():    
    err_lst=data.errorlst(data.data1)
    error_lst=data.error_list(err_lst)
    err1=str(error_lst[0]['error'])[1:-1]
    err2=str(error_lst[1]['error'])[1:-1]
    err3=str(error_lst[2]['error'])[1:-1]
    err4=str(error_lst[3]['error'])[1:-1]
    return render_template('information.html',error_lst=error_lst,err1=err1,err2=err2,err3=err3,err4=err4)
def statics():     
    maxup=sta.maxup
    maxdown=sta.maxdown
    maxall=sta.maxall
    minall=sta.minall
    averange=sta.averange
    midd=sta.midd
    outer=sta.outer
    return render_template('statics.html',maxup=maxup,maxdown=maxdown,maxall=maxall,minall=minall,averange=averange,midd=midd,outer=outer)


