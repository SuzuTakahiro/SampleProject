import sys
import os
import configparser

SETTING_KEY_NAME="SETTINGS"
FOLDER_KEY_NAME="FOLDER"
FILE_KEY_NAME="FILE"
CONF_FILE="conf/setting.ini"

def make_task(parent_dir=None,task_name="task"):
    """
    課題フォルダの作成
    既に課題フォルダが存在する場合は作成しない
    """
    task_path = ""
    conf_path = os.path.join(os.path.dirname(__file__),CONF_FILE)
    config = configparser.ConfigParser()
    config.read(conf_path,'UTF-8')
    if parent_dir is None:
        parent_dir = config[SETTING_KEY_NAME]["parent_directory"]
    
    if os.path.exists(parent_dir) == False:
        return
    task_path = os.path.join(parent_dir,task_name)
    if os.path.exists(task_path):
        return
    os.mkdir(task_path)
    make_subdir(config,task_path)
    

def make_subdir(config,task_dir):
    """
    サブディレクトリの作成
    サブディレクトリに関連したファイルがある場合はそのファイルも作成する
    """
    subdir_list = list(config[FOLDER_KEY_NAME].keys())
    for subdir in subdir_list:
        subdir_path = os.path.join(task_dir,config[FOLDER_KEY_NAME][subdir])
        os.mkdir(subdir_path)
        if subdir in config[FILE_KEY_NAME]:
            file_list = config[FILE_KEY_NAME][subdir].split(",")
            make_files(subdir_path,file_list)


def make_files(parent_dir,file_list):
    """
    サブディレクトリ内のファイル作成
    """
    for file_name in file_list :
        file_path = os.path.join(parent_dir,file_name)
        with open(file_path,"w") as f:
            f.write("####自動生成####")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1 or 2 < len(args):
        print("Argments error")
    elif len(args)==2:
        make_task(task_name=args[1])
    else:
        make_task(parent_dir=args[1],task_name=args[2])
