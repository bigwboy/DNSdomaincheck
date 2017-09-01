# -*- coding: utf8 -*-
#time:2017/8/30 10:29
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com

# encoding: UTF-8
import threading

import handle_file


class MyThread(threading.Thread):
    def __init__(self,fileNum,file_list):
        threading.Thread.__init__(self)
        self.file_data=file_list
        self.fileNum=fileNum
    def run(self):
        check_file= handle_file.handle(self.fileNum, self.file_data) #单个进程处理单个文件
        check_file.opera()
        #print "12121" +str(self.file_data)
        #self.stop() #完成后关闭线程
    def stop(self):
        self.thread_stop = True
        print "线程关闭~!!"
def create_Thread(fileNum,file_list):
        i=0
        ThreadNum=len(file_list)
        for i in range(ThreadNum):#创建10个线程
            t = MyThread(fileNum,str(file_list[i]))
            t.start()
            i+=1
            t.join()
        #print "线程结束"





if __name__ == '__main__':
    num=4
    file_list=['temp_file_1.part','temp_file_2.part','temp_file_3.part','temp_file_4.part']
    create_Thread(num,1,file_list)