# coding=utf-8

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Page():
    def __init__(self, driver):
        self.mydriver = driver

    @property
    def driver(self):
        return self.mydriver

    def _sendKey(self,element,keys,keepKeys):
        '''

        :param element: 传入的webElement
        :param keys: 赋给webElement的值
        :param keepKeys: 是否保留默认值
        :return:
        '''
        if(element and keys):
            if (not keepKeys):
                element.clear()
            element.send_keys(keys)

    def id(self,id,keys=None,keepkeys=False,senconds=None):
        '''

        :param id:
        :param keys:
        :param keepkeys:
        :param senconds:
        :return:
        '''
        if (senconds):
            element=WebDriverWait(self.driver,senconds,1).until(EC.visibility_of_element_located(By.ID,id))
        else:
            element=self.driver.find_element_by_id(id)
        self._sendKey(element,keys,keepkeys)
        return element
