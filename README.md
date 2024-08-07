# Shiny_Tursday脚本源代码

这是闪耀星骑士自动日常脚本的源代码（基于python）

可以实现自动完成日常，自动活动开荒等功能

后续会根据需求实现更多实用功能！

## 需要的python依赖

python版本3.12
除了标准依赖库以外只有一个opencv（版本号4.10.0.84

## 重要功能函数说明

## 1.startapp.py

### ---startapp()

    打开app后进入主页,能够点击更新，跳过签到，关闭公告

### ---dayu()

    大渔~大渔~（不是）
    收粉毛的菜   

## 2.back.py

### ---backhome()

    用于回到主界面
    注：并不能完全保证能回，遇到不能返回的情况时请告诉我

## 3.routine.py

### ---routine_experience()

    日常经验本扫荡

### ---routine_coin()

    日常金币本

### ---routine_task_mail(back_ = 0)

    日常任务和邮箱领取
    输入值back_设置是否返回主页
    0返回，其他数字不返回

### ---routine_staminapurchase(time = 3)

    购买体力
    输入值time为购买次数

### 注：废弃的函数

### ---routine_coin2()

    日常金币本，不好用，已经废弃了

### ---routine_exercice()

    日常合同演习本，不使用

## 4.routine_exercise.py

### ---routine_equipment()

    合同演习装备素材本

### ---routine_skill()

    合同演习技能材料本

### ---routine_breakthrough(Attribute = "thunder")

    合同演习突破材料本
    输入值是你想刷的属性：
    火fire，水water，雷thunder，光light，暗darkness♂

## 5.activity_custom.py

### ---routine_clean_activity_task(team = 0)

    活动图开荒，输入值team用于设置是否组队
    0执行，1不执行

### ---routine_activity_once(team = 0,team_ = 0)

    活动一日一次挑战，输入值team用于是否组队，team_设置自动组队
    team = 0执行，1不执行
    team_ = 0/1/2/3/4/5，分别对应默认，火，水，雷，光，暗

### ---routine_clean_veryhard_activity_task(team_veryhard = 0)

    活动图高难开荒，输入值team用于设置是否组队
    0执行，1不执行

### ---routine_sweepdown_activity_task(team = 0,which = 1)

    活动图扫荡，输入值team用于是否组队

## 6.activity_lose.py

### ---routine_activity_once_lose()

    一日一回高难失败以后重新进入关卡
    （仅限一日一回）
    画个饼，开荒的慢慢弄（躺

## 7.task.py

### ---routine_clean_task(team = 0)

    会把主线任务里所有没打过的关卡都打过

## 注：(5,6,7)

activity_custom.py，activity_lose.py和task.py

使用的target文件夹为target_custom

引用的图片识别函数来自image_custom.py

里面的图片可以根据具体情况进行更换

## 8.non_stop_testing.py

### ---nst()

    检测突发情况：升级，弹窗礼包，网络连接异常
    单独线程运行，目前只做了个弹窗礼包关闭（

#### 其余代码为框架代码，正在整理中
