# 测试写入文件
# 打开一个文件
f = open("foo.txt", "w")
f.write("Python is a good language. \nFreaking awesome\n" )
# 关闭打开的文件
f.close()


# 测试读取文件
f = open("foo.txt", "r")
str = f.read()
print(str)
# 关闭打开的文件
f.close()


# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# 基本写入接口：pickle.dump(obj, file, [,protocol])
# 基本读取接口：x = pickle.load(file)

import pprint, pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

#读取
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()






