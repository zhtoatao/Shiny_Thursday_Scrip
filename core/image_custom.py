import os
import subprocess
import cv2
import time
import random
from . import log_creater


current_folder = os.getcwd()
adb_path = None
adb_port = None

#简单的点击动作
def click(x, 
          y, 
          sleeptime,
          maxoffset=10):
    adb_command = ['"{}"'.format(adb_path), "-s", "127.0.0.1:{}".format(adb_port),]
    adb_command_str = " ".join(adb_command)
    
    random_x = x + random.randint(0-maxoffset,maxoffset)
    random_y = y + random.randint(0-maxoffset,maxoffset)
    command = f"{adb_command_str} shell input tap {random_x} {random_y}"
    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    log = log_creater.write_log(f"图片中心点击: "+str(x)+","+str(y))
    print(log)

    time.sleep(sleeptime)

#简单滑动操�?
def swipe(x1, 
          y1, 
          x2, 
          y2, 
          duration,
          waittime=2):
    adb_command = ['"{}"'.format(adb_path), "-s", "127.0.0.1:{}".format(adb_port),]
    adb_command_str = " ".join(adb_command)
    
    random_r1 = random.randint(-10,10)
    random_r2 = random.randint(-10,10)
    command = f"{adb_command_str} shell input swipe {x1 + random_r1} {y1 + random_r2} {x2+ random_r1} {y2 - random_r2}  {duration}"
    subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    time.sleep(waittime)


#adb截屏指令
def screen_shot():
    adb_command = ['"{}"'.format(adb_path), "-s", "127.0.0.1:{}".format(adb_port),]
    adb_command_str = " ".join(adb_command)

    screenshot_file = os.path.join(current_folder, "screenshot", "screenshot.png")
    subprocess.run(f"{adb_command_str} exec-out screencap -p > {screenshot_file}", shell=True, check=True)
    return screenshot_file


#check only once,没check到就false，check到了就true，可以选择点和不点
def co(target_img,
       click_ = True,
       sleeptime=2,
       threshold=0.8,
       cv_method=cv2.TM_CCOEFF_NORMED):
    
    target = os.path.join(current_folder, "target_custom", target_img)
    screenshot = cv2.imread(screen_shot())
    target_image = cv2.imread(target)
    result = cv2.matchTemplate(screenshot, target_image, cv_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        if click_:
            done:str = "执行操作：直接点击"
        else:
            done:str = "不执行点击操作"

        log = log_creater.write_log(f"找到 {target_img} 力,{done}")
        print(log)
        if click_:
            center_x = max_loc[0] + target_image.shape[1] // 2
            center_y = max_loc[1] + target_image.shape[0] // 2
            click(center_x,center_y,sleeptime)
        return True
    else:
        log = log_creater.write_log(f"找不到 {target_img}")
        print(log)
        return False

#sleep after check,check到了就等一段时间，不点击
#一般就是给nowlaoding用的
def sc(target_img,
       sleeptime=5,
       threshold=0.8,
       cv_method=cv2.TM_CCOEFF_NORMED):
    
    target = os.path.join(current_folder, "target_custom", target_img)
    screenshot = cv2.imread(screen_shot())
    target_image = cv2.imread(target)
    result = cv2.matchTemplate(screenshot, target_image, cv_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        log = log_creater.write_log(f"找到 {target_image} ,等待 {sleeptime}秒")
        time.sleep(sleeptime)

#check offset,check到了以后按偏移量进行点击
def cos(target_img,
        x_leftwards=0,
        x_rightwards=0,
        y_upwards=0,
        y_downwards=0,
        sleeptime=2,
        threshold=0.8,
        cv_method=cv2.TM_CCOEFF_NORMED):
    
    target = os.path.join(current_folder, "target_custom", target_img)
    screenshot = cv2.imread(screen_shot())
    target_image = cv2.imread(target)
    result = cv2.matchTemplate(screenshot, target_image, cv_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        log = log_creater.write_log(f"找到 {target_img} 力，执行操作：偏移点击")
        print(log)
        center_x = max_loc[0] + target_image.shape[1] // 2 - x_leftwards + x_rightwards
        center_y = max_loc[1] + target_image.shape[0] // 2 - y_downwards + y_upwards
        click(center_x,center_y,sleeptime)
        return True
    else:
        log = log_creater.write_log(f"找不到 {target_img}")
        print(log)
        return False

#simple check only once,给一直在运行的检测用的，不进行截图，只读取截图，必然点击
def sco(target_img,
       sleeptime=2,
       threshold=0.8,
       cv_method=cv2.TM_CCOEFF_NORMED):
    
    target = os.path.join(current_folder, "target_custom", target_img)
    screenshot_file = os.path.join(current_folder, "screenshot", "screenshot.png")
    screenshot = cv2.imread(screenshot_file)
    target_image = cv2.imread(target)
    result = cv2.matchTemplate(screenshot, target_image, cv_method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        log = log_creater.write_log(f"找到 {target_img} 力,执行操作：直接点击")
        print(log)
        center_x = max_loc[0] + target_image.shape[1] // 2
        center_y = max_loc[1] + target_image.shape[0] // 2
        click(center_x,center_y,sleeptime)
        return True
    else:
        return False
    
# check once while,没有找到的话就会一直找
def cow(target_img,
       click_ = True,
       sleeptime=2,
       threshold=0.8,
       cv_method=cv2.TM_CCOEFF_NORMED):
    
    target = os.path.join(current_folder, "target_custom", target_img)
    target_image = cv2.imread(target)
    
    while True:
        screenshot = cv2.imread(screen_shot())
        result = cv2.matchTemplate(screenshot, target_image, cv_method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= threshold:
            if click_:
                done = "执行操作：直接点击"
            else:
                done = "不执行点击操作"

            log = log_creater.write_log(f"找到 {target_img} 力,{done}")
            print(log)
            if click_:
                center_x = max_loc[0] + target_image.shape[1] // 2
                center_y = max_loc[1] + target_image.shape[0] // 2
                click(center_x, center_y, sleeptime)
            return True
        else:
            log = log_creater.write_log(f"找不到 {target_img}，重新寻找")
            print(log)
            time.sleep(1)