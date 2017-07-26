# Python3 模块

# Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

import sys
import module.support
from module import stringUtils   # 这是引入某个包中的某个模块，这样写的优点在于不必写冗长的包名

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')

print(module.support.say_hello_func("Python Module"))
print(stringUtils.upper("coral"))