import subprocess
import os
import time
os.chdir('E:\\To_Ting\\FD9365_night')   # assign path which you are interested
checkfolders = os.listdir(os.getcwd())
# print(len(checkfolders))
# print(checkfolders)

for i in checkfolders:
    now_path = 'E:\\To_Ting\\FD9365_night\\' +i
    print(now_path)
    os.makedirs('E:\\To_Ting\\FD9365_night_image_'+str(i))
    raw = ' -image'
    image = 'E:\\To_Ting\\FD9365_night_image_'+str(i)

    command = 'D:\\work\\tools\\vivocapture\\vivocapture_build\\x86\\app\\Debug\\vivocapture.exe {0} {1} {2}'.format(raw, now_path, image )
    subprocess.call(command.split(), shell=False)
    # i +=1

