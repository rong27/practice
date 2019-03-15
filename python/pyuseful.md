## subprocess 

#### reference
* [subprocess子進程管理](http://www.reader.idv.tw/2014/09/subprocess.html)

## print and return difference 
* print: gives the value to the user as an output string. print(3) would give a string '3' to the screen for the user to view. The program would lose the value.

* return: gives the value to the program. Callers of the function then have the actual data and data type (bool, int, etc...) return 3 would have the value 3 put in place of where the function was called.

#### shutil copy and copytree

* copytree : 複製整個資料夾文件, 若目的地有相同名稱的檔案, 則會報error
* copy : 複製整個資料夾文件, 若目的地有相同名稱的檔案, 則會取代目的地的檔案
