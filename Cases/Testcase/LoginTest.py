# coding=utf-8

from BaseTest import BaseTest
from Cases.PageObject.Base.LoginPage import LoginPage
class LoginTest(BaseTest):
    '''
    登录模块测试
    '''

    def __init__(self):
        self.lPage=LoginPage()

    def test_001_loginIn(self):
        '''
        登录测试用例001
        :return:
        '''
        self.lPage.loginIn()
        pass

