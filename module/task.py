from core import image_custom, log_creater,image
import time
from . import back


#活动剧情关开荒
def routine_clean_task(team = 0):#是否自动组队,0执行，1不执

    cout = 0
    team_ = team

    while not image_custom.co("battle.png",True):
        if image_custom.co("back.png",True):
            continue
        if image_custom.co("battle2.png",False):
            break
        
    
    while not image_custom.co("back.png",True):
        if image_custom.co("task.png",False):
            break
        time.sleep(2)

    while not image_custom.co("task.png",True):
        if image_custom.co("battle2.png",False):
            break
        if image_custom.co("back.png",True):
            continue
        time.sleep(1)

    #循环找到unfinish的关卡
    #else表示如果找不到未完成了，就去下一页
    #如果下一页也全部完成了就直接return，全部结束
    while True:
        
        while not image_custom.co("shutdown.png"):

            #关掉弹窗礼包
            if image_custom.cos("suddenly_shopping.png",0,40,0,570,2,0.65):
                    continue
            
            #简单模式里找unfinished，没有就去困难模式
            if image_custom.co("task_simple_bright.png",False,1):
                if image_custom.co("unfinished_task.png",False,1):
                    cout +=1
                    continue

                else:
                    image_custom.cos("task_hard_dim.png",0,0,0,0,2,0.9)
                    cout +=1
                    time.sleep(2)
            
            if image_custom.co("unfinished_task.png",False,1):
                    break

            #反过来
            if image_custom.co("task_hard_bright.png",False,1):

                if image_custom.co("unfinished_task.png",False,1):
                    cout +=1
                    continue

                else:
                    image_custom.cos("task_simple_dim.png",0,0,0,0,2,0.9)
                    cout +=1
                    print(f"{cout}")
                    time.sleep(2)
            
            

            if image_custom.co("unfinished_task.png",False,1):
                    break
            
            #这一页都没找到就去下一页
            if cout > 2:
                image_custom.cos("next_right.png",0,0,0,0,2,0.7)
                cout = 0

        #组队，只进行一次
        while not image_custom.co("team.png",False):
            image_custom.co("unfinished_task.png")
            time.sleep(2)

            #组不组队,
            while not team_ > 0:
                while not image_custom.co("team_confirm.png"):
                    if image_custom.co("team.png"):
                        team_ += 1
                        time.sleep(1)
        
####################################################################################################
         
        while True:
            image_custom.co("attack.png",True,1)
            time.sleep(1)
            if image_custom.co("auto_dim.png",False):
                time.sleep(1)
                break
            if image_custom.co("auto_bright.png",False):
                time.sleep(1)
                break
            if image_custom.co("battle_win.png"):
                break

        
        #超时点圈圈，超时检测没成功，算了，这个确实不好做
        #current_time = time.time()
        # while not image_custom.co("launch.png"):
        #     start_time = time.time()
        #     if current_time - start_time > 10:
        #         log = log_creater.write_log("没有成功起飞")
        #         print(log)
        #         break
###################################################################################################
###################################################################################################
        while True:
            if image_custom.co("auto_dim.png",True,2,0.9):
                time.sleep(1)
            if image_custom.co("auto_bright.png",False):
                time.sleep(2)
                break
            if image_custom.co("battle_win.png"):
                break

###################################################################################################
###################################################################################################

        while not image_custom.co("battle_complete.png",False):
            time.sleep(2)
            image_custom.co("battle_win.png")
            time.sleep(2)

        while not image_custom.co("next.png"):
            time.sleep(2)
            image_custom.co("battle_complete.png")
            time.sleep(3)
        image_custom.co("next.png")
                

