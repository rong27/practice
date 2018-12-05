import os
import shutil

os.chdir('D:\\joyvideo\\TrainingFolder\\autoremake')
os.getcwd()

name = ['170150', '171238', '171344', '171718', '171737', '172221', '173535', '173936', '175145']

# make dirs and copy files in new one:

for i in name :
    # print(i)
    foldername = 'FD9365_Delta_173_20181031_' + i
    # print(foldername)
    shutil.copytree('FD9365_Delta_173_origin', foldername)

# for n in range(586, 597):
#     # print(n)
#     foldername = 'Kavalan_13_' + str(n)
#     print(foldername)
#     # os.makedirs(foldername)
#     shutil.copytree('Kavalan_ori', foldername)

# for n in range(669, 675):
#     # print(n)
#     foldername = 'Kavalan_13_' + str(n)
#     print(foldername)
#     # os.makedirs(foldername)
#     shutil.copytree('Kavalan_ori', foldername)    

# for n in range(739, 746):
#     # print(n)
#     foldername = 'Kavalan_13_' + str(n)
#     print(foldername)
#     # os.makedirs(foldername)
#     shutil.copytree('Kavalan_ori', foldername)    