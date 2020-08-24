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





def list_files(dir_name):
    files_list = []
    '''
    folder_list = []
    '''
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            files_list.append(full_path)
        '''
        elif not os.path.isfile(item):
            folder_list.append(item)
        '''
    '''    
    if len(folder_list) not 0:
        for i in range(0,len(folder_list)):
            files_list.append(list_files(folder_list[i]))
    '''
    return files_list

'''
[1, 2, 3, 1,2,3 ]
/home/taru/Pictures/x/1
'''

def list_files_name(dir_name):
    files_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            files_list.append(item)
    return files_list



def list_files_name_shortened(dir_name):
    files_list = []
    for item in os.listdir(dir_name):
        full_path = os.path.join(dir_name,item)
        if os.path.isfile(full_path):
            name,_ = item.split('-')
            files_list.append(name)
    return files_list