# import re

# phone_number = re.compile("\d\d\d-\d\d\d-\d\d\d\d")

# mo = phone_number.search("zxc123-456-7895")
# print(mo.group()) #print 123-456-7895

# import re
# phone_number_regax = re.compile("(\d\d\d)-(\d\d\d-\d\d\d\d)")
# mo = phone_number_regax.search("zxc123-456-7895")
# print(mo.group(0))  # print 123-456-7895
# print(mo.group(1))  # print 123
# print(mo.group(2))  # print 456-7895

import re
grep_regax = re.compile("A|B")  # 匹配A 或 B
mo = grep_regax.search("A123456")
print(mo.group())   # 打印出A
mo1 = grep_regax.search("B123456")
print(mo1.group()) # 打印出B