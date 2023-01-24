#!/bin/python3
# -*- coding:utf-8 -*-

import requests, re, os
import time, sys

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

if (__name__ == '__main__'):
    t1= time.time()
    res_list = []
    print("parent process start...")
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
    
    #multiprocess
    pid_0 = os.fork()
    
    if (pid_0 == 0):
        process_sigle(0, count//2)
        os._exit(0)
    else:
        process_sigle(count//2, count)
    
    t2 = time.time()
    print("run time is %d" %(t2-t1))
    sys.exit(0)

