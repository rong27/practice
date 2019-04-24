# For remaking Winfred case
import os
import shutil

# 要從atlas copy 檔名過來
atlas_Winfred_video_path = 'Z:\\Smart VCA Benchmark\VIVOTEK\Outdoor Test_6.0.46\\'
run_2dtrackerapp_remake_path = 'D:\\joyvideo\\TrainingFolder\\autoremake\\'

FD9187HTsettings = 'D:\\joyvideo\\TrainingFolder\\2dtrackerappsettings\\pre_sale_camera_setting_Winfred\\FD9187-HT(192.168.4.165)_ori\\'
FD9365HTVsettings = 'D:\\joyvideo\\TrainingFolder\\2dtrackerappsettings\\pre_sale_camera_setting_Winfred\\FD9365-HTV(192.168.4.172)_ori\\'
IB9365EHTsettings = 'D:\\joyvideo\\TrainingFolder\\2dtrackerappsettings\\pre_sale_camera_setting_Winfred\\IB9365-EHT(192.168.4.152)_ori\\'
IB9365HTsettings = 'D:\\joyvideo\\TrainingFolder\\2dtrackerappsettings\\pre_sale_camera_setting_Winfred\\IB9365-HT(192.168.4.171)_ori\\'
IB9391EHTsettings = 'D:\\joyvideo\\TrainingFolder\\2dtrackerappsettings\\pre_sale_camera_setting_Winfred\\IB9391-EHT(192.168.4.167)_ori\\'
SD9374EHLXsettings = 'D:\\joyvideo\\TrainingFolder\\2dtrackerappsettings\\pre_sale_camera_setting_Winfred\\SD9374-EHLX(192.168.4.170)_ori\\'
   
os.chdir('D:\\joyvideo\\TrainingFolder\\autoremake')

# """
# 建立資料夾
# """
# for test_dir_name in os.listdir(atlas_Winfred_video_path):
#     """
#     如果指定目錄不存在就建立目錄
#     """
#     if not os.path.isdir(test_dir_name):
#         if "FD9365-HTV" in test_dir_name:
#             # print(test_dir_name)
#             os.mkdir(test_dir_name)
#             print("Folders Done : " + test_dir_name)


# """
# 非法字元用 _ 取代
# """

# os.chdir(run_2dtrackerapp_remake_path)
# for remake_dir in os.listdir(run_2dtrackerapp_remake_path):
#     # print(remake_dir)
#     replace_brackets = remake_dir.replace(" (", "_") # 把(取代成_
#     os.rename(remake_dir, replace_brackets) 

#     replace_space = replace_brackets.replace(" ", "_")  # 把 取代成_
#     os.rename(remake_dir, replace_space)

#     replace_right_brackets = remake_dir.replace(")", "") # 把)刪掉
#     os.rename(remake_dir, replace_right_brackets)     
    
#     replace_comma = remake_dir.replace(",", "") # 把,刪掉
#     os.rename(remake_dir, replace_comma)   

# 依照型號放設定檔
# for dirname in os.listdir(remake_path):
#     if "FD9187" in dirname:
#         # print(dirname)
#         if "video" not in os.listdir(remake_path+dirname):
#             # print(dirname)
#             os.chdir(remake_path+dirname)
#             os.mkdir("video")
#         for i in os.listdir(FD9187settings):
#             print(i)
#             shutil.copy2(FD9187settings+ i, dirname)

# for dirname65 in os.listdir(remake_path):
#     if "IB9365" in dirname65:
#         print(dirname65)
#         if "video" not in os.listdir(remake_path+dirname65):
#             print(dirname65)
#             os.chdir(remake_path+dirname65)
#             os.mkdir("video")
#         for i in os.listdir(IB9365settings):
#             print(i)
#             shutil.copy2(IB9365settings+ i, dirname65)

# 依照型號放設定檔
for dirname in os.listdir(run_2dtrackerapp_remake_path):
    if "FD9365-HTV" in dirname:
        print(dirname)
        if "video" not in os.listdir(run_2dtrackerapp_remake_path+dirname):
            print(dirname)
            os.chdir(run_2dtrackerapp_remake_path+dirname)
            os.mkdir("video")
        for i in os.listdir(FD9365HTVsettings):
            # print(i)
            shutil.copy2(FD9365HTVsettings+ i, dirname)