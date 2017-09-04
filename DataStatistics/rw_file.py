# -*- coding: utf8 -*-
#time:2017/8/30 10:21
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
#!/usr/bin/env python
#--*-- coding:utf-8 --*--
import os
import MyMultithreadingStatistics
import pyExcelerator
import time


class OPfile():
    def __init__(self,part_num,file_name,tpye=False,*line_content):
        #参数说明： part_num 为文件号码
        #          file_name 绝对路径文件名
        #          tpye 处理切片（0）和切片后文件(1)
        #          line_content 切片写入行
        self.part_num=part_num
        self.file_name=file_name
        self.line_content=line_content
        self.type=tpye
        self.temp_path = os.path.dirname(self.file_name)  # 获取文件的路径（不含文件名）
    def get_part_file_name(self):
        """"获取分割后的文件名称：在源文件相同目录下建立临时文件夹temp_part_file，然后将分割后的文件放到该路径下"""
        temp_path = os.path.dirname(self.file_name)  # 获取文件的路径（不含文件名）
        part_file_name = temp_path + "\\temp_part_file"
        if not os.path.exists(part_file_name):  # 如果临时目录不存在则创建
                try:
                    os.makedirs(part_file_name)
                except Exception:
                    print Exception
        if self.type: #判断是是否为切片
            part_file_name += self.file_name+".new"
        else:
            part_file_name += os.sep + "temp_file_" + str(self.part_num) + ".part"
        return part_file_name
    def write_file(self):
        if self.type:
            part_file_name=self.file_name+".new"
            #print  self.file_name +".new" + '\t' + "正在写入。。。"
            #print "self.line_content:    "+str(self.line_content)
            try:
                with open(part_file_name, "w+") as part_file:
                    for i in self.line_content:
                        for data_line in i:
                            #print "data_line:"+ data_line[0]
                            part_file.writelines(str(data_line[0])+" "+str(data_line[1])+'\n')
            except IOError as err:
                print(err)
            #print  part_file_name + "写入完成！"
            return part_file_name
        else:
            part_file_name = self.get_part_file_name()
            """将按行分割后的内容写入相应的分割文件中"""
            #print "temp_file_" + str(self.part_num) + ".part" + '\t' + "正在写入。。。"
            try:
                with open(part_file_name, "w") as part_file:
                    part_file.writelines(self.line_content[0])
            except IOError as err:
                print(err)
            #print "temp_file_" + str(self.part_num) + ".part" + '\t' + "写入成功"
            return part_file_name



if __name__=="__main__":
    test=OPfile(3,'./test.txt',10)