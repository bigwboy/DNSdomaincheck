# -*- coding: utf8 -*-
#time:2017/8/30 10:32
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com

#!/usr/bin/env python
#--*-- coding:utf-8 --*--
import rw_file
import pyExcelerator
import time
import os
import operator

# 获取指定路径下所有指定后缀的文件
# dir 指定路径
# ext 指定后缀，链表&不需要带点 或者不指定。例子：['xml', 'java']
def GetFileFromThisDir(dir,ext = None):
  allfiles = []
  needExtFilter = (ext != None)
  for root,dirs,files in os.walk(dir):
    for filespath in files:
      filepath = os.path.join(root, filespath)
      extension = os.path.splitext(filepath)[1][1:]
      if needExtFilter and extension in ext:
        allfiles.append(filepath)
      elif not needExtFilter:
        allfiles.append(filepath)
  #print allfiles
  return allfiles


def open_new_File(file_name):  # 打开文件
    f = open(file_name, 'rb')  # 打开文件
    lines = f.readlines()  # 读取单个文件的每一行
    return lines

def join_check_file(file_name):
    i = 0
    dict1 = {}
    # while i <10:
    data = open_new_File(file_name)
    while i < len(data):
        # 统计重复次数
        _key = data[i]
        if data[i] not in dict1:
            _value = data.count(data[i])
            dict1.setdefault(_key, _value)
        i = i + 1
    print "check date line:" + str(i)
    # 写入字典做排序
    dict = sorted(dict1.iteritems(), key=lambda d: d[1], reverse=True)
    print "check over time:" + str(time.clock())

def write_execl(dict,all_value):
    # dict 需要写入文件的数据列表
    #all_value 所有出网访问总和
    # 创建workbook和sheet对象
    wb = pyExcelerator.Workbook()
    ws = wb.add_sheet(u'第一页')
    ws.write(0, 0, u'域名')
    ws.write(0, 1, u'访问次数')
    ws.write(0, 2, u'域名占比')
    item = 0
    # # 只写入TOP10000
    while item < 10000:
        # while item<100:
        row = 0
        while row < 2:
            # print dict[item][row]
            ws.write(item + 1, row, dict[item][row])
            row += 1
        ws.write(item + 1, 2, format(dict[item][1] / float(all_value), ".2%"))  # j计算百分比占比
        item += 1
        wb.save('top100.xls')

def WriteTxt(Dict,AllValue,dir):
    OutFileDir=dir.strip('temp_part_file')+'OutFile\\'
    wb=open((OutFileDir+'Statistics.txt'),'wb')
    item=0
    for Wrline in Dict:
        if item < AllValue:
            Wdata=str(item+1)+','+str(Wrline[0])+','+str(Wrline[1])+','+str(format(Wrline[1] / float(AllValue), ".2%"))+'\n'
            item+=1
            wb.writelines(Wdata)
        else:
            break

    print "汇总数据写入Statistics.txt文件完成！"
    print "汇总结束时间:" + str(time.clock())


def join_main(dir,ext):
    # dir 指定路径
    # ext 指定后缀，链表&不需要带点 或者不指定。例子：['xml', 'java']
    line_data={}
    after_new_file_list=GetFileFromThisDir(dir, ext)  #返回文件夹中的.new文件
    for new_life in after_new_file_list:
        new_life_line=open_new_File(new_life) #返回文件中的每行数据
        i=0
        while i < len(new_life_line):
            for domain_data in new_life_line:
                    key = domain_data.split()[0]  #域名为键值
                    if domain_data.split()[0] not in line_data:
                        try:
                            #value = domain_data.split()[1]  #域名访问次数为value
                            value=domain_data.strip()[-1]
                            line_data.setdefault(key, int(value))
                        except Exception,e:
                            print str(e)+':'+domain_data
                    else:
                        line_data[key]=int(line_data[key])+int(domain_data.split()[-1])
                    i = i + 1
    line_d =sorted(line_data.iteritems(), key=lambda d: d[1], reverse=True)
    all_value=0
    for i in line_d:
        all_value= all_value+ int(i[1])
    #print all_value
    #write_execl(line_d,all_value) #写入EXECL文件
    WriteTxt(line_d, all_value,dir)





if __name__=="__main__":
    join_main('D:\\pythonobject\\DNSdomaincheck\\temp_part_file','new')
