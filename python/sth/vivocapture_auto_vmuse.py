# In order to collect IRmode data
import subprocess
import os
import time
os.chdir('E:\\To_Ting\\FD9365-HTV-Park1_IRmode')   # assign path which you are interested
checkfolders = os.listdir(os.getcwd())
# print(len(checkfolders))
# print(checkfolders)

for i in checkfolders:
    now_path = 'E:\\To_Ting\\FD9365-HTV-Park1_IRmode\\' +i
    print(now_path)
    os.makedirs('E:\\To_Ting\\FD9365-HTV-Park1_IRmode_label\\'+str(i))
    parameter = ' -image'
    save_image_path = 'E:\\To_Ting\\FD9365-HTV-Park1_IRmode_label\\'+str(i)
    command = 'D:\\work\\tools\\vivocapture\\vivocapture_build\\x86\\app\\Debug\\vivocapture.exe {0} {1} {2}'.format(parameter, now_path, save_image_path )
    subprocess.call(command.split(), shell=False)

