# 异常
# NameError: name 'j' is not defined
# i = j


# IndexError: string index out of range
# a = "123"
# print(a[3])


# KeyError: 'c'
# d = { 'a': 1, 'b': 2}
# print(d['c'])

# ZeroDivisionError: division by zero
# print(1/0)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(2 + '2')

# AttributeError: 'int' object has no attribute 'append'
# a = 123
# a.append()

# 语法错误
# SyntaxError: invalid syntax
# print())

# 捕获异常
try:
    print(1/0)
except ZeroDivisionError:
    print("0 不能做除数")

# 捕获异常 所有异常
try:
    print(1/0)
except Exception as e:
    print("%s" %e)


# 自定义错误类型 使用 raise 语句抛出一个指定的异常

try:
    raise NameError('helloError')
except NameError:
    print("自定义error")


# finally
try:
    a = open("name.text")
except Exception as e:
    print(e)
finally:  # 不管是不是有异常，都走finally
    a.close();