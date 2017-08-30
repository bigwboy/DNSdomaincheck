# -*- coding: utf8 -*-
#time:2017/8/30 10:30
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com

#!/usr/bin/env python
#--*-- coding:utf-8 --*--
import rw_file
import os
import time
import th

class handle():   #处理文件类
    def __init__(self,dirNum,file_name):
        self.dirNum=dirNum
        self.file_name=file_name
        #self.path='./temp_part_file/'
    def openFile(self,file_name): #打开分片的文件
                #file_name=self.path+self.file_name
                f = open(self.file_name, 'rb') #打开文件
                lines = f.readlines()  #读取单个文件的每一行
                i = 0
                domain = []
                for line in lines:
                    i = i + 1
                    data = line.split()
                    # 判断字符是否为异常
                    if len(data) < 3:
                        continue
                    domain.append(data[5])
                return domain
        # 对读取的数据金喜排序和统计工作
    def opera(self):
        i = 0
        dict1 = {}
        # while i <10:
        data=self.openFile(self.file_name)
        while i < len(data):
            # 统计重复次数
            _key = data[i]
            if data[i] not in dict1:
                _value = data.count(data[i])
                dict1.setdefault(_key, _value)
            i = i + 1
        #print "check date line:" + str(i)
        # 写入字典做排序
        dict = sorted(dict1.iteritems(), key=lambda d: d[1], reverse=True)
        #print "check over time:" + str(time.clock())
        #print "dict:"+str(dict)
        self.write_after_part_file(dict) #操作完成后，结果保存在新的文件中

    def write_after_part_file(self,dict):
        part_num = 1
        try:
            check_over_file = rw_file.OPfile(part_num, self.file_name, True, dict)
            after_temp_file=check_over_file.write_file()
            #print " after_temp_file:"+after_temp_file
            #return after_temp_file #分析处理后的文件名
        except IOError as err:
            print(err)
        except Exception:
            print Exception







if __name__=="__main__":
    test=handle(2,'./temp_part_file/temp_file_3.part')
    test.opera()