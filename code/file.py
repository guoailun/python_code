# 将小说的人物记录在文件中
# file1 = open('name.text', 'w')
# file1.write('诸葛亮')
# file1.close()

# # 读取文件
# file1 = open('name.text')
# # 查看文件内容有没有被读到
# print(file1.read())
# file1.read()
# file1.close()


# 文件继续写入
# file3 = open('name.text', 'a')
# file3.write('刘备')
# file3.close()

# 读取文件  读取第一行
# file4 = open('name.text')
# print(file4.readline())

# 读取文件  读取多行，逐行处理
# file5 = open('name.text')
# for one in file5.readlines():
#     print(one)
#     print('=========')


# 读取文件的指针问题
file6 = open('sanguo_name.text')
# print(file6.tell())  # 获取读取当前文件的指针
file6.read(1)   # 读取一个字符
# print(file6.tell())
    # 若此时的需求，要求读完文件后，恢复文件指针的位置
file6.seek(0)
print(file6.tell())  # 获取读取当前文件的指针
file6.read(1)   # 读取一个字符
print(file6.tell())
 

# file7 = open('sanguo_wuqi.text', 'w')
# file7.write('刀')
# file7.close()

# file7 = open('sanguo_quan.text', 'w')
# file7.write('三国演义')
# file7.close()


