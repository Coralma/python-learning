import random

# 使用if语句
flag = random.choice(range(100)) % 2
print(flag)
if flag == 1:
    print("1 - if 结果为True")
elif flag == 0:
    print("2 - if 结果为True")
else:
    print("3 - if 结果为false")

# while 循环
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

# while 循环使用 else 语句
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")


# for 语句
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


# range()函数
for i in range(5):
    print(i)

for i in range(5,9):
    print(i)

# range三位时表示增量关系，如下所示0-10之间的数据增量为3，则结果值为3,6,9
for i in range(0, 10, 3) :
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

sequence = [12, 34, 34, 23, 45, 76, 89]
for index, item in enumerate(sequence):
    print(index, item)