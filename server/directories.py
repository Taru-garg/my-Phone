import getpass
import platform

'''
By default Linux
'''

main_dir = "/home/"+str(getpass.getuser())+"/"
photos_dir = main_dir+"Pictures"
document_dir = main_dir+"Documents"
music_dir = main_dir + "Music"
video_dir = main_dir + "Videos"


'''
platfrom.system()
    1. Windows
    2. Linux
    3. Android - Linux

if name == 'Windows'
    directory(windows)
'''



'''
Actually there are no windows phone that will be able to run this app
thus this feature is only for the purpose of development and can be done later

if platform.system()=="Windows":
    main_dir = "/home/"+str(getpass.getuser())+"/"
    photos_dir = main_dir+"Pictures"
    document_dir = main_dir+"Documents"
    music_dir = main_dir + "Music"
    video_dir = main_dir + "Videos"
'''