from core import image, log_creater
import time
from . import back
'''

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

'''
def routine1():
    if back.backhome():
        image.co("battle.png")
        while True:

            while image.co("patrol.png"):

                image.co("experience.png")

                image.sc("nowloading.png",5)############

                image.co("experience_j.png")

                image.sc("nowloading.png",5)############

                if image.co("nowomen.png"):
                    image.co("autoteam.png")
            
                image.sc("nowloading.png",5)############

                image.co("skipbattle.png")

                image.sc("nowloading.png",5)############

                image.co("skipbattle_max.png")
            
                #这个得以后补上roi,先这么用着
                if image.co("0.png"):
                    break
            #image.co("coin.png")
'''

routine_experience_complete = False

routine_coin_complete = False

routine_exercice_complete = False

#日常经验本
def routine_experience():
    global routine_experience_complete
    if back.backhome():
        image.co("battle.png")
        while True:
            while not image.co("patrol.png"):
                time.sleep(2)

            while not image.co("experience.png"):
                time.sleep(2)
            
            if image.co("experience_complete.png",True,0.999):
                log = log_creater("每日经验本完成")
                print(log)
                return

            while not image.co("experience_j.png",0.9):
                time.sleep(2)
                
            while True:
                time.sleep(2)
                if image.co("nowomen.png"):
                    image.co("autoteam.png")
                if image.co("skip_complete.png",False):
                    while not image.co("patrol_ui.png",False):
                        image.co("back.png")
                    log = log_creater.write_log("每日经验本完成")
                    print(log)
                    return
                if image.co("skipbattle.png",True,0.9):
                    break

            while not image.co("skipbattle_max.png"):
                time.sleep(1)

            while not image.co("skipbattle_confirm.png"):
                time.sleep(1)

            while not image.co("skipbattle_complete.png"):
                time.sleep(1)
            
            while not image.co("experience_complete.png",False,0.95):
                time.sleep(1)
            
            routine_experience_complete = True
            log = log_creater.write_log("每日经验本完成")
            print(log)
            return
        

            #image.co("coin.png")

#日常金币本
def routine_coin2():
    if back.backhome():
        image.co("battle.png")
        while True:
            while not image.co("patrol.png"):
                time.sleep(2)
            
            # if image.co("coin_complete.png",False,0.999):
            #     log = log_creater.write_log("每日金币本完成")
            #     print(log)
            #     return

            while not image.co("coin.png"):
                time.sleep(2)

            while not image.co("coin_j.png",0.9):
                time.sleep(2)
                
            while True:
                time.sleep(2)
                if image.co("nowomen.png"):
                    image.co("autoteam.png")
                
                if image.co("skip_complete.png",False):
                    while not image.co("patrol_ui.png",False):
                        image.co("back.png")
                    log = log_creater.write_log("每日金币本完成")
                    print(log)
                    return
                if image.co("skipbattle.png",True,0.9):
                    break

            while not image.co("skipbattle_max.png"):
                time.sleep(1)

            while not image.co("skipbattle_confirm.png"):
                time.sleep(1)

            while not image.co("skipbattle_complete.png"):
                time.sleep(1)
            
            while not image.co("coin_complete.png",False,0.95):
                 time.sleep(1)
                
            log = log_creater.write_log("每日金币本完成")
            print(log)
            return

#日常金币本改良版
def routine_coin():

    while True:
        if image.co("patrol.png"):
            break
        if image.co("routine_ui.png",False):
            break
        else:
            back.backhome()

    while True:
        while not image.co("coin.png"):
            time.sleep(2)

        while not image.co("coin_j.png",0.9):
            time.sleep(2)
            
        while True:
            time.sleep(2)
            if image.co("nowomen.png"):
                image.co("autoteam.png")
            
            if image.co("skip_complete.png",False):
                while not image.co("patrol.png",False):
                    image.co("back.png")
                log = log_creater.write_log("每日金币本完成")
                print(log)
                return
            if image.co("skipbattle.png",True,0.9):
                break

        while not image.co("skipbattle_max.png"):
            time.sleep(1)

        while not image.co("skipbattle_confirm.png"):
            time.sleep(1)

        while not image.co("skipbattle_complete.png"):
            time.sleep(1)
        
        while not image.co("coin_complete.png",False,0.95):
                time.sleep(1)
            
        log = log_creater.write_log("每日金币本完成")
        print(log)
        return

#日常演习本
def routine_exercice():
    if back.backhome():
        image.co("battle.png")
        while True:
            while not image.co("exercise.png"):
                time.sleep(2)
            
            # if image.co("coin_complete.png",False,0.95):
            #     log = log_creater.write_log("每日日常演习本完成")
            #     print(log)
            #     return

            while not image.co("equipment.png.png"):
                time.sleep(2)

            while not image.co("equipment_j.png.png",0.9):
                time.sleep(2)
                
            while True:
                time.sleep(2)
                if image.co("nowomen.png"):
                    image.co("autoteam.png")
                if image.co("skipbattle.png",True,0.9):
                    break

            while not image.co("skipbattle_max.png"):
                time.sleep(1)

            while not image.co("skipbattle_confirm.png"):
                time.sleep(1)

            while not image.co("skipbattle_complete.png"):
                time.sleep(1)
                
            log = log_creater("每日金币本完成")
            print(log)
            return


#体力购买三次
def routine_staminapurchase(time_):
    # while not image.co("stamina_ui.png",False):#image.cos("stamina.png",0,150,0,0,0.9):
    #     time.sleep(1)
    #     image.cos("stamina.png",0,150,0,0,0.9)
    #     image.co("stamina_ui.png",False)
    #     image.co("back.png",True,0.95)
    cout = 0
    while cout<time_:
        while not image.cos("stamina.png",0,150,0,0,0.9):
            image.co("back.png",True,0.9)
    
        while not image.co("stamina_ui.png",False):
            image.cos("stamina.png",0,150,0,0,0.9)

        while not image.cos("stamina_ui.png",0,300,0,80):
            time.sleep(1)

        while not image.co("stamina_purchase_confirm.png"):
            time.sleep(1)
        while not image.co("stamina_purchase_shutdown.png"):
            time.sleep(1)
        cout += 1

def routine_task_mail(back_ = 0):
    back.backhome()
    while not image.co("task_recieve.png",True,2,0.7):
        image.co("task.png",True,2,0.7)
    
    while not image.co("task_recieved.png",True,2,0.7):
        while not image.co("task_shutdown.png",True,2,0.7):
            image.co("task_recieved.png",True,2,0.7)
            
    log = log_creater.write_log("没用可以领取的任务了")
    print(log)

    while not image.co("passports_ui.png",True,2,0.7):
        image.co("Passports.png",True,2,0.7)

    while not image.co("passport_recieved.png",False):
        image.co("task_shutdown.png",True,2,0.7)
        image.co("passport_recieve.png")
    
    log = log_creater.write_log("没用可以领取的通行证了")
    print(log)

    back.backhome()

    while not image.co("recieve_mail.png",False):
        image.co("passport_recieve.png")
    
    while not image.co("mail_shutdown.png",False):
        image.co("recieve_mail.png")
    
    image.co("mail_shutdown.png")

    image.co("xshutdown.png")
    

    if back_ == 0:
        back.backhome()
        


    