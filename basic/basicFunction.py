# 函数
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
#Python 定义函数使用 def 关键字，一般格式如下：
#def 函数名（参数列表）:
#    函数体

def hello() :
   print("Hello World!")

hello()

# 更复杂点的应用，函数中带上参数变量:
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

# python 传不可变对象实例
def ChangeInt(a):
    a = 10
# 调用函数
b = 2
ChangeInt(b)
print(b)  # 结果是 2

# 传可变对象实例
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

# 不定长参数
# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)


# lambda 函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


# return语句

# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print("函数内 : ", total)
   return total;

# 调用sum函数
total = sum( 10, 20 );
print("函数外 : ", total)