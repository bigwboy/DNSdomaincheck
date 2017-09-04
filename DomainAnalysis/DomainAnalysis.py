# -*- coding: utf8 -*-
#time:2017/9/4 13:13
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
import DNS
import RoadWriteFile

#域名解析
def DomainAnalysis(DomainList):
    DNS.DiscoverNameServers()
    reqobj = DNS.Request()
    reqobj.defaults['server'] = ['113.215.2.222']

#DEBUG
if __name__ == "__main__":
    pass