# 让用户输入狗狗年龄, +int()函数，转换为int型
dog_age = int(input("请输入你家狗狗的年龄: "))

if dog_age < 0: 
    print("狗狗崽子，好小，好que")
elif dog_age == 10: 
    print("狗狗的智商实际已经跟你差不多啦，不要被碾压哦")
elif dog_age > 10:
    human = 22 + (dog_age -2)*5
    print("对应人类年龄: ", human)
else :
    print("啦啦啦")

### 退出提示
input("点击 enter 键退出")