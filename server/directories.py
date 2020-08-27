import getpass


"""
By default Linux
"""

main_dir = "/home/" + str(getpass.getuser()) + "/"
photos_dir = main_dir + "Pictures"
document_dir = main_dir + "Documents"
music_dir = main_dir + "Music"
video_dir = main_dir + "Videos"


"""
os.system()
    1. Windows
    2. Linux
    3. Android

if name == 'Windows'
    directory(windows)
"""
