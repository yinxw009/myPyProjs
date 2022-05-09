#!/usr/bin/python3
import requests
import os
 
try:
    def test(i):
        # 1.准备url
        url = "https://cdn3.jiuse.cloud/hls/426142/index%d.ts" % i
 
        # 视频存放位置
        root = "D://video//"
 
        # 抓取文件起的名字
        path = root + "426142_index%d.ts" % i
        print(path)
 
        if not os.path.exists(root):
            # 如果该目录不存在就创建它
            os.mkdir(root)
        if not os.path.exists(path):
            # 获取到目标视频的所有信息
            r = requests.get(url)
            # 打印访问的状态码是否为200
            print(r.status_code)
            # 以二进制写的方式将r的二进制内容写入path
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
 
    # 写一个循环方法，获取所有的视频
    for i in range(49):
        test(i) # 调用爬取视频方法
except:
    print("爬取失败")