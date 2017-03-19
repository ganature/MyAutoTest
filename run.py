# encoding=utf-8

from Common.driver import DriverFactory
from Data.Db import DataConfig
from HTMLTestRunner import HTMLTestRunner
import unittest
import sys
import os

if __name__=='__main__':
    '''初始化数据'''
    data=DataConfig()
    data.initDb()

    '''初始化驱动'''
    factory=DriverFactory()
    myDriver=factory.driver()

    '''定义测试报告的路径和文件'''
    curpath=os.path.dirname(sys.argv[0])#获取当前路径
    reportPath=curpath+'/Data/report.html'
    fp=open(reportPath,'wb')

    '''定义测试报告'''
    runner=HTMLTestRunner(
        stream='',#操作文件的句柄
        title='',#测试报告的标题
        description=''#描述
    )
    '''构建测试集'''
    '''discover批量添加目录下，以文件名查找所有以'test'开始的测试用例'''
    suite=unittest.TestLoader.discover()

    '''执行测试'''
    runner.run(suite)
    fp.close()
