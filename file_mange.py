# 获取与改变当前路径
##################################################################
# import os
# # 获取当前路径
# print(os.getcwd())
# # 改变当前路径
# os.chdir("/home/ubuntu")
# print(os.getcwd())

# 获取与改变当前路径
##################################################################
import os
# 获取当前路径
current_path = os.getcwd()
# 在当前路径下创建file_manage 和中间文件夹files
os.makedirs(current_path+"/files/file_manage")