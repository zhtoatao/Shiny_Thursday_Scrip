from core import image, log_creater
import time
from . import back

#日常演习本
def routine_equipment():
    log = log_creater.write_log("合同演习开始")
    print(log)
    if back.backhome():
        image.co("battle.png")
        while True:
            while not image.co("exercise.png",0.7):
                time.sleep(2)

            while not image.co("equipment.png"):
                time.sleep(2)

            while not image.co("equipment_j.png",0.9):
                time.sleep(2)
                
            while True:
                time.sleep(2)
                if image.co("nowomen.png"):
                    image.co("autoteam.png")
                if image.co("skip_complete.png",False):
                    while not image.co("exercise_ui.png",False):
                        image.co("back.png")
                    log = log_creater.write_log("每日装备本完成")
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
            
            while not image.co("exercise_ui.png"):
                image.co("skipbattle_complete.png")
                
            log = log_creater.write_log("每日装备经验本完成")
            print(log)
            return


def routine_skill():

    # if image.co("exercise_ui.png",False):
    #     log = log_creater.write_log("不退回主页，直接开始任务")
    #     print(log)
    
    while True:
        if not image.co("exercise_ui.png",False):
            while not (image.co("battle.png") or image.co("battle2.png")):
                back.backhome
            while not image.co("exercise.png"):
                time.sleep(2)
        else:
            log = log_creater.write_log("不退回主页，直接开始任务")
            print(log)

        while not image.co("exercise_ui.png",False):
                time.sleep(2)

        while not image.co("skill.png"):
            time.sleep(2)

        while not image.co("skill_j.png",0.9):
            time.sleep(2)

        while True:
            time.sleep(2)
            if image.co("nowomen.png"):
                image.co("autoteam.png")
            if image.co("skip_complete.png",False):
                while not image.co("exercise_ui.png",False):
                    image.co("back.png")
                log = log_creater.write_log("每日技能本完成")
                print(log)
                return True
            if image.co("skipbattle.png",True,0.9):
                break

        while not image.co("skipbattle_max.png"):
            time.sleep(1)

        while not image.co("skipbattle_confirm.png"):
            time.sleep(1)

        while not image.co("skipbattle_complete.png"):
            time.sleep(1)

        while not image.co("exercise_ui.png",False):
            image.co("skipbattle_complete.png")
            

        log = log_creater.write_log("每日技能本完成")
        print(log)
        return True
    
def routine_breakthrough(Attribute = "thunder"):

    # if routine_equipment():
    #     log = log_creater.write_log("不退回主页，继续任务")
    #     print(log)


    while True:
        if not image.co("exercise_ui.png",False):
            while not (image.co("battle.png") or image.co("battle2.png")):
                back.backhome
            while not image.co("exercise.png"):
                time.sleep(2)
        else:
            log = log_creater.write_log("不退回主页，继续任务")
            print(log)

        while not image.co("exercise_ui.png",False):
            time.sleep(2)

        while not image.co("breakthrough.png"):
            time.sleep(2)
        
        if Attribute == "fire":
            while not image.co("fire.png"):
                image.swipe(936,200,952,540,1000)
                time.sleep(1)
        if Attribute == "water":
            while not image.co("water.png"):
                image.swipe(936,200,952,540,1000)
                time.sleep(1)
        if Attribute == "thunder":
            while not image.co("thunder.png"):
                image.swipe(936,540,952,200,1000)
                print("滑动")
                time.sleep(1)

        if Attribute == "light":
            while not image.co("light.png"):
                image.swipe(936,540,952,200,1000)
                time.sleep(1)

        if Attribute == "darkness":
            while not image.co("darkness.png"):
                image.swipe(936,540,952,200,1000)
                time.sleep(1)
            

        while not image.co("breakthrough_j.png",0.9):
            time.sleep(2)

        while True:
            time.sleep(2)
            if image.co("nowomen.png"):
                image.co("autoteam.png")
            if image.co("skip_complete.png",False):
                while not image.co("exercise_ui.png",False):
                    image.co("back.png")
                log = log_creater.write_log("每日突破本完成")
                print(log)
                return True
            if image.co("skipbattle.png",True,0.9):
                break

        while not image.co("skipbattle_max.png"):
            time.sleep(1)

        while not image.co("skipbattle_confirm.png"):
            time.sleep(1)

        while not image.co("skipbattle_complete.png"):
            time.sleep(1)

        while not image.co("exercise_ui.png",False):
            image.co("skipbattle_complete.png")

        log = log_creater.write_log("每日突破本完成")
        print(log)
        return