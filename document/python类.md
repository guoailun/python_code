# learn-python python class

1、定义一个类 名字一般大写
2、类的继承
3、多态（子类定义跟父类重名的方法，覆盖父类的方法，表现出来的多种形态）
4、类需要实例化之后才能访问

# learn-python python class 补充

1、type 方法 可以获得对象是属于哪个类的
type("123")

2、isinstance() 判断类之间的继承关系 , 返回值为 True 何 False

# learn-python python 异常和类的结合



【严重质疑这一讲的super()讲法】【严重质疑这一讲的super()讲法】【严重质疑这一讲的super()讲法】！！！！

使用方法完全没有讲明白，关键的 super().__init__() 后面一个括号里面的内容由于设计的问题，完全乱了！！！！

后面一个括号传入的是参数值，放到父类去赋值，是有顺序要求的！！！有顺序要求的！！！

super().__init__(name) 不是视频里老师带过没有讲明白的意思，如果按照视频里面的表达，代表的意思是“将name初始化”。错的！！！！正确的解读应该是“把输入的name值（按照排列的顺序）传入到父类去进行初始化”！！！

比如
class Monster():
    def __init__(self, name, hp=10011):
        self.name = name
        self.hp = hp

class Boss(Monster):
    '定义boss的内容，Monster的子类'
    def __init__(self, name, level, hp=101):
        super().__init__(hp)
        self.level = level

boss_10 = Boss(name='boss_10', level='99级', hp=900)
代表的意思是：把900（不是默认值）当作第一个参数值传入父类，而父类第一个属性是name，所以这个子类的实例的name就是900了。

比如：
class Boss(Monster):
    '定义boss的内容，Monster的子类'
    def __init__(self, name, level, hp=101):
        super().__init__(name,hp)

那么name还是name的值，hp还是hp的值。

但是，如果是：
class Boss(Monster):
    '定义boss的内容，Monster的子类'
    def __init__(self, name, level, hp=101):
        super().__init__(hp, name)
那么，name就是hp位置的值，hp就是name位置的值