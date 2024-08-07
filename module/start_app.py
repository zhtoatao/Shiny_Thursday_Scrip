from core import image, log_creater
import time



#回到主页
def backhome():
    #回主界面
    while not image.co("home1.png",False):
        image.sc("nowloading.png",2)
        while not image.co("home2.png"):
            image.sc("nowloading.png",2)
            image.co("nowloading.png",False,5)
            image.co("back.png")
            if image.co("home1.png"):
                break


'''
#def co(target_img,
        click_ = True,
        sleeptime=5,
        threshold=0.8,
        cv_method=cv2.TM_CCOEFF_NORMED)
'''

#打开app后进入主页
#会点击更新，跳过签到，关闭公告
def startapp():

    #桌面找app
    image.co("app.png")

    #点击start，有更新就点更新
    while not image.co("loading.png",False,5):
        if image.co("home_announ.png",False,1):
            break
        image.sc("nowloading.png",5)
        time.sleep(2)
        image.co("start.png",True,5)
        time.sleep(2)
        image.co("update.png",True,5)
        time.sleep(2)
        if image.cos("newest.png",0,0,150,0):
            while not image.co("qooapp.png"):
                time.sleep(5)
            log = log_creater.write_log("请在qoo端口进行更新")
            print(log)
        if image.co("skip1.png",False,1):
            break
        if image.co("announ_shutdown.png",False,1):
            break
        if image.co("home_announ.png",False,1):
            break
        if image.co("task_shutdown.png",False,1):
            continue
                
    
    log = log_creater.write_log("游戏进主界面")
    print(log)
    
    #点击签到的skip
    while not image.co("announ_shutdown.png",False):
        if image.co("home_announ.png",False,1):
            break
        image.co("skip1.png",True,1)
        image.co("skip2.png",True,1)
        image.sc("nowloading.png",False,5)
        if image.co("friend.png",True,5):
            break
        if image.co("announ_shutdown.png",True,5):
            break
        
    
    log = log_creater.write_log("游戏签到完成")
    print(log)


    start_time = time.time()
    #点击公告的关闭按键
    while True:
        image.co("announ_shutdown.png",True,5)
        current_time = time.time()
        if image.co("home_announ.png",False,1):
            break
        if current_time - start_time > 4:
            log = log_creater.write_log("公告按钮获取超时")
            print(log)
            break
        
    
    log = log_creater.write_log("游戏公告关闭完成")
    print(log)



    #点击友情点收集的按钮
    start_time = time.time()
    while True:
        current_time = time.time()
        if image.co("home_announ.png",False,1):
            break
        image.co("announ_shutdown.png",True,5)
        if current_time - start_time > 8:
            log = log_creater.write_log("友情点获取超时")
            print(log)
            break
        

    log = log_creater.write_log("友情点获取完成")
    print(log)
    log = log_creater.write_log("游戏启动任务完成")
    print(log)


#大渔~大渔~（我也不太清楚算啥，收粉毛菜吧
def dayu():
    image.co("dayu.png")
    start_time = time.time()

    while not image.co("dayu_shutdwon.png"):
        image.co("skip1.png")
        image.co("skip2.png")
        image.co("nowloading.png",False,4)
        current_time = time.time()
        if current_time - start_time > 8:
            log = log_creater.write_log("大渔获取超时")
            print(log)
            break