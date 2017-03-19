# coding=utf-8


class MyDriver(object):

    def __init__(self,driver):
        self.mydriver = driver

    @property
    def driver(self):
        return self.mydriver

    def getUrl(self,url):
        self.driver.get(url)

    def maxWindow(self):
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
