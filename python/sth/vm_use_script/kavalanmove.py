# In order to move Fg image and xml file
# for kavalan folder

import os 
import numpy as np
import re
import shutil

os.chdir('C:\\Kavalan_2dtrackerapp')
checkfolders = os.listdir('C:\\Kavalan_2dtrackerapp')
os.makedirs('KavalanFGPng')

for i in range(len(checkfolders)):
    folder_cnn = 'C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn'
    os.chdir('C:\\Kavalan_2dtrackerapp\\')
    os.makedirs('C:\\KavalanFGPng\\'+ checkfolders[i])
    os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i])

    if 'HumanShort' in os.listdir(folder_cnn):
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i])
        os.makedirs('HumanShort' )
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i]+ '\\HumanShort' )
        os.makedirs('xml')
    if 'HumanShortFg' in os.listdir(folder_cnn):
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i])
        os.makedirs('HumanShortFg' )
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i]+ '\\HumanShortFg' )
        os.makedirs('png')
        os.makedirs('xml')
    if 'MultiScaleHumanShort' in os.listdir(folder_cnn):
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i])
        os.makedirs('MultiScaleHumanShort' )
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i]+ '\\MultiScaleHumanShort' )
        os.makedirs('xml')        
    if 'MultiScaleHumanShortFg' in os.listdir(folder_cnn):
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i])
        os.makedirs('MultiScaleHumanShortFg')
        os.chdir('C:\\KavalanFGPng\\'+ checkfolders[i]+ '\\MultiScaleHumanShortFg' )
        os.makedirs('png')
        os.makedirs('xml')        

    for modelname in ['HumanShort', 'HumanShortFg', 'MultiScaleHumanShort', 'MultiScaleHumanShortFg']: 
        if modelname in os.listdir('C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn'):
            if 'positive' in  os.listdir('C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn\\' +modelname):
                # print(modelname)
                # print(os.listdir('C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn\\' +modelname))
                folder_cnn_positive = 'C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn\\' +modelname+ '\\positive'

                for fgimage_xml in os.listdir(folder_cnn_positive):
            
                    # find and move fg.png / xmlfile           
                    fg_pngRegex = re.compile(r'fg.png$')
                    fg_png = fg_pngRegex.findall(fgimage_xml)
                    xmlRegex = re.compile(r'.xml')
                    xmlfile = xmlRegex.findall(fgimage_xml)   
                    if fg_png != []:
                        shutil.move('C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn\\' +modelname+ '\\positive\\' + fgimage_xml, 'C:\\KavalanFGPng\\'+ checkfolders[i]+ '\\' + modelname + '\\png' )
                    elif xmlfile !=[]:
                        shutil.move('C:\\Kavalan_2dtrackerapp\\'+ checkfolders[i]+'\\cnn\\' +modelname+ '\\positive\\' + fgimage_xml, 'C:\\KavalanFGPng\\'+ checkfolders[i]+ '\\' + modelname + '\\xml' )
                


