#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# #    File: 
# #    Project: 
# #    Author: zzy
# #    mail: elliot.bia.8989@outlook.com
# #    github: https://github.com/elliot-bia
# #    Date: 2019-11-17 11:44:11
# #    LastEditors: zzy
# #    LastEditTime: 2019-11-17 16:17:49
# #    ---------------------------------
# #    Description: 
###
for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d= %d" % (j,i,j*i),end=" ")
     print("")