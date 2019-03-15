import os
import shutil

os.chdir('C:\\tracker_auto_vm')

# make dirs and copy files in new one:

# videopath = 'C:\\IRdata\\Taina_video'
# print(len(os.listdir(videopath)))

# for number in range(len(os.listdir(videopath))):
#     foldername = 'IR_mode_' + str(number)
#     print(foldername)
#     shutil.copytree('C:\\IRdata\\FD9365-HTV_Tainan_Park1', foldername)

for i in os.listdir('C:\\tracker_auto_vm'):
    print('C:\\tracker_auto_vm\\' +i)
    shutil.copy('C:\\tracker2d_reconfig.yml', 'C:\\tracker_auto_vm\\' +i)

