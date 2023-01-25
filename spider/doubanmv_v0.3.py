#!/bin/python3
# -*- coding:utf-8 -*-

###invoke threading

import requests, re, os
import time, sys
import threading

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def get_contents(i=0):
    url = "https://movie.douban.com/top250?start=%d&filter=" %(i)
    response = requests.get(url, headers = headers)
    contents = response.text
    return contents

def save_picture(url, f_name):
    response = requests.get(url, headers = headers)
    contents = response.content
    f_name.write(contents)

def process_sigle(x, y):
    for i in res_list[x:y]:
        f_name = os.path.join("douban", i[1]+".jpg")
        with open(f_name, "wb") as f:
            save_picture(i[0], f)


if (__name__ == "__main__"):

    time1 = time.time()

    print("parent process start...")
    res_list = []
    count = re.findall(r'[\S\s]*?<span class="count">\(共(\d+)条\)</span>', get_contents())
    count = int(count[0])

    for i in range(0, count, 25):
        contents = get_contents(i)
        results = re.findall(r'\s<li>\s+<div class="item">[\s\S]+?<img width="100".+?src="(.+?)"[\S\s]+?<span class="title">(.+?)</span>', contents)
        for i in results:
            res_list.append(i)
    
    if (not os.path.exists("douban")):
        os.mkdir("douban")
    else:
        pass

    t1 = threading.Thread(target = process_sigle, args = (0, count//2))
    t2 = threading.Thread(target = process_sigle, args = (count//2, count))
    t1.start()
    t2.start()
    print("thread start...")
    t1.join()
    t2.join()
    print("parent process done")

    time2 = time.time()
    print("Run time is %0.2f" %(time2 - time1))
    sys.exit(0)


