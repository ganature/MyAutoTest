# coding=utf-8

from Page import Page

class LoginPage(Page):
    '''
    登录页面
    '''

    def __init__(self,driver):
        self.loginPage=Page(driver)

    def loginIn(self):
        '''
        登录
        :return:
        '''
        pass

    def loginOut(self):
        pass
