import os
import socket

def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(1)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def list_files(dir_name,depth=1):
    files_list = []
    folder_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            files_list.append(full_path)
        elif os.path.isdir(full_path) and depth<=2:
            folder_list.append(full_path)
    if len(folder_list) > 0 and depth<=2:
        internal_list = []
        for i in range(0,len(folder_list)):
            internal_list = list_files(folder_list[i],depth+1)
            for i in range(0,len(internal_list)):
                files_list.append(internal_list[i])
    return files_list

def list_files_name(dir_name,depth=1):
    files_list = []
    folder_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            files_list.append(item)
        elif os.path.isdir(full_path) and depth<=2:
            folder_list.append(full_path)
    if len(folder_list) > 0 and depth<=2:
        print(depth)
        internal_list = []
        for i in range(0,len(folder_list)):
            internal_list = list_files_name(folder_list[i],depth+1)
            for i in range(0,len(internal_list)):
                files_list.append(internal_list[i])
    return files_list



def list_files_name_shortened(dir_name,depth=1):
    files_list = []
    folder_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            _ = item.split('-')
            files_list.append(_[0])
        elif os.path.isdir(full_path) and depth<=2:
            folder_list.append(full_path)
    if len(folder_list) > 0 and depth<=2:
        internal_list = []
        for i in range(0,len(folder_list)):
            internal_list = list_files_name(folder_list[i])
            for i in range(0,len(internal_list)):
                _ = internal_list[i].split('-')
                files_list.append(_[0])
    return files_list