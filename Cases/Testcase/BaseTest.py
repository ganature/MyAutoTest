# coding=utf-8

import unittest


class BaseTest(unittest.TestCase):
    def __init__(self,Driver):
        super(BaseTest, self).__init__()
        self.driver = Driver
        self.url = 'http://www.baidu.com'

    def setUp(self):
        self.driver.getUrl(self.url)
        self.driver.maxWindow()

    def tearDown(self):
        self.driver.quit()

