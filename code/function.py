# 参数的定义
# 1、关键字参数
def num(a, b, c):
    print("a = %s" %(a))
    print("b = %s" %(b))
    print("c = %s" %(c))

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
    print(var1)

fun()
print(var1)


