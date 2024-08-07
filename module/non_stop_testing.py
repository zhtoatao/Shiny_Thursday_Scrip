#任务：不断检测是否有以下三种情况
#1.升级
#2.弹窗礼包
#3.网络连接异常

from core import image,image_non_stop, log_creater
import time
import threading

restart = threading.Event()
ct = 0

def nst():
    global ct
    if image_non_stop.co("buy.png",False):
        image_non_stop.co("shutdown.png")
        time.sleep(20)

    if image_non_stop.cos("internet_is_lose.png",0,0,150,0):
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
    if ct % 5 == 0:
        log = log_creater.write_log("------异常状况保持检测中！")
        print(log)
        ct +=1
    time.sleep(10)
        

