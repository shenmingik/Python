# 拷贝文件和文件夹
##################################################################
import shutil
import os

current_path = os.getcwd()
# 拷贝test.txt 文件到temp1文件夹下
shutil.copy(current_path+"/test.txt",current_path+"/Python/temp1")
# 将temp1文件夹内容拷贝到temp2文件夹下,此时会创建temp2文件
shutil.copytree(current_path+"/Python/temp1",current_path+"/Python/temp2")
