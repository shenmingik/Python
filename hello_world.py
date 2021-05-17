# print("hello world") --> hello world

# message="hello world"
# print(message) --> hello worl

# message="hello world"
# print(message.title()) -->Hello World
# print(message.upper()) -->HELLO WORLD
# print(message.lower()) -->hello world

# message = "hello world"
# interger = 1
# print(message)
# print(interger)

# message = "hello world"
# print(message.title())
# print(message.upper())
# print(message.lower())

# message = "hello" + " " + "world"
# print(message)
# print(message.title() + " by Python\n")
# print("\tbut C++ is the best")

# print(2+3)
# print(2*3)
# print(2/3)
# print(2**3)

# message = "hello world"
# interger = 1
# print(message +str(interger))

# bicycles = ["trek","redline","specialized"]
# print(bicycles)
# bicycles[1]="real-redline"
# print(bicycles)
# bicycles.append("phoenix")
# print(bicycles)
# bicycles.insert(1,"osram")
# print(bicycles)

# bicycles = ['trek', 'osram', 'redline', 'specialized', 'phoenix']
# print(bicycles)

# del bicycles[1]
# print(bicycles)

# bicycles.pop()
# print(bicycles)

# bicycles.pop(1)
# print(bicycles)

# bicycles.remove("trek")
# print(bicycles)

# bicycles = ['trek', 'osram', 'redline', 'specialized', 'phoenix']
# for bicycle in bicycles:
#     print(bicycle + " in for")
# print("out of for")
# print(sorted(bicycles))
# print(bicycles)

# 逆序排序
# bicycles.sort(reverse=True)
# print(bicycles)

# # 相当于[1,5)
# for value in range(1,5):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# numbers = list(range(2,6,2))
# print(numbers)

# numbers = list(range(1,6))
# print(numbers)
# print("max: "+str(max(numbers)))
# print("min: "+str(min(numbers)))
# print("sum: "+str(sum(numbers)))

# numbers = list(range(1,6))
# # 打印前三个
# print(numbers[0:3])
# # 打印后三个
# print(numbers[2:6])
# # 从开头开始打印四个
# print(numbers[:4])
# # 从下标2开始打印到末尾
# print(numbers[2:])

# numbers = list(range(1,6))
# # 相当于指针复制，浅拷贝
# numbers_copy = numbers
# # 深拷贝
# numbers_real_copy = numbers[:]
# numbers[0] = 96
# print(numbers_copy)
# print(numbers_real_copy)

# dimensions = (200,50,"hello world")
# print(dimensions[0])
# print(dimensions[1])
# print(dimensions[2])

# # 以下报错
# # dimensions[0] = 100

# dimensions = (200,50,"hello world")
# for dimension in dimensions:
#     if dimension == "hello world":
#         print("hello world is in dimensions")
#     elif dimension == 50:
#         print("50 is in dimensions")
#     elif dimension == 200:
#         print("200 is in dimension")
#     else:
#         print("200、50、hello world are not in dimensions")

dimensions = (200,50,"hello world")
if "hello" not in dimensions:
    print("hello is not in dimensions")
else:
    print("hello in dismensions")
