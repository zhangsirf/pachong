# -*- coding: utf-8 -*-
"""
@Author  :Mart
@Time    :2021/9/15 15:27
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
import os
import json
import re

import requests

root_path = os.path.abspath(os.path.dirname(__file__))
json_path = os.path.join(root_path, 'xhsjson')
# 创建目录文件夹
# os.makedirs('./image/', exist_ok=True)
json_path_pic = os.path.join(root_path, 'image')
def read_files(path):
    """
    :param path:
    :return:
    """
    print(path)
    data = []
    files = os.listdir(path)  # 得到文件夹下所有文件的名称
    for file in files:
        print(file)
        filepath = path + '/' + file
        if os.path.isfile(filepath):  # 如果是文件就打开，需要注意os.path.isfile需要传入绝对地址
            with open(filepath, 'r', encoding='UTF-8') as js_file:

                js = json.load(js_file)
                print(js["data"]["items"][0]["note_card"]["title"])
                tittle = js["data"]["items"][0]["note_card"]["title"]
                print(js["data"]["items"][0]["note_card"]["desc"])
                # print(js["data"]["items"][0]["note_card"]["image_list"])
                i = 0
                os.makedirs('./image/'+str(tittle)+'/', exist_ok=True)
                for pic in js["data"]["items"][0]["note_card"]["image_list"]:
                    # 构造请求头
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
                    }
                    print(pic['url'])
                    # 发送get请求图片url
                    r = requests.get(
                        pic['url'],
                        headers=headers)
                    # wb 以二进制打开文件并写入，文件名不存在会创建
                    with open('./image/'+str(tittle)+'/' + str(i) +'.png', 'wb') as f:
                        f.write(r.content)  # 写入二进制内容
                        i += 1


print(read_files(json_path))

