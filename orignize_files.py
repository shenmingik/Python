# 拷贝文件和文件夹
##################################################################
# import shutil
# import os

# current_path = os.getcwd()
# # 拷贝test.txt 文件到temp1文件夹下
# shutil.copy(current_path+"/test.txt",current_path+"/Python/temp1")
# # 将temp1文件夹内容拷贝到temp2文件夹下,此时会创建temp2文件
# shutil.copytree(current_path+"/Python/temp1",current_path+"/Python/temp2")

# 移动文件和文件夹
##################################################################
# import shutil
# import os

# current_path = os.getcwd()
# # 将temp2文件夹内的文件拷贝到temp中,并将temp2改名为temp
# shutil.move(current_path+"/Python/temp2",current_path+"/temp")

# 删除文件和文件夹
##################################################################
# import shutil
# import os

# current_path = os.getcwd()
# shutil.rmtree(current_path+"/temp")

# 删除文件和文件夹
##################################################################
# import shutil
# import os

# current_path = os.getcwd()
# for folder_name,sub_folders,file_names in os.walk(current_path):
#     print(folder_name+":")
#     # 加载当前文件路径下的所有子文件
#     for sub_folder in sub_folders:
#         print("\t"+folder_name+": "+sub_folder+"(dir)")
#     for file_name in file_names:
#         print("\t"+folder_name+": "+file_name)

# 创建压缩文件
##################################################################
# import zipfile
# import os

# current_path = os.getcwd()
# new_zip = zipfile.ZipFile("newZip","w")
# new_zip.write("test.txt",compress_type=zipfile.ZIP_DEFLATED)
# new_zip.write("test.cpp",compress_type=zipfile.ZIP_DEFLATED)

# 读取压缩文件
##################################################################
# import zipfile
# import os

# current_path = os.getcwd()
# new_zip = zipfile.ZipFile("newZip","r")
# files = new_zip.namelist()

# for file in files:
#     info = new_zip.getinfo(file)
#     print("filename: "+file)
#     print("\tsize: "+str(info.file_size))
#     print("\tcompress_size: "+str(info.compress_size))

# 解压缩压缩文件
##################################################################
import zipfile
import os

current_path = os.getcwd()
example_zip = zipfile.ZipFile("newZip","r")
# 解压
example_zip.extractall()
example_zip.close()