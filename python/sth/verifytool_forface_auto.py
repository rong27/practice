import subprocess
import os
import time
# os.chdir('D:\\joyvideo\\Face_verify\\autoFaceVerify')
checkfolders = os.listdir('D:\\joyvideo\\Face_verify\\autoFaceVerify')


for i in checkfolders:

    now_path = os.path.join('D:\\joyvideo\\Face_verify\\autoFaceVerify',i)
    print(now_path)
    os.chdir(now_path)
    UseFaceVerifytool = subprocess.call('D:\\joyvideo\\Face_verify\\verifyTool0116_ForFace\\Release\\Start.bat')

