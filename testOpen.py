import os

def rename_files():
    file_list = os.listdir(r"/Users/xiangnan/Downloads/prank")
    print(file_list)
    os.chdir(r"/Users/xiangnan/Downloads/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "1234567890"))
    
rename_files()
