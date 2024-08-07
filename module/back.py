from core import image, log_creater
import time
'''
#def co(target_img,
        click_ = True,
        sleeptime=5,
        threshold=0.8,
        cv_method=cv2.TM_CCOEFF_NORMED)
'''

def backhome():
    #回主界面
    while not image.co("home1.png",False,1,0.6):
        image.sc("nowloading.png",2)
        while not image.co("home2.png"):
            if image.co("home1.png",False,1,0.6):
                break
            image.sc("nowloading.png",2)
            time.sleep(1)
            image.co("back.png")
            image.cos("x_shutdown.png",0,250,0,0)
            
    log = log_creater.write_log("已到达主界面")
    print(log)
    return True