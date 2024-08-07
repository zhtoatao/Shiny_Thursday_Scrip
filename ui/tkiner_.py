import tkinter as tk
from tkinter import ttk
import threading
import os
import pickle
import subprocess
from . import main_
from core import log_creater,image,image_custom,image_non_stop
from tkinter import messagebox



def on_button2_click():
    print("这玩意是标题")

#输入栏灰字
def on_entry_focusin_1(event):
    if entry_1.get() == "fire/water/thunder/light/darkness":
        entry_1.delete(0, tk.END)
        entry_1.config(fg='black')

def on_entry_focusout_1(event):
    if entry_1.get() == "":
        entry_1.insert(0, "fire/water/thunder/light/darkness")
        entry_1.config(fg='gray')


def on_entry_focusin_2(event):
    if entry_3.get() == "0/1/2/3/4/5,详见说明书":
        entry_3.delete(0, tk.END)
        entry_3.config(fg='black')

def on_entry_focusout_2(event):
    if entry_3.get() == "":
        entry_3.insert(0, "0/1/2/3/4/5,详见说明书")
        entry_3.config(fg='gray')





#pickle数据读取
DATA_FILE = 'user_data.pkl'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return {
        'adb路径': '',
        'adb端口': '',
        '打开app进入主页': '',
        '大渔~': '',
        '回到主页': '',
        '日常经验+硬币本': '',
        '合同演习': '',
        '突破本属性': '',
        '体力购买': '',
        '购买次数': '',
        '活动一日一回': '',
        '活动一日一回自动组队':'',
        '自动组队依据': '',
        '活动图扫荡': '',
        '活动图开荒': '',
        '活动图开荒自动组队': '',
        '活动高难开荒': '',
        '活动高难开荒自动组队': '',
        '主线图开荒': '',
        '主线图开荒自动组队': '',
        '回主页领取任务通行证，邮箱': '',
    }

def save_data():
    data = {
        'adb路径': input_text_4.get(),
        'adb端口': input_text_5.get(),
        '打开app进入主页': var_sa.get(),
        '大渔~': var_dy.get(),
        '回到主页': var_bh.get(),
        '日常经验+硬币本': var_rt.get(),
        '合同演习': var_rex.get(),
        '突破本属性': var_rea.get(),
        '体力购买': var_rsp.get(),
        '购买次数': var_spt.get(),
        '活动一日一回': var_rao.get(),
        '活动一日一回自动组队':var_rao_1.get(),
        '自动组队依据': raot_.get(),
        '活动图扫荡': var_rsat.get(),
        '活动图开荒': var_rct.get(),
        '活动图开荒自动组队': var_rct_1.get(),
        '活动高难开荒': var_rcvat.get(),
        '活动高难开荒自动组队': var_rcvat_1.get(),
        '主线图开荒': var_rctk.get(),
        '主线图开荒自动组队': var_rctk_1.get(),
        '回主页领取任务通行证，邮箱': var_rtm.get()
    }
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)

def on_closing():
    save_data()
    root.destroy()

# 加载上次保存的数据
data = load_data()








# 创建主窗口
root = tk.Tk()
root.title("Shiny_Thursday_Scrip")
root.configure(bg="#404040")  # 设置窗口背景颜色为白色

# 创建按钮

button2 = ttk.Button(root, text="  ---闪耀星期四自动日常脚本！---  ", command=on_button2_click, style="Button.TButton")
button2.pack(pady=15)


#############################################################################################################################
# 创建复选框变量

var_dy = tk.IntVar()
var_bh = tk.IntVar()
var_rt = tk.IntVar()
var_rex = tk.IntVar()
var_spt = tk.IntVar()
var_rsp = tk.IntVar()
var_rao = tk.IntVar()
var_rsat = tk.IntVar()
var_rct = tk.IntVar()
var_rcvat = tk.IntVar()
var_rctk = tk.IntVar()
var_rtm = tk.IntVar()

var_rea = tk.IntVar()

var_rao_1 = tk.IntVar()
var_raot_ = tk.IntVar()
var_rao_2 = tk.IntVar()
var_rct_1 = tk.IntVar()
var_rcvat_1 = tk.IntVar()
var_rctk_1 = tk.IntVar()


checkbox_options = {
    "anchor": tk.W,
    "wraplength": 10000,
    "fg": "#E0E0E0",
    "bg": "#404040",
    "selectcolor": "#404040", 
    "activebackground": "#404040",  
    "activeforeground": "#E0E0E0"  ,
    "font": ("Times New Roman", 12)
}

checkbox_options_sub = {
    "anchor": tk.W,
    "wraplength": 9000,
    "fg": "#E0E0E0",
    "bg": "#404040",
    "selectcolor": "#404040", 
    "activebackground": "#404040",  
    "activeforeground": "#E0E0E0"  ,
    "font": ("Times New Roman", 10)
}

input_text = "none"

frame_left = tk.Frame(root, bg='#404040')
frame_left.pack(side=tk.LEFT, padx=10)

frame_right = tk.Frame(root, bg='#404040')
frame_right.pack(side=tk.LEFT, padx=10)

# 创建复选框
var_sa = tk.IntVar()
checkbox_1 = tk.Checkbutton(frame_left, text="打开app进入主页", variable=var_sa, **checkbox_options)
var_sa.set(data['打开app进入主页'])
checkbox_1.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_2 = tk.Checkbutton(frame_left, text="大渔~", variable=var_dy, **checkbox_options)
var_dy.set(data['大渔~'])
checkbox_2.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_3 = tk.Checkbutton(frame_left, text="回到主页", variable=var_bh, **checkbox_options)
var_bh.set(data['回到主页'])
checkbox_3.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_4 = tk.Checkbutton(frame_left, text="日常经验+硬币本", variable=var_rt, **checkbox_options)
var_rt.set(data['日常经验+硬币本'])
checkbox_4.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_5 = tk.Checkbutton(frame_left, text="合同演习", variable=var_rex, **checkbox_options)
var_rex.set(data['合同演习'])
checkbox_5.pack(pady=10, anchor=tk.W, padx=(50, 0))

var_rea = tk.StringVar()

frame = tk.Frame(frame_left)
frame.pack(pady=8)

label = tk.Label(frame, text="突破本属性:")
label.pack(side=tk.LEFT, padx=10)

entry_1 = tk.Entry(frame, textvariable=var_rea)
entry_1.insert(0, "fire/water/thunder/light/darkness")
entry_1.config(fg='gray')
entry_1.pack(side=tk.LEFT, padx=10)
var_rea.set(data['突破本属性'])


entry_1.bind("<FocusIn>", on_entry_focusin_1)
entry_1.bind("<FocusOut>", on_entry_focusout_1)

checkbox_6 = tk.Checkbutton(frame_left, text="体力购买", variable=var_rsp, **checkbox_options)
var_rsp.set(data['体力购买'])
checkbox_6.pack(pady=10, anchor=tk.W, padx=(50, 0))

frame = tk.Frame(frame_left)
frame.pack(pady=8)

label = tk.Label(frame, text="购买次数:")
label.pack(side=tk.LEFT, padx=10)

var_spt = tk.StringVar(value="3")
entry_2 = tk.Entry(frame, textvariable=var_spt)
entry_2.config(fg='gray')
entry_2.pack(side=tk.LEFT, padx=10)
var_spt.set(data['购买次数'])

checkbox_7 = tk.Checkbutton(frame_left, text="活动一日一回", variable=var_rao, **checkbox_options)
var_rao.set(data['活动一日一回'])
checkbox_7.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_7_1 = tk.Checkbutton(frame_left, text="自动组队", variable=var_rao_1, **checkbox_options_sub)
var_rao_1.set(data['活动一日一回自动组队'])
checkbox_7_1.pack(pady=7, anchor=tk.W, padx=(65, 0))

raot_ = tk.StringVar()

frame = tk.Frame(frame_left)
frame.pack(pady=8)

label = tk.Label(frame, text="自动组队依据:")
label.pack(side=tk.LEFT, padx=5)

entry_3 = tk.Entry(frame, textvariable=raot_)
entry_3.insert(0, "0/1/2/3/4/5,详见说明书")
entry_3.config(fg='gray')
entry_3.pack(side=tk.LEFT, padx=5)
raot_.set(data['自动组队依据'])


entry_3.bind("<FocusIn>", on_entry_focusin_2)
entry_3.bind("<FocusOut>", on_entry_focusout_2)

checkbox_8 = tk.Checkbutton(frame_right, text="活动图扫荡", variable=var_rsat, **checkbox_options)
var_rsat.set(data['活动图扫荡'])
checkbox_8.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_9 = tk.Checkbutton(frame_right, text="活动图开荒", variable=var_rct, **checkbox_options)
var_rct.set(data['活动图开荒'])
checkbox_9.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_9_1 = tk.Checkbutton(frame_right, text="自动组队", variable=var_rct_1, **checkbox_options_sub)
var_rct_1.set(data['活动图开荒自动组队'])
checkbox_9_1.pack(pady=7, anchor=tk.W, padx=(65, 0))

checkbox_10 = tk.Checkbutton(frame_right, text="活动高难开荒", variable=var_rcvat, **checkbox_options)
var_rcvat.set(data['活动高难开荒'])
checkbox_10.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_10_1 = tk.Checkbutton(frame_right, text="自动组队", variable=var_rcvat_1, **checkbox_options_sub)
var_rcvat_1.set(data['活动高难开荒自动组队'])
checkbox_10_1.pack(pady=15, anchor=tk.W, padx=(50, 0))

checkbox_11 = tk.Checkbutton(frame_right, text="主线图开荒", variable=var_rctk, **checkbox_options)
var_rctk.set(data['主线图开荒'])
checkbox_11.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_11_1 = tk.Checkbutton(frame_right, text="自动组队", variable=var_rctk_1, **checkbox_options_sub)
var_rctk_1.set(data['主线图开荒自动组队'])
checkbox_11_1.pack(pady=7, anchor=tk.W, padx=(65, 0))

checkbox_12 = tk.Checkbutton(frame_right, text="回主页领取任务\n通行证，邮箱", variable=var_rtm, **checkbox_options_sub)
var_rtm.set(data['回主页领取任务通行证，邮箱'])
checkbox_12.pack(pady=10, anchor=tk.W, padx=(50, 0))

checkbox_13 = tk.Checkbutton(frame_right, text="好想吃光天\n不穿鞋子的脚啊",  **checkbox_options_sub)
checkbox_13.pack(pady=(50,35), anchor=tk.W, padx=(50, 0))
    
#############################################################################################################################

frame_right_right = tk.Frame(root, bg='#404040')
frame_right_right.pack(side=tk.TOP, padx=10)

sub_frame_1 = tk.Frame(frame_right_right)
sub_frame_1.pack(side=tk.TOP, padx=10, pady=20)

label_1 = tk.Label(sub_frame_1, text="adb路径:")
label_1.pack(side=tk.LEFT, padx=0)

input_text_4 = tk.StringVar()
input_text_4.set(data['adb路径'])
entry_2_1 = tk.Entry(sub_frame_1, textvariable=input_text_4)
entry_2_1.config(fg='gray')
entry_2_1.pack(side=tk.LEFT, padx=10)

sub_frame_2 = tk.Frame(frame_right_right)
sub_frame_2.pack(side=tk.TOP, padx=10, pady=5)

label_2 = tk.Label(sub_frame_2, text="adb端口:")
label_2.pack(side=tk.LEFT, padx=0)

input_text_5 = tk.StringVar()
input_text_5.set(data['adb端口'])
entry_2_2 = tk.Entry(sub_frame_2, textvariable=input_text_5)
entry_2_2.config(fg='gray')
entry_2_2.pack(side=tk.LEFT, padx=10)



# 绑定窗口关闭事件
#root.protocol("WM_DELETE_WINDOW", on_closing)


#############################################################################################################################


def get_adb():
    return input_text_4.get(),input_text_5.get()

def run_adb(adb_path, adb_port):
    try:
        subprocess.run([adb_path, "connect", "127.0.0.1:" + adb_port], check=True)
        log_message = log_creater.write_log(f"adb路径: {adb_path} \nadb端口: {adb_port}")
        print(log_message)
    except subprocess.CalledProcessError as e:
        log_message = log_creater.write_log(f"adb连接失败: {e}")
        print(log_message)



ad = False
ad_lock = threading.Lock()

def change_startapp():
    adb_path_,adb_port_ = get_adb()
    
    run_adb(adb_path_, adb_port_)

    image.adb_path = adb_path_
    image.adb_port = adb_port_
    image_custom.adb_path = adb_path_
    image_custom.adb_port = adb_port_
    image_non_stop.adb_path = adb_path_
    image_non_stop.adb_port = adb_port_


    #1.打开app进入主页
    sa = var_sa.get()

    #2.大渔~
    dy = var_dy.get()

    #3.回到主页
    bh = var_bh.get()

    #4.日常经验+硬币本
    rt = var_rt.get()

    #5.合同演习
    rex = var_rex.get()
    #5.1突破本属性
    rea = var_rea.get()
    if rex == 1:
        if rea not in ["fire", "water", "thunder", "light", "darkness"]:
            messagebox.showwarning("突破本属性异常", "请填写fire, water, thunder, light, darkness\n五个中的一个")
            return

    #6.体力购买
    rsp = var_rsp.get()
    #6.1体力购买次数
    spt = int(var_spt.get())

    #7.活动一日一回
    rao = var_rao.get()
    #7.1是否组队
    raot = var_rao_1.get()
    #7.2组队依据
    raot_ = var_raot_.get()
    if rao == 1:
        if raot not in ["0", "1", "2", "3", "4","5"]:
            messagebox.showwarning("活动一日一回组队依据异常", "请填写0/1/2/3/4/5\n六个中的一个")
            return

    #8.活动图扫荡
    rsat = var_rsat.get()

    #9.活动图开荒
    rct = var_rct.get()
    #9.1是否组队
    rctt = var_rct_1.get()

    #10.活动高难开荒
    rcvat = var_rcvat.get()
    #10.1是否组队
    rcvatt = var_rcvat.get()

    #11.主线图开荒
    rctk = var_rctk.get()
    #11.1是否组队
    rctkt = var_rctk_1.get()

    #12.回主页领取任务，通行证，邮箱
    rtm = var_rtm.get()

    ad = False
    ad_lock = threading.Lock()

    t1 = threading.Thread(target=lambda:main_.allclick(sa, dy, bh, rt, rex, rea, rsp, spt, rao, raot, raot_, rsat, rct, rctt, rcvat, rcvatt, rctk, rctkt, rtm))
    t2 = threading.Thread(target=main_.nst)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    #main_.thread_(sa, dy, bh, rt, rex, rea, rsp, spt, rao, raot, raot_, rsat, rct, rctt, rcvat, rcvatt, rctk, rctkt, rtm)

run_button = ttk.Button(frame_right_right, text="运行", command=change_startapp)
run_button.pack(side=tk.TOP, pady=(150, 20), padx=20)

run_button = ttk.Button(frame_right_right, text="保存设置", command=save_data)
run_button.pack(side=tk.TOP, pady=(150, 20), padx=20)

style = ttk.Style()
style.configure("Button.TButton", 
                borderwidth=0, 
                relief="flat", 
                background="darkblue", 
                foreground="black", 
                font=("Helvetica", 15))
style.map("Button.TButton", background=[("active", "lightblue")])

root.mainloop()
