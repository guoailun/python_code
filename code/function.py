# 参数的定义
# 1、关键字参数


def num(a, b, c):
    print("a = %s" % (a))
    print("b = %s" % (b))
    print("c = %s" % (c))

# num(1, 2, 3)
# num(1, c=3, b=2)

# 可变长参数 第一个参数是必填参数，后面的是可选参数


def howlong1(first, *other):
    print(1 + len(other))

# howlong1(1,[1,2,3])


def howlong2(*other):
    print(len(other))

# howlong2()


# 函数的作用域
var1 = 123


def fun():
    # var1 = 456
    global var1
    var1 = 456
    # print(var1)


fun()
# print(var1)


def outer():
    num = 10

    def inner():
        # nonlocal num   # nonlocal关键字声明
        global num   # nonlocal关键字声明
        num = 100
        # print('inner %d' %num)
    inner()


    # print('outer %d' %num)
outer()

# print('global %d' %num)


# 对待器对象 迭代器方法 iter() next()
list = [1, 2, 3]
it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # except

# 迭代器
# 来创建一个可以使用float步长的range()函数


def float_range(start, end, step):
    x = start
    while x < end:
        yield x
        x += step

# y = float_range(10, 20, 0.5)
# t = iter(y)
# print(next(t))
# print(next(t))

# for index in float_range(10, 20, 0.5):
#     print(index)


# lambda表达式
def add(x, y):
    return x + y


print(add(3, 5))

# add 函数转化成 lambda表达式如下
# lambda x,y: return x + y


def var(x, y): return x + y


print(var(6, 34))


def one(item):
    return item[1]


list_one = [1, 2, 3]
# print(one(list_one))
dic_one = {'a': 'aa', 'b': 'bb'}

# for item in dic_one.items():
#     print(item)

# for item in dic_one.values():
#     print(item)

# for item in dic_one.keys():
#     print(item)

# 函数的闭包
# 1、非闭包的加和函数


def sum_count():
    a = 1
    b = 2
    return a + b

# 闭包思想实现加和函数


def sum_count2(a):
    def add(b):
        return a + b
    return add


num1 = sum_count()
num2 = sum_count2(1)

# print(type(num1))
# print(type(num2))

# print(num2(3))


# 用闭包思想实现累加器
def counter(NUM=0):
    arr = [NUM]
    def add_1():
        arr[0] += 1
        return arr[0]
    return add_1

num3 = counter(5)
num4 = counter(18)


print(num3())
print(num3())
print(num3())

print(num4())
print(num4())
print(num4())


