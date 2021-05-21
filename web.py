# 启动新浏览器
##################################################################
# import webbrowser
# webbrowser.open("https://so.csdn.net/so/search?q=进程&t=blog&u=shenmingxueIT")

# 获取命令行参数
##################################################################
# import sys
# import webbrowser
# # 如果有输出参数
# if len(sys.argv) > 1:
#     content = "".join(sys.argv[1])
# webbrowser.open("https://so.csdn.net/so/search?q="+content+"&t=blog&u=shenmingxueIT")

# 下载网页
##################################################################
# import requests
# # 该网址包含整部罗密欧
# res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
# if res.status_code == requests.codes.ok:
#     print(len(res.text))
#     # 打印出小说的前几个字符
#     print(res.text[0:250])

# 检查错误
##################################################################
import requests
# 一个错误的url
res = requests.get("http://inventwithpython.com/123456")
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" %(exc))