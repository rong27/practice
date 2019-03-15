# In order to collect IRmode data
import subprocess
import os
import time
os.chdir('E:\\vivocapture_video\\Thurmal\\20190110')   # assign path which you are interested
checkfolders = os.listdir(os.getcwd())
# print(len(checkfolders))
# print(checkfolders)

for i in checkfolders:
    now_path = 'E:\\vivocapture_video\\Thurmal\\20190110\\' +i
    print(now_path)
    os.makedirs('E:\\vivocapture_video\\Thurmal\\20190110label\\'+str(i))
    parameter = ' -image'
    save_image_path = 'E:\\vivocapture_video\\Thurmal\\20190110label\\'+str(i)
    command = 'D:\\work\\tools\\vivocapture\\vivocapture_build\\x86\\app\\Debug\\vivocapture.exe {0} {1} {2}'.format(parameter, now_path, save_image_path )
    subprocess.call(command.split(), shell=False)

