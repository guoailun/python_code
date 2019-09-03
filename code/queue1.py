# 多线程来实现经典问题：生产者，消费者模式
# 生产者，消费者

from threading import Thread, current_thread
import time
import random
from queue import Queue

# 面向对象的编程模式
queue = Queue(5)  # 定义队列的长度
# 生产者类
class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()  # 线程的名字
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)  # 随机产生一个数字
            queue.put(num)  # 网队列放数据
            print('生产者 %s 生产了数据 %s' %(name, num))
            t = random.randint(1, 3)  # 随机产生一个数字
            time.sleep(t)
            print('生产者 %s 睡眠了 %s秒' % (name, t))



# 消费者类
class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()  # 线程的名字
        global queue
        while True:
            num = queue.get()  # 去一个数据
            queue.task_done()  # 封装好了线程等待和线程同步的方法
            print('消费者 %s 消费了数据 %s' %(name, num))
            t = random.randint(1, 5)  # 随机产生一个数字
            time.sleep(t)
            print('消费者 %s 睡眠了 %s秒' % (name, t))

# 生产者少于消费者, c1, c2轮流获取数据

p1 = ProducerThread(name = 'p1')
p1.start()

c1 = ConsumerThread(name = 'c1')
c1.start()

c2 = ConsumerThread(name = 'c2')
c2.start()




# p1 = ProducerThread(name = 'p1')
# p1.start()

# p2 = ProducerThread(name = 'p2')
# p2.start()

# c1 = ConsumerThread(name = 'c1')
# c1.start()

