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