from core import image_custom, log_creater,image
import time

def routine_activity_once_lose():
    if image_custom.co("finished3.png",False):
        #找一日一回
        find_unfinished = 0
        while not image_custom.co("very_hard_unfinished_once.png",False):
            if find_unfinished % 2 == 0:
                image.swipe(736,200,752,540,1000)
            if find_unfinished % 2 == 1:
                image.swipe(936,540,952,200,1000)
            if find_unfinished > 10:
                log = log_creater.write_log("未找到一日一回")
                print(log)
                return
            find_unfinished +=1
        
        #找到了点进去
        if image_custom.cos("very_hard_unfinished_once.png",0,0,0,0,2,0.7):
            time.sleep(2)
        
        image_custom.cow("finished2.png")
    return True

