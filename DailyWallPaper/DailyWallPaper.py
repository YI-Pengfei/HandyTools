# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:28:51 2021

@author: YI
"""

import random
import ctypes
import time
import os
import shutil
import requests
import json
import sys
import path
from PIL import Image 
from bs4 import BeautifulSoup
import tkinter
import tkinter.filedialog

# ## 指定一个文件夹，定时更换壁纸
# path = r"C:\Users\杨超越"
# while True:
#     file = os.listdir(path);  # 打开存储图片文件夹中的图片目录
#     filepath = path +"\\" + random.choice(file);  # 随机选取某张图片，建立绝对地址
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)  # 设置桌面壁纸
#     time.sleep(30 * 60);  # 睡眠半个小时

class GetImage():
    def __init__(self,source='wallhaven'):
        self.source = source
    def chooseSource(self, source):
        self.source = source
    def getImage(self, downloadFolder):
        """ 从网站上爬取壁纸，并下载
        downloadFolder: 下载路径
        source: 壁纸源网站
        """
        if not os.path.exists(downloadFolder):
            os.makedirs(downloadFolder)        
        if self.source=='wallhaven':
            url = 'https://alpha.wallhaven.cc/wallpaper/' 
            response = requests.get(url) 
            print(response.text)
            soup = BeautifulSoup(response.text,'html.parser')
            imgs = soup.find_all('img')
            length = len(imgs)
            if length > 0:
                match = random.choice(imgs)
                rawUrl = match.get('src')
                rawId = rawUrl.split('/')[-1]
                rawUrl = 'https://w.wallhaven.cc/full/' + rawId[0:2] + '/wallhaven-' + rawId
                raw = requests.get(rawUrl) 
                imgFile = os.path.join(downloadFolder, rawId)
                with open(imgFile,'wb') as f:
                    f.write(raw.content)
            print(imgFile)
            return imgFile
        
        elif self.source=='Bing':
            searchURL = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
            response = requests.get(searchURL)
            data = json.loads(response.text)
    
            resultId = data['images'][0]['hsh']
            resultURL = 'https://cn.bing.com' + data['images'][0]['url']
            resultURL = resultURL.replace("1920x1080","1920x1200") ## 替换为更高分辨率
            print(u'正在为您下载图片:%s...' % resultId)
            if(not os.path.exists(downloadFolder)):
                os.makedirs(downloadFolder)
            
            jpgFile = resultId + '.jpg'
            jpgFile = os.path.join(downloadFolder, jpgFile)
            response = requests.get(resultURL)
            with open(jpgFile,'wb') as file:
                file.write(response.content)
            return jpgFile    

    def setWallpaper(self,file):
        """ 设置文件file为壁纸 """
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file, 0)  # 设置桌面

########################### 第二部分 ###########################################
########################## Tkinter事件 ########################################
### 先建一个壁纸对象 (全局变量)
G =  GetImage()  

def chooseSource_wallhaven_TK():
    """ 选择壁纸源 """
    G.chooseSource('wallhaven')
    info_LABEL.config(text='壁纸源：WallHaven')

def chooseSource_Bing_TK():
    """ 选择壁纸源 """
    G.chooseSource('Bing')
    info_LABEL.config(text='壁纸源：Bing')

def setWallPaper():
    outPath = os.getcwd()+'\\temp'
    f=G.getImage(outPath)
    G.setWallpaper(f)
    info_LABEL.config(text='切换成功！')
    
def rmTemp():
    """ 清空缓存文件夹 """
    shutil.rmtree(os.getcwd()+'\\temp')
  
    
########################### 第三部分 ###########################################
########################## 窗体 ########################################


root = tkinter.Tk()
root.geometry('800x400')
root.title('每日壁纸')
#  一个显示信息的Label
info_LABEL = tkinter.Label(root,text='',justify=tkinter.LEFT,fg='red')
info_LABEL.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.1)

## ======================= 布置添加文件、清空文件的按钮 =========================
BUTTON_changeSource=tkinter.Button(root,text='WallHaven',command=chooseSource_wallhaven_TK)
BUTTON_changeSource.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)

BUTTON_changeSource2=tkinter.Button(root,text='Bing',command=chooseSource_Bing_TK)
BUTTON_changeSource2.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.2)


BUTTON_setWallPaper=tkinter.Button(root,text='设置壁纸',command=setWallPaper)
BUTTON_setWallPaper.place(relx=0.1, rely=0.35, relwidth=0.2, relheight=0.2)

BUTTON_rmTemp=tkinter.Button(root,text='清空缓存',command=rmTemp)
BUTTON_rmTemp.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)

# ## ========================= 布置一个显示提示信息的文本框 =======================
# output1_TEXT = tkinter.Text(root)
# output1_TEXT.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4) # relx=0.55, rely=0.5, relwidth=0.4, relheight=0.4

root.mainloop()


# if __name__=='__main__':
#     G =  GetImage()  
#     f=G.getImage(os.getcwd()+'\\temp')
#     G.setWallpaper(f)