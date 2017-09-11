# -*- coding: utf8 -*-
#time:2017/8/30 10:30
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com

import re

# !/usr/bin/env python
# --*-- coding:utf-8 --*--
import rw_file


class handle():   #处理文件类
    def __init__(self,dirNum,file_name):
        self.dirNum=dirNum
        self.file_name=file_name
        self.DomainReg = re.compile('(?i)\\b((?=[a-z0-9-]{1,63}\\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\\.)+[a-z]{2,63}\\b')
        self.IpRegre_ip = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')  # 判断IP
        #self.path='./temp_part_file/'
    def openFile(self): #打开分片的文件
                #file_name=self.path+self.file_name
                f = open(self.file_name, 'rb') #打开文件
                lines = f.readlines()  #读取单个文件的每一行
                i = 0
                Domain = []
                LocalIp=[]
                for line in lines:
                    i = i + 1

                    #######某某广电DNS专用
                    #DataList = line.split('|')
                    # if len(DataList) < 3:
                    #     continue
                    # for Data in DataList:
                    #
                    #     if self.DomainReg.match(Data):
                    #         # 域名判断
                    #         Domain.append(Data)
                    #     elif self.IpRegre_ip.match(Data):
                    #         # ip判断
                    #         LocalIp.append(Data)

                    ###############流控数据
                    DataList=line.split()
                    Data=DataList[0]
                    if self.DomainReg.match(Data):
                            # 域名判断
                            Domain.append(str(Data))
                    elif self.IpRegre_ip.match(str(Data)):
                            # ip判断
                            LocalIp.append(str(Data))


                return Domain
        # 对读取的数据进行排序和统计工作
    def opera(self):
        i = 0
        dict1 = {}
        # while i <10:
        data=self.openFile()
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
    test=handle(2,'D:\pythonobject\DNSdomaincheck\\temp_part_file\\temp_file_3.part')
    test.opera()