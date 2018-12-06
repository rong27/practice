import os 
import numpy as np


os.chdir('C:\\Kavalan_2dtrackerapp')
checkfolders = os.listdir('C:\\Kavalan_2dtrackerapp')
# print(np.array(checkfolders))



for i in range(len(checkfolders)):
    os.chdir('C:\\Kavalan_2dtrackerapp\\'+checkfolders[i]+'\\cnn\\')
    # print(os.getcwd())
    modelname = os.listdir()
    if 'HumanShort' in modelname:
        os.chdir('C:\\Kavalan_2dtrackerapp\\'+checkfolders[i]+'\\cnn\\HumanShort')
        print(os.getcwd())
    else:
        print('No HumanShort model in ' +checkfolders[i])

    if 'HumanShortFg' in modelname:
        os.chdir('C:\\Kavalan_2dtrackerapp\\'+checkfolders[i]+'\\cnn\\HumanShortFg')
        print(os.getcwd())       
    else:
        print('No HumanShortFg model in ' +checkfolders[i])
        
    if 'MultiScaleHumanShort' in modelname:
        os.chdir('C:\\Kavalan_2dtrackerapp\\'+checkfolders[i]+'\\cnn\\MultiScaleHumanShort')
        print(os.getcwd())
    else:
        print('MultiScaleHumanShort model in ' +checkfolders[i])

    if 'MultiScaleHumanShortFg' in modelname:
        os.chdir('C:\\Kavalan_2dtrackerapp\\'+checkfolders[i]+'\\cnn\\MultiScaleHumanShortFg')
        nowpath = os.getcwd()
        print(nowpath)
    else:
        print('MultiScaleHumanShortFg model in ' +checkfolders[i])


