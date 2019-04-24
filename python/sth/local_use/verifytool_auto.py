import subprocess
import os
import time
os.chdir('D:\\joyvideo\\autoverify')
checkfolders = os.listdir('D:\\joyvideo\\autoverify')
# print(len(checkfolders))
# print(checkfolders)

for i in checkfolders:

    now_path = os.path.join('D:\\joyvideo\\autoverify',i)
    print(now_path)
    os.chdir(now_path)
    Useverifytool = subprocess.call('D:\\joyvideo\\verifyTool2019_04_23\\Release\\Start.bat')

