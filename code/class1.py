# 面向过程编程：根据程序的执行顺序，从上到下边写我们相应的函数

# user1 = {"name": "tom", "hp": 100}
# user2 = {"name": "jerry", "hp": 100}


# def print_role(role):
#     print("name is %s, ph is %d" % (role['name'], role['hp']))


# print_role(user1)

# 面向对象编程：归类


class Player():  # 定义一个类 名字一般大写
    def __init__(self, name, hp, occu):  # self表示类进行实例化之后，这个实力本身  __init__ 实例化类的时候回执行
        self.role_name = name  # 类的属性  若想要属性只能通过方法做修改，则在属性前加__(两个下滑线，则不能被直接修改)
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 定义一个方法
        print("%s: %d %s" % (self.role_name, self.hp, self.occu))

    def update_name(self, newName):
        self.role_name = newName


# 定义一个怪物类

# 类的继承
class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print("我会跑")

    def whoami(self):
        print('我是怪物父类')


class Animal(Monster):  # 继承怪物类
    '普通怪物类'

    def __init__(self, hp):  # 在子类中重新init会消耗计算机的性能 可以用super
        self.hp = hp


class Boss(Monster):  # 继承怪物类
    'boss怪物物类'

    # def __init__(self, ph=1000):
    #     super().__init__(ph)

    def whoami(self):
        print('我是怪物我怕谁')


# a1 = Monster(200)
# print(a1.hp)
# a1.run()

# a2 = Boss(400)
# print(a2.hp)

# a3 = Monster()
# print(a3.hp)

# a2 = Animal(10)
# print(a2.hp)
# a2.run()

# a3 = Boss()
# print(a3.hp)
# a3.run()
# a3.whoami()

# type() 方法判断属于哪个类
# print("a1的类型是 %s" %(type(a1)))
# print("a2的类型是 %s" %(type(a2)))
# print("a3的类型是 %s" %(type(a3)))

# 判断 one 是不是 some 的子类

# print(isinstance(a1, Monster))
# print(isinstance(a2, Animal))
# print(isinstance(a2, Monster))


# user1 = Player('tom', 100, '战士')  # 类的实例化
# user2 = Player('jerry', 100, '法师')
# user1.print_role()
# user1.update_name('zw')
# user1.print_role()
# user1.role_name = ('123') # 此方法调用后，名字也被修改了
# user1.print_role()


# user2.print_role()


# 尝试些with

# class Testwith():
#     def __enter__(self):
#         print("enter")
#     def __exit__(self, exc_ype, exc_val, exc_tb):
#         if exc_tb is None:
#             print("正常结束")
#         else:
#             print("has error %s" %exc_tb)


# with Testwith():
#     print("开始运行")
#     raise NameError("testNameError") # 通过raisez手动抛出异常


class Dog:
    
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs
