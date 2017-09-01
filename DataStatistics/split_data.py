# -*- coding: utf8 -*-
#time:2017/8/30 10:16
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
#!/usr/bin/env python
#--*-- coding:utf-8 --*--
import os

import rw_file


class SplitFiles():
    """按行分割文件"""
    def __init__(self, file_name, line_count=1000):
        """初始化要分割的源文件名和分割后的文件行数"""
        self.file_name = file_name
        self.line_count = line_count
    def split_file(self):
        if self.file_name and os.path.exists(self.file_name): #判断文件是否存在
            try:
                with open(self.file_name) as f : # 使用with读文件
                    temp_count = 0
                    temp_content = []
                    part_num = 1
                    after_file_list=[]
                    for line in f:
                        if temp_count < self.line_count:
                            temp_count += 1
                        else :
                            split= rw_file.OPfile(part_num, self.file_name, False, temp_content)
                            #part_num文件编号
                            #self.file_name  文件名
                            #tpye=False #切片开关
                            #temp_content需要写入的文件内容
                            after_file_list.append(split.write_file())#返回分片成功文件名保存至列表
                            part_num += 1
                            temp_count = 1
                            temp_content = []
                        temp_content.append(line)
                    else : # 正常结束循环后将剩余的内容写入新文件中
                        split = rw_file.OPfile(part_num, self.file_name, False, temp_content)
                        # part_num文件编号
                        # self.file_name  文件名
                        # tpye=False #切片开关
                        # temp_content需要写入的文件内容
                        split.write_file()
                        after_file_list.append(split.write_file())  # 返回分片成功文件名保存至列表
                    #print "afpter_file_list:  "+str(after_file_list)
                    return after_file_list
            except IOError as err:
                print(err)
            except Exception:
                print Exception
        else:
            print("%s is not a validate file" % self.file_name)

if __name__ == "__main__":
    sf = SplitFiles('/home/liuguangwei/PycharmProjects/bigdata/test.txt')
    sf.split_file()
