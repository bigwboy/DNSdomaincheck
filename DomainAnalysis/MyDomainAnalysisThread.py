# -*- coding: utf8 -*-
#time:2017/9/4 13:35
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
import threading

import DomainAnalysis


class MyThread(threading.Thread):
    def __init__(self,DomainNum,Domain):
        threading.Thread.__init__(self)
        self.Domain=Domain
        self.DomainNum=DomainNum
    def run(self):
        AnalysitData= DomainAnalysis.DomainAnalysis(self.Domain) #单个进程处理单个文件
        AnalysitData.opera()
        #print "12121" +str(self.file_data)
        #self.stop() #完成后关闭线程
    def stop(self):
        self.thread_stop = True
        print "线程关闭~!!"
def create_Thread(DomainNum,DomainList):
    Threadings = []
    ThreadNum = len(DomainList)

    # 创建ThreadNum个进程
    for i in range(ThreadNum):
        t = MyThread(DomainNum, DomainList[i][0])
        Threadings.append(t)
    # 开启所有进程
    for i in range(ThreadNum):
        Threadings[i].start()
    # 等待所有线程结束
    for i in range(ThreadNum):
        Threadings[i].join()

    #print "线程结束"
#DEBUG
if __name__ == "__main__":
    pass