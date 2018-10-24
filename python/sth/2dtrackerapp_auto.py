import subprocess
import os
import time
os.chdir('D:\\joyvideo\\TrainingFolder\\autoremake')
checkfolders = os.listdir('D:\\joyvideo\\TrainingFolder\\autoremake')
# print(len(checkfolders))

for i in range(len(checkfolders)):

    now_path = os.path.join('D:\\joyvideo\\TrainingFolder\\autoremake\\',checkfolders[i])
    # print(now_path)
    os.chdir(now_path)
    open2dtrackerapp = subprocess.call('D:\\work\\projects\\trackerproc\\trackerproc_build\\x86\\app\\Release\\2dtrackerapp.exe')

    i +=1



