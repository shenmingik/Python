# 启动新浏览器
##################################################################
# import webbrowser
# webbrowser.open("https://so.csdn.net/so/search?q=进程&t=blog&u=shenmingxueIT")

# 获取命令行参数
##################################################################
import sys
import webbrowser
# 如果有输出参数
if len(sys.argv) > 1:
    content = "".join(sys.argv[1])
webbrowser.open("https://so.csdn.net/so/search?q="+content+"&t=blog&u=shenmingxueIT")

