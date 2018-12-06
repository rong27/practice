# delete unuseful files

import os
import shutil
import numpy as np
import re

# def DeleteFiles(path, DirList, filelist):
#     dirfile = []
#     dirfile = os.listdir(path)
#     for sth in dirfile:
#         if sth not in DirList:
#             filepath = os.path.join(path, sth)
#             if os.path.isdir(filepath):
#                 shutil.rmtree(filepath, True)
                
#             elif sth not in filelist:
#                 filepath = os.path.join(path, sth)
#                 if not os.path.isdir(filepath):
#                     os.remove(sth)

# for i in os.listdir('C:\\new_shortdata'):
#     os.chdir('C:\\new_shortdata\\'+ i)
#     path = os.getcwd()
#     print(path)
#     dirslist = ['video']
#     settings = ['config.yml', 'config_camerainfo.json', 'config_vca_ae.json', 'config_vca_alarm.json',
#                 'config_vca_capability.xml', 'config_vca_di.json', 'config_vca_features.json',
#                 'config_vca_re.json', 'intrinsics.yml', 'parameter.yml', 'tracker_config.xml']
#     DeleteFiles(path, dirslist, settings)




# for i in os.listdir('C:\\Kavalan_2dtrackerapp'):
#     os.chdir('C:\\Kavalan_2dtrackerapp\\'+ i)
#     path = os.getcwd()
#     dirslist = ['cnn']
#     filelist = []
#     DeleteFiles(path, dirslist, filelist)

# for i in os.listdir('C:\\Kavalan_2dtrackerapp'):
#     os.chdir('C:\\Kavalan_2dtrackerapp\\'+ i + '\\cnn')
#     path = os.getcwd()
#     dirslist = ['HumanShort', 'HumanShortFg', 'MultiScaleHumanShort', 'MultiScaleHumanShortFg']
#     filelist = []
#     DeleteFiles(path, dirslist, filelist)

# for i in os.listdir('C:\\KavalanFGPng'):
#     path = 'C:\\KavalanFGPng\\' + i 
#     for model in os.listdir(path):
#         if 'png' in os.listdir('C:\\KavalanFGPng\\' + i +'\\'+ model):
#             shutil.copytree('C:\\KavalanFGPng\\' + i +'\\'+ model +'\\png', 'C:\\KavalanFGPng\\' + i +'\\'+ model +'\\postive\\png' )
#         if 'xml' in os.listdir('C:\\KavalanFGPng\\' + i +'\\'+ model):
#             shutil.copytree('C:\\KavalanFGPng\\' + i +'\\'+ model +'\\xml', 'C:\\KavalanFGPng\\' + i +'\\'+ model +'\\postive\\xml' )
#         modelpath = 'C:\\KavalanFGPng\\' + i + '\\' + model
#         dirslist = ['postive', 'negative']
#         filelist = []
#         DeleteFiles(modelpath, dirslist, filelist)

# move negative fg image
# KavalanFGPngDir = 'C:\\KavalanFGPng\\'
# OriginFgPath = 'C:\\Kavalan_2dtrackerapp\\'
# for i in os.listdir(KavalanFGPngDir):
#     for modelname in ['HumanShortFg', 'MultiScaleHumanShortFg']:
#         if modelname in os.listdir(KavalanFGPngDir + i+ '\\'):
#             os.chdir(KavalanFGPngDir + i+ '\\'+ modelname)
#             # print(os.getcwd())
#             if 'negative' not in os.listdir(os.getcwd()):
#                 os.makedirs(KavalanFGPngDir+ i+ '\\'+ modelname +'\\negative\\png')
#             else:
#                 # print(os.getcwd())
#                 # print(np.array(os.listdir(OriginFgPath+ i + '\\cnn\\' + modelname + '\\negative')))
#                 if 'negative' in os.listdir(OriginFgPath+ i + '\\cnn\\' + modelname +'\\'):
#                     for negpng in os.listdir(OriginFgPath+ i + '\\cnn\\' + modelname + '\\negative'):                    
#                         neg_pngRegex = re.compile(r'fg.png$')
#                         neg_png = neg_pngRegex.findall(negpng)
#                     # print(neg_png)
#                         if neg_png != []:
#                             shutil.move(OriginFgPath+ i + '\\cnn\\' + modelname + '\\negative\\'  + negpng, KavalanFGPngDir+ '\\' + i+ '\\'+ modelname+'\\negative\\png\\' )
                    