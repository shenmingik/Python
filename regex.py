# import re

# phone_number = re.compile("\d\d\d-\d\d\d-\d\d\d\d")

# mo = phone_number.search("zxc123-456-7895")
# print(mo.group()) #print 123-456-7895

import re
phone_number_regax = re.compile("(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_number_regax.search("zxc123-456-7895")
print(mo.group(0))
print(mo.group(1))  # print 123
print(mo.group(2))  # print 456-7895