import threading
from module import start_app,routine,routine_exercise,activity_custom,task,non_stop_testing
from core import log_creater

ad = False
ad_lock = threading.Lock()

#sa, dy, bh, rt, rex, rea, rsp, spt, rao, raot, raot_, rsat, rct, rctt, rcvat, rcvatt, rctk, rctkt, rtm = 0

def allclick(sa, dy, bh, rt, rex, rea, rsp, spt, rao, raot, raot_, rsat, rct, rctt, rcvat, rcvatt, rctk, rctkt, rtm):
    
    global ad

    ad = False
    
    #1.打开app进入主页
    if sa == 1:
        start_app.startapp()
        print("---------打开app进入主页完成")

    #2.大渔~
    if dy == 1:
        start_app.dayu()
        print("---------大渔完成----------")


    #3.回到主页
    if bh == 1:
        start_app.backhome()
        print("---------回到主页完成----------")

    #4.日常经验+硬币本
    if rt == 1:
        routine.routine_experience()
        routine.routine_coin()
        print("---------日常经验+硬币本完成----------")

    #5.合同演习
    if rex == 1:
        routine_exercise.routine_equipment()
        routine_exercise.routine_skill()
        routine_exercise.routine_breakthrough(rea)
        print("---------合同演习完成----------")
        

    #6.体力购买
    if rsp == 1:
        routine.routine_staminapurchase(spt)
        print("---------体力购买完成----------")

    #活动
    #7.活动一日一回
    if rao == 1:
        activity_custom.routine_activity_once(raot,raot_)
        print("---------活动一日一回完成----------")

    #8.活动图扫荡
    if rsat == 1:
        activity_custom.routine_sweepdown_activity_task()
        print("---------活动图扫荡完成----------")

    #9.活动图开荒
    if rct == 1:
        activity_custom.routine_clean_activity_task(rctt)
        print("---------活动图开荒完成----------")

    #10.活动高难开荒
    if rcvat == 1:
        activity_custom.routine_clean_veryhard_activity_task(rcvatt)
        print("---------活动高难开荒完成----------")

    #11.主线图开荒
    if rctk == 1:
        task.routine_clean_task(rctkt)
        print("---------主线图开荒完成----------")

    #12.回主页领取任务，通行证，邮箱
    if rtm == 1:
        routine.routine_task_mail()
        print("---------回主页领取任务，通行证，邮箱完成----------")

    with ad_lock:
        ad = True
        

def nst():
    #检测突发情况
    while True:
        with ad_lock:
            if ad:
                log = log_creater.write_log("线程全部结束")
                print(log)
                break
        non_stop_testing.nst()

def thread_(sa, dy, bh, rt, rex, rea, rsp, spt, rao, raot, raot_, rsat, rct, rctt, rcvat, rcvatt, rctk, rctkt, rtm):
    t1 = threading.Thread(target=allclick(sa, dy, bh, rt, rex, rea, rsp, spt, rao, raot, raot_, rsat, rct, rctt, rcvat, rcvatt, rctk, rctkt, rtm))
    t2 = threading.Thread(target=nst)

    t1.start()
    t2.start()

    t1.join()
    t2.join()








