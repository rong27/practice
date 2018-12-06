import os
import shutil
import numpy as np
import re

def DeleteFiles(path, DirList, filelist):
    dirfile = []
    dirfile = os.listdir(path)
    for sth in dirfile:
        if sth not in DirList:
            filepath = os.path.join(path, sth)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath, True)
                
            elif sth not in filelist:
                filepath = os.path.join(path, sth)
                if not os.path.isdir(filepath):
                    os.remove(sth)


## delete us shop dirs and files except cnn and shrotmodel of dirs

# for folders in os.listdir('C:\\US_shop_app_us13'):
#     # print(folders)
#     os.chdir('C:\\US_shop_app_us13\\'+folders)
#     path = os.getcwd()
#     # print(path)
#     dirslist = ['cnn']
#     filelist = []
#     DeleteFiles(path, dirslist, filelist)
#     os.chdir('C:\\US_shop_app_us13\\'+folders+'\\cnn')
#     cnnpath = os.getcwd()
#     # print(cnnpath)
#     cnnmodellist = ['HumanShort', 'HumanShortFg', 'MultiScaleHumanShort', 'MultiScaleHumanShortFg']
#     DeleteFiles(cnnpath, cnnmodellist, filelist)

## delete dirs which cnn dir is empty

# for folders in os.listdir('C:\\US_shop_app_us13'):
#     os.chdir('C:\\US_shop_app_us13\\'+ folders +'\\cnn')
#     if os.listdir(os.getcwd()) == []:
#         print(folders)
#         os.chdir('C:\\US_shop_app_us13')
#         shutil.rmtree('C:\\US_shop_app_us13\\'+ folders)