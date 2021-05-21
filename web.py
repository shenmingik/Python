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
# import requests
# # 一个错误的url
# res = requests.get("http://inventwithpython.com/123456")
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print("There was a problem: %s" %(exc))

# 下载页面到文件
##################################################################
# import requests
# res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
# res.raise_for_status()
# down_file = open("Romo&Juliet.txt","wb")
# # iter_content()方法在循环的每次迭代中，返回一段内容。每一段都是bytes数据类型，我们需要指定一段包含多少字节
# for chunk in res.iter_content(50000):
#     down_file.write(chunk)

# down_file.close()

# 解析HTML
##################################################################
import requests
import bs4
import sys
import pyperclip

if len(sys.argv) > 1:
    i = 2
    content = "".join(sys.argv[1])
    while i < len(sys.argv):
        content = content + " "+"".join(sys.argv[i])
        i = i+1
# 从剪切板获取参数
else:
    content = pyperclip.paste()
url = "https://dict.youdao.com/w/eng/"+content+"/#keyfrom=dict2.index"
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,features="html.parser")

elems = soup.select("div.trans-container > ul")

# 根据有道的编写规则，elems[0]里面存储的就是单词释义的相关信息
words = list(elems[0])
for word in words:
    word = str(word)
    if word.find("<li>") != -1:
        begin = word.find("<li>")
        end = word.find("</li>")
        print(word[begin+4:end])
