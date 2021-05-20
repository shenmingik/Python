# 获取与改变当前路径
##################################################################
import os
# 获取当前路径
print(os.getcwd())
# 改变当前路径
os.chdir("/home/ubuntu")
print(os.getcwd())