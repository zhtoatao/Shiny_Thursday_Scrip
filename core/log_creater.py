import datetime
import glob
import os

txt_exist  = False 
VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

def write_log(message, log_level="INFO", log_id=None):
    global txt_exist
    if log_level not in VALID_LOG_LEVELS:
        raise ValueError(f"Invalid log level: {log_level}. Valid levels are {VALID_LOG_LEVELS}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if log_id is None:
        try:
            log_id = os.getpid()
        except Exception as e:
            raise RuntimeError(f"Failed to get process ID: {e}")

    log_entry = f"{log_id} {log_level} {timestamp} {message}"

    # 创个文件夹放日志
    log_folder = os.path.join(os.getcwd(), "log")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    #log超过十个就给你删掉一个
    log_files = sorted(glob.glob(os.path.join(log_folder, "*.txt")), key=os.path.getctime)
    if len(log_files) >= 10:
        oldest_log_file = log_files[0]
        os.remove(oldest_log_file)
    
    # 一次main.py创一次txt
    if not txt_exist:
        log_file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.txt")
        log_file_path = os.path.join(log_folder, log_file_name)
        txt_exist = True
    else:
        log_file_path = log_files[-1]        

    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry + "\n")

    return log_entry
