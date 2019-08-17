# learn-python python 模块的导入

1、 import [模块名] 例如：import time
可以调用模块内的方法：time.sleep()

2、import t as time #对导入的模块重命名
t.sleep()

3、from time import sleep #导入 time 某块的 sleep 函数
使用时直接调用 sleep() # 这种导入方式我们不推荐，容易与模块当前文件中的函数造成重名，产生覆盖的问题

# learn-python python 自定义模块

文件名.py 新建文件，写入一些方法，在其他文件中 import 文件名，就可以调用自己封装的方法了
