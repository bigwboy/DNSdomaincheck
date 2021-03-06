# -*- coding: utf8 -*-
# time:2017/8/30 10:11
# VERSION:1.0
# __OUTHOR__:guangguang
# Email:kevinliu830829@163.com
# !/usr/bin/env python
# --*-- coding:utf-8 --*--
import os
import sys
import time

import join_file
import split_data
import MyDataStatisticsThread


def DataStatistics(file_name):
    # file_name=sys.argv[1]
    #file_name = 'D:\pythonobject\DNSdomaincheck\jiangsudns20170731'
    print file_name
    if file_name:
        print "分析开始：" + str(time.clock())
        print "切片文档：" + str(time.clock())
        CheckFile = split_data.SplitFiles(file_name)
        FilePath = os.path.dirname(file_name)
        section_data = CheckFile.split_file()  # 分片切割返回分片文件路径和分片文件数
        # data={文件名列表}
        # print section_data
        print "分片完成：" + str(time.clock())

        print "逐个文件统计开始：" + str(time.clock())
        # 线程操作
        FileNum = len(section_data)
        f = 0
        ThreadNum = 10
        if FileNum > 10:  # 判断分片文件是否大于10，若大于每次创建10个线程，小与10个创建与文件数相同线程
            while f < (FileNum / 10):  # 每次创建10个进程    创建文件数/10 次
                headle_file_list = []
                # print section_data
                i = 0
                while i < 10:  # 每次读取10个文件名
                    # print i
                    headle_file_list.append(section_data[i])
                    i += 1
                MyDataStatisticsThread.create_Thread(ThreadNum, headle_file_list)  # 创建10线程
                # f 当前循环次数
                # 待处理的文件列表
                # th.stop_Thread()  # 执行完成后关
                if len(section_data):
                    for i in headle_file_list:
                        section_data.remove(i)  # 将已处理的文件名剔除
                f += 1
            if len(section_data):
                MyDataStatisticsThread.create_Thread(FileNum // 10, section_data)
        else:
            # print "section"+str(section_data)
            MyDataStatisticsThread.create_Thread(FileNum, section_data)  # 创建线程
            # th.stop_Thread()  # 执行完成后关闭

        print "分析文件" + file_name + " 完成！ 用时：" + str(time.clock())

        print "数据汇总开始：" + str(time.clock())
        temp_path = os.path.dirname(section_data[0])
        join_file.join_main(temp_path, 'new')
        print "数据汇总完成～！！！！"
        return True
    else:
        print "错误：请输入需要分析的文件名！"

if __name__ == "__main__":
    try:
        #file_name=sys.argv[1]
        DataStatistics('D:\pythonobject\DNSdomaincheck\AnalyzeData\quanzhou.txt')
    except:
        print "错误：请输入需要分析的文件名！"