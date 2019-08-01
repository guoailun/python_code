# learn-python python 错误 在ptyhon中的错误至少有两种
语法错误和异常（ syntax errors 和 exceptions ）

1）语法错误
2）异常

# learn-python python 捕获异常
 try 和 except 
 1、一个 try 语句可能包含多个 except 子句，分别指定处理不同的异常。至多只会有一个分支被执行。
 2、一个 except 子句可以在括号中列出多个异常的名字，例如:
    except (RuntimeError, TypeError, NameError):
        pass

3、try … except 语句可以带有一个 else子句，该子句只能出现在所有 except 子句之后。当 try 语句没有抛出异常时，需要执行一些代码，可以使用这个子句。例如:

    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

# learn-python python 捕获异常 所有异常 Exception
Python 使用 raise 语句抛出一个指定的异常。例如:

>>>raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: HiThere
