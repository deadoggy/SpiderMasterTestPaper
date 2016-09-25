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

        response = urllib2.urlopen(url + '.shtml')
        html = response.read().decode('gbk')
        pagecount = int(re.findall('''var _PAGE_COUNT="(.*?)"''', html)[0])

        SheetContent = ""

        for index in range(0, pagecount):
            if 0 == index:
                pageurl = url + '.shtml'
            else:
                pageurl = url + '_' + str(index) + '.shtml'


    def __processPerSheet(self, url):
        '''
        处理每一页的内容（政治和英语）
        :param url: 该页的url
        :return:
        '''
        ret = ""

        html = urllib2.urlopen(url).read().decode('gbk')
        pattern_1 = '<div class="TRS_Editor">(.*?)</div>'
        pattern_2 = '<p align="(.*?)">(.*?)</p>'

        editor = re.findall(pattern_1, html)
        contentset = re.findall(pattern_2, editor)

        for tag in contentset:
            if()





