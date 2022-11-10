import requests
import matplotlib.pyplot as plt
import time
 
#摳api
body = {'username': 'AirCenterQC', 'password': '@irQc12#'}
r = requests.post('http://192.168.21.33:11767/api/extract_predict_data?Machine=D-001&Product=0162B00100&Work_type=Stampers', data=body)
#轉json
data = r.json()
#取得第一筆資料
new_data=data[0]
#由小到大排序
data1=data[::-1]
range_list=[
"3.25~3.35","2.2~2.3","6.14~6.3","2.63~2.77","2.1~2.3","3.23~3.37","2.34~2.54","0.38~0.42","0.53~0.63","0.53~0.63","0.53~0.63","0.53~0.63","0.53~0.63"]
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
#檢測某筆資料是否有異常
def status(new_d):
    new_data=new_d
    quality_status=True
    if (float(new_data["detail_1"])>float(standard["detail_1up"])) or (float(new_data["detail_2"])>float(standard["detail_2up"])) or (float(new_data["detail_3"])>float(standard["detail_3up"])) or (float(new_data["detail_4"])>float(standard["detail_4up"])) or (float(new_data["detail_5"])>float(standard["detail_5up"])) or (float(new_data["detail_6"])>float(standard["detail_6up"]))or (float(new_data["detail_7"])>float(standard["detail_7up"]))or (float(new_data["detail_8"])>float(standard["detail_8up"]))or (float(new_data["detail_9"])>float(standard["detail_9up"]))or (float(new_data["detail_10"])>float(standard["detail_10up"]))or (float(new_data["detail_11"])>float(standard["detail_11up"]))or (float(new_data["detail_12"])>float(standard["detail_12up"]))or (float(new_data["detail_13"])>float(standard["detail_13up"])):
        quality_status=False
    elif (float(new_data["detail_14"])<float(standard["detail_1down"])) or (float(new_data["detail_15"])<float(standard["detail_2down"])) or (float(new_data["detail_16"])<float(standard["detail_3down"])) or (float(new_data["detail_17"])<float(standard["detail_4down"])) or (float(new_data["detail_18"])<float(standard["detail_5down"])) or (float(new_data["detail_19"])<float(standard["detail_6down"]))or (float(new_data["detail_20"])<float(standard["detail_7down"]))or (float(new_data["detail_21"])<float(standard["detail_8down"]))or (float(new_data["detail_22"])<float(standard["detail_9down"])) or (float(new_data["detail_23"])<float(standard["detail_10down"])) or (float(new_data["detail_24"])<float(standard["detail_11down"])) or (float(new_data["detail_25"])<float(standard["detail_12down"])) or (float(new_data["detail_26"])<float(standard["detail_13down"])):
        quality_status=False
    return quality_status
#紀錄那些資料有異常
def regular():
    regular_lst=[]
    for new_data in data1:
        for i in range(13):
            a='detail_'+str(i+1)
            up='detail_'+str(i+1)+'up'
            b='detail_'+str(i+14)
            down='detail_'+str(i+1)+'down'
            if (float(new_data[a])>float(standard[up])) or (float(new_data[b])<float(standard[down])):
                regular_lst.append(i+1)
    list2 = list(set(regular_lst))
    list2.sort()
    return list2
#計算正確率
def yield_Machine(data200):
    pass_rate=0
    for i in data200:
        if status(i):
            pass_rate+=1
    return (pass_rate/len(data1))*100
#個別資料是否有異常
def yield_each(detail):
    sup=detail+'up'
    sdown=detail+'down'
    if (float(new_data[detail])>float(standard[sup])) or (float(new_data[detail])<float(standard[sdown])):
        return False
    else:
        return True
#特定detail的最大值
def get_max(detail):
    max=float(new_data[detail])
    for i in data:
        if float(i[detail])>max:
            max=float(i[detail])
    return max
#特定detail的最小值
def get_min(detail):
    min=float(new_data[detail])
    for i in data:
        if float(i[detail])<min:
            min=float(i[detail])
    return min
#特定detail在100分鐘內是否有異常
def get_colormax(detail):
    if get_max(detail)>float(standard[detail+'up']) or get_max(detail)<float(standard[detail+'down']):
        return False
    else:
        return True
def get_colormin(detail):
    if get_min(detail)>float(standard[detail+'up']) or get_min(detail)<float(standard[detail+'down']):
        return False
    else:
        return True
#繪製正確率圓餅圖
def get_Donut(correct,mistake):
    fig=plt.figure(14)
    size_of_groups=[correct,mistake]
    plt.pie(size_of_groups,colors=['green','red'])
    my_circle=plt.Circle( (0,0), 0.7, color='#E2E2E2')
    plt.text(0., 0.,str(correct)+'%', horizontalalignment='center', verticalalignment='center',color='green',size=30)
    fig.patch.set_facecolor('#E2E2E2')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('dinkle/static/image/donut.png')
#get_Donut_image=get_Donut(yield_Machine(data),100-yield_Machine(data))
#取得最新一筆資料的轉速
def get_Speed():
    new_speed=new_data['Speed']
    return new_speed
#取得最新一筆資料的頻率
def get_Frequency():
    new_fre=new_data['frequency']
    return new_fre
#取得最進100筆資料的最大轉速
def max_speed():
    max=float(new_data['Speed'])
    for i in data:
        if float(i['Speed'])>max:
            max=float(i['Speed'])
    return max
#取得最進100筆資料的最小轉速
def min_speed():
    min=float(new_data['Speed'])
    for i in data:
        if float(i['Speed'])<min:
            min=float(i['Speed'])
    return min
#取得最進100筆資料的最大頻率
def max_Frequency():
    max=float(new_data['frequency'])
    for i in data:
        if float(i['frequency'])>max:
            max=float(i['frequency'])
    return max
#取得最進100筆資料的最小頻率
def min_Frequency():
    min=float(new_data['frequency'])
    for i in data:
        if float(i['frequency'])<min:
            min=float(i['frequency'])
    return min
#紀錄異常的時間和detail
def errorlst(new_d):
    errorlst=[]
    for new_data in new_d:
        if (float(new_data["detail_1"])>float(standard["detail_1up"])) or (float(new_data["detail_2"])>float(standard["detail_2up"])) or (float(new_data["detail_3"])>float(standard["detail_3up"])) or (float(new_data["detail_4"])>float(standard["detail_4up"])) or (float(new_data["detail_5"])>float(standard["detail_5up"])) or (float(new_data["detail_6"])>float(standard["detail_6up"]))or (float(new_data["detail_7"])>float(standard["detail_7up"]))or (float(new_data["detail_8"])>float(standard["detail_8up"]))or (float(new_data["detail_9"])>float(standard["detail_9up"]))or (float(new_data["detail_10"])>float(standard["detail_10up"]))or (float(new_data["detail_11"])>float(standard["detail_11up"]))or (float(new_data["detail_12"])>float(standard["detail_12up"]))or (float(new_data["detail_13"])>float(standard["detail_13up"])):
            regular_lst=[]
            for i in range(13):
                a='detail_'+str(i+1)
                up='detail_'+str(i+1)+'up'
                b='detail_'+str(i+14)
                down='detail_'+str(i+1)+'down'
                if (float(new_data[a])>float(standard[up])) or (float(new_data[b])<float(standard[down])):
                    regular_lst.append(i+1)
            errorlst.append({'time':new_data['time'],'error':regular_lst})
        elif (float(new_data["detail_14"])<float(standard["detail_1down"])) or (float(new_data["detail_15"])<float(standard["detail_2down"])) or (float(new_data["detail_16"])<float(standard["detail_3down"])) or (float(new_data["detail_17"])<float(standard["detail_4down"])) or (float(new_data["detail_18"])<float(standard["detail_5down"])) or (float(new_data["detail_19"])<float(standard["detail_6down"]))or (float(new_data["detail_20"])<float(standard["detail_7down"]))or (float(new_data["detail_21"])<float(standard["detail_8down"]))or (float(new_data["detail_22"])<float(standard["detail_9down"])) or (float(new_data["detail_23"])<float(standard["detail_10down"])) or (float(new_data["detail_24"])<float(standard["detail_11down"])) or (float(new_data["detail_25"])<float(standard["detail_12down"])) or (float(new_data["detail_26"])<float(standard["detail_13down"])):
            regular_lst=[]
            for i in range(13):
                a='detail_'+str(i+1)
                up='detail_'+str(i+1)+'up'
                b='detail_'+str(i+14)
                down='detail_'+str(i+1)+'down'
                if (float(new_data[a])>float(standard[up])) or (float(new_data[b])<float(standard[down])):
                    regular_lst.append(i+1)
            errorlst.append({'time':new_data['time'],'error':regular_lst})
    return errorlst
#對時間做操作
def slicedate(lst):
    timeString=lst['time']
    time_lst={}
    struct_time = time.strptime(timeString, "%Y-%m-%d %H:%M:%S")
    day_timeString = time.strftime("%Y/%m/%d", struct_time)
    hour_timeString=time.strftime("%I:%M %p", struct_time)
    time_lst.update({'time':day_timeString,'hour':hour_timeString})
    return time_lst
def error_list(lst):
    newlst=[]
    for i in lst:
        a=slicedate(i)
        b=i['error']
        newlst.append({'time':a['time'],'hour':a['hour'],'error':b})
    return newlst
#記錄各detail出錯總次數
def statistics():
    count={'detail_1':0,'detail_2':0,'detail_3':0,'detail_4':0,'detail_5':0,'detail_6':0,'detail_7':0,'detail_8':0,'detail_9':0,'detail_10':0,'detail_11':0,'detail_12':0,'detail_13':0,}
    for new_data in data1:
        if (float(new_data["detail_1"])>float(standard["detail_1up"])) or (float(new_data["detail_2"])>float(standard["detail_2up"])) or (float(new_data["detail_3"])>float(standard["detail_3up"])) or (float(new_data["detail_4"])>float(standard["detail_4up"])) or (float(new_data["detail_5"])>float(standard["detail_5up"])) or (float(new_data["detail_6"])>float(standard["detail_6up"]))or (float(new_data["detail_7"])>float(standard["detail_7up"]))or (float(new_data["detail_8"])>float(standard["detail_8up"]))or (float(new_data["detail_9"])>float(standard["detail_9up"]))or (float(new_data["detail_10"])>float(standard["detail_10up"]))or (float(new_data["detail_11"])>float(standard["detail_11up"]))or (float(new_data["detail_12"])>float(standard["detail_12up"]))or (float(new_data["detail_13"])>float(standard["detail_13up"])):
            for i in range(13):
                a='detail_'+str(i+1)
                up='detail_'+str(i+1)+'up'
                b='detail_'+str(i+14)
                down='detail_'+str(i+1)+'down'
                if (float(new_data[a])>float(standard[up])) or (float(new_data[b])<float(standard[down])):
                    c=count[a]+1
                    count.update({a:c})
        elif (float(new_data["detail_14"])<float(standard["detail_1down"])) or (float(new_data["detail_15"])<float(standard["detail_2down"])) or (float(new_data["detail_16"])<float(standard["detail_3down"])) or (float(new_data["detail_17"])<float(standard["detail_4down"])) or (float(new_data["detail_18"])<float(standard["detail_5down"])) or (float(new_data["detail_19"])<float(standard["detail_6down"]))or (float(new_data["detail_20"])<float(standard["detail_7down"]))or (float(new_data["detail_21"])<float(standard["detail_8down"]))or (float(new_data["detail_22"])<float(standard["detail_9down"])) or (float(new_data["detail_23"])<float(standard["detail_10down"])) or (float(new_data["detail_24"])<float(standard["detail_11down"])) or (float(new_data["detail_25"])<float(standard["detail_12down"])) or (float(new_data["detail_26"])<float(standard["detail_13down"])):
            for i in range(13):
                a='detail_'+str(i+1)
                up='detail_'+str(i+1)+'up'
                b='detail_'+str(i+14)
                down='detail_'+str(i+1)+'down'
                if (float(new_data[a])>float(standard[up])) or (float(new_data[b])<float(standard[down])):
                    c=count[a]+1
                    count.update({a:c})
    return count
#繪製記錄圖
def sta_img():
    fig=plt.figure(31)
    left = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    labels=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    height = statistics().values()
    plt.figure(figsize=(15,5))
    plt.xlabel('(Detail)')
    plt.ylabel('(frequency)')
    plt.bar(left, height,color='#E29F9F',tick_label=labels)
    plt.savefig('dinkle/static/image/statics.png')
#sta_img()
def analysis():
    regular_lst=[]
    for new_data in data1:
        for i in range(13):
            a='detail_'+str(i+1)
            up='detail_'+str(i+1)+'up'
            b='detail_'+str(i+14)
            down='detail_'+str(i+1)+'down'
            if (float(new_data[a])>float(standard[up])):
                regular_lst.append({a:[i+1,new_data[a],new_data[b],0]})
            if (float(new_data[b])<float(standard[down])):
                regular_lst.append({a:[i+1,new_data[a],new_data[b],1]})
        if regular_lst!=[]:
            break
    return regular_lst

