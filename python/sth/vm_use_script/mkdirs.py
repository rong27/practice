import os
import shutil

<<<<<<< Updated upstream
#os.chdir('C:\\Kavalan_2dtrackerapp') for vmuse
=======
os.chdir('C:\\Kavalan_2dtrackerapp')
>>>>>>> Stashed changes
os.getcwd()

# make dirs and copy files in new one:

for n in range(586, 597):
    # print(n)
    foldername = 'Kavalan_13_' + str(n)
    print(foldername)
    # os.makedirs(foldername)
    shutil.copytree('Kavalan_ori', foldername)

for n in range(669, 675):
    # print(n)
    foldername = 'Kavalan_13_' + str(n)
    print(foldername)
    # os.makedirs(foldername)
    shutil.copytree('Kavalan_ori', foldername)    

for n in range(739, 746):
    # print(n)
    foldername = 'Kavalan_13_' + str(n)
    print(foldername)
    # os.makedirs(foldername)
<<<<<<< Updated upstream
    shutil.copytree('Kavalan_ori', foldername)    
>>>>>>> Stashed changes
=======
    shutil.copytree('Kavalan_ori', foldername)    
>>>>>>> Stashed changes
