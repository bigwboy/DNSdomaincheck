# -*- coding: utf8 -*-
#time:2017/9/4 13:13
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
import DNS
import RoadWriteFile
import MyDomainAnalysisThread
import re
#开线程
def DomainAnalysisThreading(DomainDict):
    DomainListNum=len(DomainDict)
    ThreadNum = 10
    RuturnData=[]
    f=0
    if DomainListNum > 10:  # 判断需要解析域名是否大于10，若大于每次创建10个线程，小与10个创建与文件数相同线程
            while f < (DomainListNum / 10):  # 每次创建10个进程    创建文件数/10 次
                DomainList = []
                # print DomainList
                i = 0
                while i < 10:  # 每次读取10个域名
                    # print i
                    DomainList.append(DomainDict.items()[i])
                    i += 1
                MyDomainAnalysisThread.create_Thread(ThreadNum, DomainList)  # 创建10线程
                # f 当前循环次数
                # 待处理的文件列表
                # th.stop_Thread()  # 执行完成后关
                if len(DomainDict):
                    for i in DomainList:
                        DomainDict.pop(i[0])  # 将已处理的域名剔除
                f += 1
            if len(DomainDict):
                MyDomainAnalysisThread.create_Thread(DomainListNum // 10, DomainDict.keys())
    else:
            # print "section"+str(DomainList)
            MyDomainAnalysisThread.create_Thread(DomainListNum, DomainDict)  # 创建线程
            # th.stop_Thread()  # 执行完成后关闭

#解析域名
def DomainAnalysis(Domain):
    DNS.DiscoverNameServers()
    reqobj = DNS.Request()
    reqobj.defaults['server'] = ['113.215.2.222']
    ReturnData=[]
    Returndomain=[]
    Returndomain.append(Domain)
    j=False
    try:
        answerobj = reqobj.req(name=Domain,qtype = DNS.Type.A)
        x = answerobj.answers
        if not x:
            ReturnData.append(str(Domain) + "," + "False" )
        else:
            for donequeries in x:
                i = 1
                if j:
                    break
                if donequeries['typename'] == "CNAME":  # 判断是否含有CNAME
                    DomainCname = donequeries['data']
                    Returndomain.append(DomainCname)
                elif donequeries['typename'] == "A":
                    re_ip = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')  # 判断IP
                    if re_ip.match(donequeries['data']):  # 直到IP停止
                        A = donequeries['data']

    except Exception,e:
        print e
        pass
    return ReturnData



#对获取数据进行初步处理
def PretereatmentData(AnalyzeData):
    DomainDict={}
    for LineData in AnalyzeData:
        LineData=str(LineData).split(',')
        Domain=LineData[1]
        LineData.remove(Domain)
        DomainDict[Domain]=LineData
    return DomainDict
    pass

#DEBUG
if __name__ == "__main__":
    AnalyzeData = RoadWriteFile.ReadFile('..\\OutFile\\Statistics.txt')
    DomainDict=PretereatmentData(AnalyzeData.ReturnData())
    DomainAnalysisThreading(DomainDict)