#coding:utf-8
from UrlController import UrlController as UC
import docx
import urllib
import  urllib2
import re

urlcontroller = UC()

class SheetController:
    __sheetdic = urlcontroller.getAllSheetUrlBySubject()

    def __processPoliticsSheet(self, url):
        '''
        处理政治试题
        政治题的内容直接显示在页面上，所以要提取页面并替换关键字
        :return:
        '''

        response = urllib2.urlopen(url)
        html = response.read().decode('gbk')
        PageCount = int(re.findall('''var _PAGE_COUNT="(.*?)"''', html)[0])

        
