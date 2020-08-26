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

depth = 1;

def list_files(dir_name):
    files_list = []
    '''
    folder_list = []
    '''

    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            files_list.append(full_path)
        elif os.path.isdir(full_path):
            for item_in in os.listdir(full_path):
                new_full_path = os.path.join(full_path,item_in)
                if os.path.isfile(new_full_path):
                    files_list.append(new_full_path)

    '''
    if len(folder_list) > 0 and depth <=2:
        depth = depth + 1;
        internal_list = []
        for i in range(0,len(folder_list)):
            internal_list = list_files(folder_list[i])
            print(internal_list)
        for i in range(0,len(internal_list)):
            files_list.append(internal_list[i])
    '''
    return files_list

def list_files_name(dir_name):
    files_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            files_list.append(item)
        elif os.path.isdir(full_path):
            for item_in in os.listdir(full_path):
                new_full_path = os.path.join(full_path,item_in)
                if os.path.isfile(new_full_path):
                    files_list.append(item_in)
    return files_list



def list_files_name_shortened(dir_name):
    files_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            name,_ = item.split('-')
            files_list.append(name)
        elif os.path.isdir(full_path):
            for item_in in os.listdir(full_path):
                new_full_path = os.path.join(full_path,item_in)
                if os.path.isfile(new_full_path):
                    files_list.append(item_in)
    return files_list
