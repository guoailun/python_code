arr1 = ['小燕子', '紫薇', '皇帝']
arr2 = ['漱芳斋', '大明湖畔', '紫禁城']
arr3 = ['杂技、杂耍', '琴棋书画', '玉玺']

arrList = [arr1, arr2, arr3]

arr_num = [[1, 2, 3], [4, [5, 6]], [7]]

# print(arrList)
# print(arr_num)

# 看一个单词中是否包含元音字母
word = 'asdfaeuwq'
volews = ['a', 'e', 'i', 'o', 'u']
# 一个对象在另一个对象当中用 in
for letter in word:
    if letter in volews:
        print(letter)

num = [1, 2, 3, 4]
# print(num)
num.remove(3)
# print(num)

# num.remove(3) // 找不到要删除的值，报错
# print(num)

numzw = [1, 2, 4]
print(numzw.pop())
print(numzw)
print(numzw.pop(0))
print(numzw)
print(numzw[0])
