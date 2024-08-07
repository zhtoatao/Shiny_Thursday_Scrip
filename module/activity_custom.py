from core import image_custom, log_creater,image
import time
from . import back,activity_lose


#活动图开荒
def routine_clean_activity_task(team):#是否自动组队,0执行，1不执行
    #看看进没进battle页，没进就跑回主页
    # while True:
    #     if not image_custom.co("activity_.png",False,0.7):
    #         while True:
    #             if not image_custom.co("battle.png"):
    #                 print("没走back")
    #                 back.backhome
    #                 print("走back了")
    #                 image_custom.co("battle.png")
    #                 image_custom.co("battle2.png")
    #                 break
    #             if not image_custom.co("battle2.png"):
    #                 back.backhome
    #                 image_custom.co("battle2.png")
    #                 image_custom.co("battle.png")
    #                 break
    

    #写了半天不会写。凑合用吧，还是会回主页的
        
    while not image_custom.co("battle.png",True):
        if image_custom.co("back.png",True):
            continue
        if image_custom.co("battle2.png",False):
            break
        
    
    while not image_custom.co("battle.png",True):
        if image_custom.co("battle2.png",False):
            break
        time.sleep(1)

    while not image_custom.co("activity_.png",True):
        if image_custom.co("battle2.png",False):
            break
        if image_custom.co("back.png",True):
            continue
        time.sleep(1)

    while not image_custom.co("activity.png"):
        time.sleep(1)

    #循环找到unfinish的关卡
    #如果找不到未完成了，就去下一页
    #如果打完发现上锁了也去下一页
    #如果下一页也全部完成了就直接return，全部结束
    lock_ = 0
    while True:
        while not image_custom.co("shutdown.png"):
            if lock_ == 0:
                if image_custom.co("locked.png",False,1,0.95):
                    log = log_creater.write_log("下半未解锁，下一页继续")
                    print(log)
                    image_custom.cos("task_hard_dim.png",0,0,0,0,2,0.8)
                    lock_ +=1
                    continue
            
            if lock_ == 1:
                if image_custom.co("locked.png",False,1,0.95):
                    log = log_creater.write_log("下半未解锁，开荒完成")
                    print(log)
                    return

            if image_custom.co("unfinished.png",False,1):
                break

            if image_custom.cos("task_hard_dim.png",0,0,0,0,2,0.8):
                time.sleep(1)
                continue 

            else:
                log = log_creater.write_log("活动开荒完成")
                print(log)
                return

        if image_custom.co("unfinished.png"):
            time.sleep(1)
            #组不组队
            if team == 0:
                while not image_custom.co("team.png"):
                    time.sleep(1)
                while not image_custom.co("team_confirm.png"):
                    time.sleep(1)
                    team += 1
########################################################################
         
        while True:
            image_custom.co("attack.png",True,1)
            time.sleep(1)
            if image_custom.co("auto_dim.png",True,2,0.9):
                time.sleep(1)
                break
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("battle_win.png"):
                break
##########################################################################
         
        while True:
            if image_custom.co("auto_dim.png",True,2,0.9):
                time.sleep(1)
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("battle_win.png"):
                break
##########################################################################
        #超时点圈圈，超时检测没成功，算了，这个确实不好做
        #current_time = time.time()
        # while not image_custom.co("launch.png"):
        #     start_time = time.time()
        #     if current_time - start_time > 10:
        #         log = log_creater.write_log("没有成功起飞")
        #         print(log)
        #         break

        while not image_custom.co("battle_complete.png",False):
            time.sleep(1)
            image_custom.co("battle_win.png")
            time.sleep(1)

        while not image_custom.co("next.png"):
            time.sleep(1)
            image_custom.co("battle_complete.png")
            time.sleep(3)

        while not image_custom.co("finished3.png",False):
            image_custom.co("next.png")
            image_custom.co("shutdown.png")
                

#活动高难开荒
def routine_clean_veryhard_activity_task(team_veryhard = 0):#是否自动组队,0执行，1不执行
        
    while not image_custom.co("battle.png",True):
        if image_custom.co("back.png",True):
            continue
        if image_custom.co("battle2.png",False):
            break
        
    
    while not image_custom.co("battle.png",True):
        if image_custom.co("battle2.png",False):
            break
        time.sleep(1)

    while not image_custom.co("activity_.png",True):
        if image_custom.co("battle2.png",False):
            break
        if image_custom.co("back.png",True):
            continue
        time.sleep(1)

    while not image_custom.co("activity.png"):
        time.sleep(1)

    #循环找到unfinish的关卡
    while True:
        while not image_custom.co("shutdown.png"):

            while not image_custom.co("very_hard_bright.png",False,1):
                
                if image_custom.co("very_hard_dim.png"):
                    break
            break
        
        find_unfinished = 0
        while not image_custom.co("very_hard_unfinished.png",False):
            if find_unfinished % 2 == 0:
                image.swipe(936,200,952,540,1000)
            if find_unfinished % 2 == 1:
                image.swipe(936,540,952,200,1000)
            if find_unfinished > 3:
                log = log_creater.write_log("未找到需要开荒的高难")
                print(log)
                return
            find_unfinished +=1


        if image_custom.co("very_hard_unfinished.png"):
            time.sleep(1)
            #组不组队
            if team_veryhard == 0:
                while not image_custom.co("team.png"):
                    time.sleep(1)
                while not image_custom.co("team_confirm.png"):
                    time.sleep(1)
                    team_veryhard += 1
        
#######################################################################################################
        lose_=0
        while True:
            image_custom.co("veryhard_attack.png",True,1)
            time.sleep(1)
            if image_custom.co("auto_dim.png",False):
                time.sleep(1)
                break
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("veryhard_attack_dim.png",False):
                log = log_creater.write_log("票数不够，出击不能，停止开荒")
                print(log)
                return
######################################################################################################
######################################################################################################
         
        while True:
            if image_custom.co("auto_dim.png"):
                time.sleep(1)
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("battle_win.png"):
                break

######################################################################################################

        while not image_custom.co("battle_complete.png",False):
            time.sleep(1)
            image_custom.co("battle_win.png")
            time.sleep(1)

        while not image_custom.co("next.png"):
            time.sleep(1)
            image_custom.co("battle_complete.png")
            time.sleep(3)

        image_custom.co("next.png")

#活动一日一次挑战
def routine_activity_once(team = 0,team_ = 0):#是否自动组队,0执行，1不执行
        
    while not image_custom.co("battle.png",True):
        if image_custom.co("back.png",True):
            continue
        if image_custom.co("battle2.png",False):
            break
        
    
    while not image_custom.co("battle.png",True):
        if image_custom.co("battle2.png",False):
            break
        time.sleep(1)

    while not image_custom.co("activity_.png",True):
        if image_custom.co("battle2.png",False):
            break
        if image_custom.co("back.png",True):
            continue
        time.sleep(1)

    while not image_custom.co("activity.png"):
        time.sleep(1)

    #循环找到一日一回的关卡
    #如果完成了就直接return，全部结束
    while True:
        while not image_custom.co("shutdown.png"):

            while not image_custom.co("very_hard_bright.png",False,1):
                
                if image_custom.co("very_hard_dim.png"):
                    break
            break
        
        find_unfinished = 0
        while not image_custom.co("very_hard_unfinished_once.png",False):
            if find_unfinished % 2 == 0:
                image.swipe(736,200,752,540,1000)
            if find_unfinished % 2 == 1:
                image.swipe(936,540,952,200,1000)
            if find_unfinished > 100:
                if image_custom.co("very_hard_locked.png",False):
                    log = log_creater.write_log("一日一回已完成")
                    print(log)
                    return
                log = log_creater.write_log("一日一回已完成")
                print(log)
                return
            find_unfinished +=1


        if image_custom.cos("very_hard_unfinished_once.png",0,0,0,0,2,0.7):
            time.sleep(1)
            #组不组队,要不要按属性组
            if team == 0:
                while not image_custom.co("team.png"):
                    time.sleep(1)
                if team_ == 1:
                    while not image_custom.co("fire.png"):
                        time.sleep(1)
                        team += 1
                    image_custom.co("team_confirm.png")
                if team_ == 2:
                    while not image_custom.co("water.png"):
                        time.sleep(1)
                        team += 1
                    image_custom.co("team_confirm.png")
                if team_ == 3:
                    while not image_custom.co("thunder.png"):
                        time.sleep(1)
                        team += 1
                    image_custom.co("team_confirm.png")
                if team_ == 4:
                    while not image_custom.co("light.png"):
                        time.sleep(1)
                        team += 1
                    image_custom.co("team_confirm.png")
                if team_ == 5:
                    while not image_custom.co("darkness.png"):
                        time.sleep(1)
                        team += 1
                    image_custom.co("team_confirm.png")
                if team_ == 0:
                    while not image_custom.co("team_confirm.png"):
                        time.sleep(1)
                        team += 1

                
        
        #进入战斗了，因为会有各自突发情况，所以全部进行条件判断
###################################################################################
         
        while True:
            image_custom.co("veryhard_attack.png",True,1)
            time.sleep(1)
            if image_custom.co("auto_dim.png",False):
                time.sleep(1)
                break
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("veryhard_attack_dim.png",False):
                log = log_creater.write_log("票数不够，出击不能，停止开荒")
                print(log)
                return
            if image_custom.co("battle_win.png"):
                break
            if activity_lose.routine_activity_once_lose():
                continue

#########################################################################
#########################################################################
        while True:
            if image_custom.co("auto_dim.png"):
                time.sleep(1)
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("battle_win.png"):
                break
            if activity_lose.routine_activity_once_lose():
                continue
##########################################################################

        while not image_custom.co("battle_complete.png",False):
            time.sleep(1)
            image_custom.co("battle_win.png")
            time.sleep(1)
            if activity_lose.routine_activity_once_lose():
                continue

        while not image_custom.co("next.png"):
            time.sleep(1)
            image_custom.co("battle_complete.png")
            return

        image_custom.co("next.png")

#活动困难扫荡，可以选第10还是第9
#team_veryhard:是否自动组队,0执行，1不执行
#which:扫荡哪关，0第九关，1第十关
def routine_sweepdown_activity_task(team = 0,which = 1):
        
    while not image_custom.co("battle.png",True):
        if image_custom.co("back.png",True):
            continue
        if image_custom.co("battle2.png",False):
            break
        
    
    while not image_custom.co("battle.png",True):
        if image_custom.co("battle2.png",False):
            break
        time.sleep(1)

    while not image_custom.co("activity_.png",True):
        if image_custom.co("battle2.png",False):
            break
        if image_custom.co("back.png",True):
            continue
        time.sleep(1)

    while not image_custom.co("activity.png"):
        time.sleep(1)

    #进hard
    while not image_custom.co("task_hard_bright.png"):
        image_custom.co("task_hard_dim.png")

    while not image_custom.co("attack.png",False):
        if image_custom.co("unfinished_task.png",False):
            log = log_creater.write_log("还有关卡没有完成，停止任务")
            print(log)
            return
        image_custom.cos("task_hard_bright.png",0,0,90,0)



    #第几关，第十关就继续，第九关就点一下箭头
    while True:
        if which == 1:
            time.sleep(1)
            log = log_creater.write_log("扫桑第十关")
            print(log)
            break

        if which == 0:
            image_custom.cow("next_left.png")
            log = log_creater.write_log("扫荡第九关")
            print(log)
            break

    if team == 0:
        while not image_custom.co("team.png"):
            time.sleep(1)
        while not image_custom.co("team_confirm.png"):
            time.sleep(1)
        team += 1
####################################################################################
    while not image_custom.co("team_confirm.png",False):
        image_custom.cos("attack.png",0,0,0,100)
        if image_custom.co("stomia_purchase.png",False):
            log = log_creater.write_log("体力不足以扫荡，停止任务")
            print(log)
            return
####################################################################################
    image_custom.co("max.png")
    image_custom.co("team_confirm.png")

    while not image_custom.co("sweepdown_complete.png"):
        time.sleep(1)

    image_custom.co("sweepdown_complete.png")

    log = log_creater.write_log("扫荡完成")
    print(log)

    while not image_custom.co("task_daily.png",False):
        image_custom.co("back.png")
    
    while not image_custom.co("recieve_all.png"):
        image_custom.co("task_daily.png")
    
    while not image_custom.co("shutdown.png"):
        image_custom.co("recieve_all.png")

    back.backhome()