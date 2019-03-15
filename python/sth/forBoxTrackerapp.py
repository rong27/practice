import subprocess
import os
import time
os.chdir('E:\\Terry\\auto3dtracker')
checkfolders = os.listdir('E:\\Terry\\auto3dtracker')
# print(len(checkfolders))
# print(checkfolders)

for i in checkfolders:

    now_path = os.path.join('E:\\Terry\\auto3dtracker',i)
    print(now_path)
    os.chdir(now_path)
    open2dtrackerapp = subprocess.call('E:\\Terry\\box\\Special-app\\3dtrackerapp.exe')

