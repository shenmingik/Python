# import re

# phone_number = re.compile("\d\d\d-\d\d\d-\d\d\d\d")

# mo = phone_number.search("zxc123-456-7895")
# if mo != None:
#     print(mo.group()) #print 123-456-7895
# else:
#     print("Don't have phone number")

# import re
# phone_number_regax = re.compile("(\d\d\d)-(\d\d\d-\d\d\d\d)")
# mo = phone_number_regax.search("zxc123-456-7895")
# if mo != None:
#     print(mo.group(0))  # print 123-456-7895
#     print(mo.group(1))  # print 123
#     print(mo.group(2))  # print 456-7895
# else:
#     print("Don't have phone number")

# import re

# phone_number_regax = re.compile("(\d\d\d)-(\d\d\d-\d\d\d\d)")

# mo = phone_number_regax.search("zxc123-456-7895")
# if mo != None:
#     print(mo.groups())
# else:
#     print("Don't have phone number")

# 管道匹配多个分组
##################################################################

# import re
# grep_regax = re.compile("A|B")  # 匹配A 或 B

# mo = grep_regax.search("A123456")
# if mo != None:
#     print(mo.group())   # 打印出A

# mo1 = grep_regax.search("B123456")
# if mo != None:
#     print(mo1.group()) # 打印出B

# import re
# bat_regax = re.compile("Bat(man|mobile|compter|bat)")
# mo = bat_regax.search("Batmobile lost a wheel")
# if mo != None:
#     print(mo.group()) # Batmobile
#     print(mo.group(1)) # mobile

# 用问号实现可选匹配
##################################################################
# import re
# bat_regax = re.compile("Bat(wo)?man")

# mo1 = bat_regax.search("The Adventures of Batman")
# if mo1 != None:
#     print(mo1.group())  #Batman

# mo2 = bat_regax.search("The Adventures of Batwoman")
# if mo2 != None:
#     print(mo2.group())  #Batwoman

# 用*匹配零次或多次
##################################################################
# import re

# bat_regax = re.compile("Bat(wo)*man")

# mo1 = bat_regax.search("The Advantures of Batman")
# if mo1 != None:
#     print(mo1.group())  # Batman

# mo2 = bat_regax.search("The Advantures of Batwoman")
# if mo2 != None:
#     print(mo2.group())  # Batwoman

# mo3 = bat_regax.search("The Advantures of Batwowowoman")
# if mo3 != None:
#     print(mo3.group())  # Batwowowoman

# 用+匹配一次或多次
##################################################################
# import re

# bat_regax = re.compile("Bat(wo)+man")

# mo1 = bat_regax.search("The Advantures of Batman")
# if mo1 != None:
#     print(mo1.group()) 

# mo2 = bat_regax.search("The Advantures of Batwoman")
# if mo2 != None:
#     print(mo2.group())  # Batwoman

# mo3 = bat_regax.search("The Advantures of Batwowowoman")
# if mo3 != None:
#     print(mo3.group())  # Batwowowoman

# 用{}匹配特定次数
##################################################################
# import re

# bat_regax = re.compile("Bat(wo){1}man")

# mo1 = bat_regax.search("The Advantures of Batman")
# if mo1 != None:
#     print(mo1.group()) 

# mo2 = bat_regax.search("The Advantures of Batwoman")
# if mo2 != None:
#     print(mo2.group())  # Batwoman

# mo3 = bat_regax.search("The Advantures of Batwowowoman")
# if mo3 != None:
#     print(mo3.group())  

# 贪心匹配和非贪心匹配
##################################################################
# import re

# greedyha_regax = re.compile("(ha){3,5}")
# mo1 = greedyha_regax.search("hahahahaha")   # 贪心
# if mo1 != None:
#     print(mo1.group()) # hahahahaha

# nongreedyha_regax = re.compile("(ha){3,5}?") # 非贪心
# mo2 = nongreedyha_regax.search("hahahahaha")
# if mo2 != None:
#     print(mo2.group())  # hahaha

# findall 方法
##################################################################
# import re
# phone_regax = re.compile("\d{3}-\d{3}-\d{4}")

# mo1 = phone_regax.search("Cell:123-465-7895 Work:987-654-3210")
# if mo1!=None:
#     print(mo1.group()) # 123-465-7895

# mo2 = phone_regax.findall("Cell:123-465-7895 Work:987-654-3210")
# if mo2!=None:
#     for phone in mo2:
#         print(phone)    # 123-465-7895; 987-654-3210

# 自定义字符分类
##################################################################
# import re
# vowel_regax = re.compile("[a-d]")

# mo = vowel_regax.search("ghjwaio")
# if mo != None:
#     print(mo.group())   # a