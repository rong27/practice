import os 
import re
import shutil
import numpy as np 

# make the same name folders


for foldername in os.listdir('C:\\testUS_shop_shortmodel'):
    os.chdir('C:\\testUS_shop_FG_XML')
    # os.makedirs(foldername)
    cnnmodel = ['HumanShort', 'HumanShortFg', 'MultiScaleHumanShort', 'MultiScaleHumanShortFg']
    for modelname in cnnmodel:
        if modelname in os.listdir('C:\\testUS_shop_shortmodel\\'+foldername+'\\cnn'):
            os.chdir('C:\\testUS_shop_FG_XML\\'+foldername)
            # os.makedirs(modelname)
            logic = ['positive', 'negative']
            for recognize in logic:
                if recognize in os.listdir('C:\\testUS_shop_shortmodel\\'+foldername+'\\cnn\\'+modelname):
                    os.chdir('C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname)
                    # os.makedirs(recognize)
            if 'negative' in os.listdir('C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname):
                os.chdir('C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname+'\\negative')
                # os.makedirs('png')
            if 'positive' in os.listdir('C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname):
                os.chdir('C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname+'\\positive')
                # os.makedirs('png')
                # os.makedirs('xml')

           # move FGpng and xml
            if 'negative' in os.listdir('C:\\testUS_shop_shortmodel\\'+foldername+'\\cnn\\'+modelname):
                fgimage_negative_path ='C:\\testUS_shop_shortmodel\\'+foldername+'\\cnn\\'+modelname+'\\negative'
                for negative_fgimage in os.listdir(fgimage_negative_path):
                    fg_neg_pngRegex = re.compile(r'fg.png$')
                    fg_neg_png = fg_neg_pngRegex.findall(negative_fgimage)
                    if fg_neg_png != []:    
                        shutil.move(fgimage_negative_path+'\\'+negative_fgimage, 'C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname+'\\negative\\png')

            if 'positive' in os.listdir('C:\\testUS_shop_shortmodel\\'+foldername+'\\cnn\\'+modelname):
                fgimage_positive_path ='C:\\testUS_shop_shortmodel\\'+foldername+'\\cnn\\'+modelname+'\\positive'
                for positive_fgimage in os.listdir(fgimage_positive_path):
                    fg_pos_pngRegex = re.compile(r'fg.png$')
                    fg_pos_png = fg_pos_pngRegex.findall(positive_fgimage)
                    xmlRegex = re.compile(r'.xml$')
                    xmlfile = xmlRegex.findall(positive_fgimage)
                    if fg_pos_png != []:
                        shutil.move(fgimage_positive_path+'\\'+positive_fgimage, 'C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname+'\\positive\\png')
                    elif xmlfile != []:
                        # print(fgimage_positive_path+'\\'+positive_fgimage)
                        # print(os.listdir('C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname+'\\positive\\png'))
                        shutil.move(fgimage_positive_path+'\\'+positive_fgimage, 'C:\\testUS_shop_FG_XML\\'+foldername+'\\'+modelname+'\\positive\\xml')







