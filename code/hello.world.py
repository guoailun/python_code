# 这是我的第一个Python程序

import time # 我导入了一个时间模块

print(time.time())  # 在屏幕上打印毫秒

if 10-9 > 0:
    # 这行需要缩进，缩进需要4个空格
    print("10大于9")

squares = [1, 4, 9, 16, 25]

squares2 = squares[:]

squares = squares + [3, 6]

# print(squares2[:])
# print(squares)
# for i in range(4):
#     print(i)

words = ['cat', 'window', 'defenestrate']
for w in words:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        w = 'aaa'

print(words)


for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
       words.insert(0, w)

print(words)

# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
str1 = 'hello'
# 集合里的元素不能重复
print(set(str1))