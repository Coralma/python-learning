from urllib import request

response = request.urlopen("http://car.autohome.com.cn/config/series/314.html")  # 打开网站
fi = open("314.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()