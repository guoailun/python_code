# learn-python python 映射的类型：字典
1、字典：字典包含哈希值和指向的对象
    {"哈希值": "对象"}  =>  {'length': 180, 'width': 80}

2、字典键的特性
    1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住；
    2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行；

3、推导式 （列表推导式和字典推导式）

4、dict() 构造函数可以直接从 key-value 对中创建字典:

>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}

5、如果关键字都是简单的字符串，有时通过关键字参数指定 key-value 对更为方便:

>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}