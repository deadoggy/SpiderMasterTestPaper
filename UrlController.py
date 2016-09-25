#coding:utf-8
import urllib2
import re



class UrlController:
    RootUrl = 'http://kaoyan.eol.cn/shiti/'
    def __findSubjectUrl(self):
        '''
        找到按学科分类的母链接
        :return:
        '''
        reponse = urllib2.urlopen(self.RootUrl)
        html = reponse.read()
        Pattern = u'''>2016-05-25</span><a href=".(.*?)">'''
        UrlSet = re.findall(Pattern, html, re.S)
        ret = {
            'politics': [],
            'math': [],
            'english': []
        }
        for item in UrlSet:
            if [] != re.findall('zhengzhi', item, re.S) or [] != re.findall('politics', item, re.S):
                ret['politics'].append(self.RootUrl + item)
            elif [] != re.findall('yingyu', item, re.S) or [] != re.findall('english', item, re.S):
                ret['english'].append(self.RootUrl + item)
            elif [] != re.findall('shuxue', item, re.S) or [] != re.findall('math', item, re.S):
                ret['math'].append(self.RootUrl + item)
        return ret

    def __getAllSheetUrl(self, RootUrl, Subject):
        '''
        给定学科母链接，找到所有的试题URL
        :param RootUrl:学科母链接
        :param Subject: 学科名，用于区分不同的Pattern
        :return:['www.1', 'www.2', ...]
        '''
        # 读取页面
        response = urllib2.urlopen(RootUrl)
        html = response.read().decode('gbk')

        # 根据学科找到对应的Pattern
        Pattern = ""
        if Subject == 'politics':
            Pattern = u'''<td><a href="(.*?).shtml">20..年</a></td>'''
        elif Subject == 'english':
            Pattern = u'''<p align="center"><a href="(.*?).shtml">英语二</a></p>'''
        elif Subject == 'math':
            Pattern = u'''<p align="center"><a href="(.*?).shtml">数三</a></p>'''

        ret = re.findall(Pattern, html)
        return ret

    def getAllSheetUrlBySubject(self):
        '''
        返回一个根据学科分类的所有试题的URL字典
        :return:
        '''
        subjectroot = self.__findSubjectUrl()
        SheetDic = {
            'math': [],
            'english': [],
            'politics': []
        }
        for key in subjectroot.keys():
            SheetDic[key] = self.__getAllSheetUrl(subjectroot[key][0], key)

        return SheetDic












            


