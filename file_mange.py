# 获取与改变当前路径
##################################################################
# import os
# # 获取当前路径
# print(os.getcwd())
# # 改变当前路径
# os.chdir("/home/ubuntu")
# print(os.getcwd())

# 创建文件夹
##################################################################
# import os
# # 获取当前路径
# current_path = os.getcwd()
# # 在当前路径下创建file_manage 和中间文件夹files
# os.makedirs(current_path+"/files/file_manage")

# 处理绝对路径和相对路径
##################################################################
# import os

# current_path = os.getcwd()
# if os.path.isabs(current_path) == True:
#     print(current_path+" is a absolute path")

# # 如果传入.表示当前路径
# if os.path.isabs(".") == True:
#     print(". is not a absolute path")

# print("current path is: "+os.path.abspath("."))
# print("current path: "+os.path.abspath(".")+" to root dir \"home\" ways is "+os.path.relpath(".","/home"))

# 获取文件名
##################################################################
# import os

# current_name = os.getcwd()+"/Python/file_manage.py"
# print("dir is "+os.path.dirname(current_name))
# print("file is "+os.path.basename(current_name))

# 获取文件大小和文件夹内容
import os

current_name = os.getcwd()
print(current_name+" size: "+str(os.path.getsize(current_name)))
# 获取当前路径下所有文件(夹)的大小
for file in os.listdir(current_name):
    # 非文件夹
    if os.path.isdir(current_name+"/"+file) == False:
        print( file +" size: ",str(os.path.getsize(current_name+"/"+file)))
    # 文件夹
    else:
        print("(dir) "+file+" size: "+str(os.path.getsize(current_name+"/"+file)))