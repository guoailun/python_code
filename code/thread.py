# 定义一个函数
# def myThread(arg1, arg2):
#     print('%s %s' % (arg1, arg2))


# for i in range(1, 6):
#     myThread(i, i+1)


# 下面用多线程来重新编写以上功能  -- 采用编写一个函数的方法

import threading
import time
from threading import current_thread
# current_thread 可以输出当前线程的一些信息

# def myThread(arg1, arg2):
#     print(current_thread().getName(), 'start')
#     print('%s %s' % (arg1, arg2))
#     time.sleep(1)
#     print(current_thread().getName(), 'end')

# for i in range(1, 6):
#     t1 = threading.Thread(target=myThread, args=(1, i+1))
#     t1.start()

# print(current_thread().getName(), '主线程结束')

# 下面我们在用面向对象的方式实现多线程 -- 采用面向对象的方式

class MyThread(threading.Thread):
    def run(self):  # 重写run方法
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'end')

t1 = MyThread()
t1.start()
t1.join()

print(current_thread().getName(), '主线程结束')




# 以上俩种实现的多线程的方式，主线程先于子线程结束

# 加join方法 
