# encoding=utf-8
from selenium import webdriver
from Mydriver import MyDriver

class DriverFactory:
    '''
    驱动构造
    '''
    def driver(self):
        dr = webdriver.Ie()
        d = MyDriver(dr)
        return d

    def quit(self,myDriver):
        myDriver.quit()


