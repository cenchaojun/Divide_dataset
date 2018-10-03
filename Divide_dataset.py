# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:13:52 2018

@author: 天蓝蓝铭靓靓
"""

import os
import random
import shutil

Train_dir = "D:/Train"
Test_dir = "D:/Test"
train_percentage = 0.8  #训练集比例，(0,1)
 
def Divide_dataset(Train_dir, Test_dir, train_percentage):
    if not os.path.exists(Test_dir):
        os.mkdir(Test_dir)
    folders = os.listdir(Train_dir)
    for folder in folders :
        dir = Train_dir + '/' + folder + '/'
        if not os.path.exists(Test_dir + '/'+ folder + '/'):
            os.mkdir(Test_dir + '/' +folder + '/')
        pictures = os.listdir(dir)
        random.shuffle(pictures)
        train_num = int(len(pictures) * train_percentage)
        
        for i in pictures[train_num:]:
            shutil.move(dir + i , Test_dir + '/' + folder + '/')
            
if __name__ == '__main__':
    Divide_dataset(Train_dir, Test_dir, train_percentage)