# learn-python python 标准库
python.org => documentation => 3.+ => Library Reference

# learn-python python 基本的，需要掌握的库
文本处理服务，数据类型（日期类型）、通用操作系统服务 等

# learn-python python 日常应用比较广泛的模块
1、文字处理的 re
2、日期类型的time、datetime
3、数字和数学类型的math、random
4、文件盒目录访问的pathlib、os.path
5、数据压缩和归档的tarfile
6、通用操作系统os、logging、argparse
7、多线程的 threading、queue
8、Internet数据处理的 base64、json、urllib
9、结构化标记处理工具的 html、xml
10、开发工具unitest
11、调试工具的timeit
12、软件包发布的venv
13、运行服务的_main_

# 正则表达式元字符
. 匹配任意的单个字符
^ 以什么开头
$ 以什么结尾 ,从后向前匹配
* 匹配前边的字符出现0次到多次
+ 匹配前边的字符出现1次到多次
? 匹配前边的字符出现0次或1次
{m} 表示前边的字符出现指定的次数
{m,n} 表示前边的字符出现m次到n次
[] 中括号里边的任意一个字符匹配成功，就可以匹配成功 cab cbb ccb cdb c[bcd]
| 

转义的符号
\d 匹配的内容是一串数字  == [0-9]+ == [0123456789]+
\D 匹配的内容不包含数字
\s 匹配的内容是字符串

() 分组 （2018)-(03)-(04)  r'(\d+)-(\d+)-(\d+)'  group(1) 取出哪一组 groups()

2018-03-01
2018-04-04
(03|04)

^$ 表示这一行是空行
.*? 不使用贪婪模式

match()  完全匹配
search() 可以不完全匹配，包含相应的字符串就可以
sub() 进行字符串的替换 三个参数（匹配规则，替换成什么内容，你要替换的字符串）
findall() 进行匹配多次

# datetime time

# 数学类的库 math

# 产生随机数的库 random

# 文件与目录操作库 os.path
