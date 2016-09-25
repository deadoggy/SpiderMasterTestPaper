#coding:utf-8
from UrlController import UrlController as UC
from docx import Document
from docx.enum.text import *
import  urllib2
import re

class SheetController:
    urlcontroller = UC()
    __sheetdic = urlcontroller.getAllSheetUrlBySubject()

    def __processSheet(self, url, subject):
        '''
        处理每一套试题
        :return:
        '''

        response = urllib2.urlopen(url + '.shtml')
        html = response.read().decode('gbk')
        pagecount = int(re.findall('''var _PAGE_COUNT="(.*?)"''', html)[0])
        title = re.findall(u'''<title>(.*?)-考研-中国教育在线</title>''', html)[0]
        docx = Document()

        for index in range(0, pagecount):
            if 0 == index:
                pageurl = url + '.shtml'
            else:
                pageurl = url + '_' + str(index) + '.shtml'
            self.__processPerSheet(pageurl, docx)

        docx.save(subject + '/' + title + '.docx')

    def __processPerSheet(self, url, docx):
        '''
        处理每一页的内容（政治和英语）
        :param url: 该页的url
        :return:
        '''

        html = urllib2.urlopen(url).read().decode('gbk')
        pattern_1 = u'''<div class=TRS_Editor>(.*?)</div>'''
        pattern_1_2 =  u'''<div class="TRS_Editor">(.*?)</div>'''#网站上class不一致
        pattern_2 = u'''<p align="(.*?)">(.*?)</p>'''

        editor = re.findall(pattern_1, html, re.S)
        if [] == editor:
            editor = re.findall(pattern_1_2, html, re.S)
        contentset = re.findall(pattern_2, editor[0], re.S)

        for tag in contentset:
            if tag[0] == u'justify':#如果是正常内容
                if tag[1] == u'&nbsp;':#如果有空格
                    docx.add_run(' ')
                elif [] != re.findall(u'<strong>', tag[1]):#如果有黑体
                    content = re.findall(u'<strong>(.*?)</strong>', tag[1])[0]
                    docx.add_paragraph(content).bold = True
                else:
                    docx.add_paragraph(tag[1])
            elif tag[0] == u'center': #居中内容
                if [] != re.findall('<img', tag[1]):#如果是图片：
                    imgurl = url[0:len(url) - 23] + re.findall('''src =".(.*?)" ''', tag[1])[0]#获取图片链接
                    docx.add_picture(imgurl).paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                else:
                    docx.add_paragraph(tag[1]).paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        pass

    def getAllPaper(self):
        for key in self.__sheetdic.keys():
            for item in self.__sheetdic[key]:
                self.__processSheet(item, key)
        print "Done!"








