#coding:utf-8
import urllib
import urllib2
import re
import docx

RootUrl = 'http://kaoyan.eol.cn/shiti/'


def findSubjectUrl():
    '''
    找到按学科分类的母链接
    :return:
    '''
    reponse = urllib2.urlopen(RootUrl)
    html = reponse.read()
    Pattern = u'''>2016-05-25</span><a href=".(.*?)">'''
    UrlSet = re.findall(Pattern, html, re.S)
    ret = {
        'politics':[],
        'math':[],
        'english':[]
    }
    for item in UrlSet:
        if [] != re.findall('zhengzhi', item, re.S) or [] != re.findall('politics', item, re.S):
            ret['politics'].append(RootUrl+item)
        elif [] != re.findall('yingyu', item, re.S) or [] != re.findall('english', item, re.S):
            ret['english'].append(RootUrl+item)
        elif [] != re.findall('shuxue', item, re.S) or [] != re.findall('math', item, re.S):
            ret['math'].append(RootUrl+item)
    return ret

def getAllSheetUrl(RootUrl, Subject):
    '''
    给定学科母链接，找到所有的试题URL
    :param RootUrl:学科母链接
    :param Subject: 学科名，用于区分不同的Pattern
    :return:['www.1', 'www.2', ...]
    '''
    #读取页面
    response = urllib2.urlopen(RootUrl)
    html = response.read().decode('gbk')

    #根据学科找到对应的Pattern
    Pattern = ""
    if Subject == 'politics':
        Pattern = u'''<td><a href="(.*?)">20..年</a></td>'''
    elif Subject == 'english':
        Pattern = u'''<p align="center"><a href="(.*?)">英语二</a></p>'''
    elif Subject == 'math':
        Pattern = u'''<p align="center"><a href="(.*?)">数三</a></p>'''

    ret = re.findall(Pattern, html)
    return ret



test = findSubjectUrl()

SheetDic = {
    'math': [],
    'english': [],
    'politics': []
}

for key in test.keys():
    SheetDic[key] = getAllSheetUrl(test[key][0], key)

pass





            


