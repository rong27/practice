import os
import numpy as np  
import shutil

# cnn_small_negative_image_name = os.listdir('C:\\Users\\joy.lin\\Desktop\\SC129-Face2\\cnn-small\\Angle0_HeadTop\\negative')
# print(len(cnn_small_negative_image_name))

# cnn_negative_image_name = os.listdir('C:\\Users\\joy.lin\\Desktop\\SC129-Face2\\cnn\\Angle0_HeadTop\\negative')
# print(len(cnn_negative_image_name))

# for smallimage in cnn_small_negative_image_name:
#     for image in cnn_negative_image_name:
#         if smallimage == image:
#             print(image)
#             shutil.copy('C:\\Users\\joy.lin\\Desktop\\SC129-Face2\\cnn\\Angle0_HeadTop\\negative\\'+image,'C:\\Users\\joy.lin\\Desktop\\NBcase\\20181128\\HeadTop\\positive')


# cnn_small_positive_image_name = os.listdir('C:\\Users\\joy.lin\\Desktop\\SC129-Face2\\cnn-small\\Angle0_HeadTop\\positive')
# print(len(cnn_small_positive_image_name))

# cnn_positive_image_name = os.listdir('C:\\Users\\joy.lin\\Desktop\\SC129-Face2\\cnn\\Angle0_HeadTop\\positive')
# print(len(cnn_positive_image_name))

# for postive_smallimage in cnn_small_positive_image_name:
#     for postive_image in cnn_positive_image_name:
#         if postive_smallimage == postive_image:
#             print(postive_image)
#             shutil.copy('C:\\Users\\joy.lin\\Desktop\\SC129-Face2\\cnn\\Angle0_HeadTop\\positive\\'+postive_image,'C:\\Users\\joy.lin\\Desktop\\NBcase\\20181128\\HeadTop\\negative')

# compare short image of samll imgae and big image(Terry) , if the same copy big image to another folders

def compare_positive_short_image(small_path, big_path, move_folder):
    cnn_small_positive_image_name = os.listdir(small_path)
    cnn_positive_image_name = os.listdir(big_path)
    for postive_smallimage in cnn_small_positive_image_name:
        for postive_image in cnn_positive_image_name:
            if postive_smallimage == postive_image:
                shutil.copy(big_path+ postive_image, move_folder)

