# -*- coding: utf8 -*-
#time:2017/9/4 13:35
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
import threading

import DomainAnalysis


class MyThread(threading.Thread):
    def __init__(self,DomainList,DomainNum):
        threading.Thread.__init__(self)
        self.file_data=DomainList
        self.fileNum=DomainNum
    def run(self):
        AnalysitData= DomainAnalysis.DomainAnalysis(self.fileNum, self.file_data) #单个进程处理单个文件
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
#DEBUG
if __name__ == "__main__":
    pass