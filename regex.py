import re

phone_number = re.compile("\d\d\d-\d\d\d-\d\d\d\d")

mo = phone_number.search("zxc123-456-7895")
print(mo.group())