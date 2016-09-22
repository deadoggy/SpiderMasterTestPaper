#coding:utf-8
import urllib2
import re
import docx

def findAllUrl():
    '''
    按学科找到所有试题和答案的url
    :return:
    '''
    reponse = urllib2.urlopen('http://zhenti.kaoyan.eol.cn/')
    html = reponse.read()
    Pattern = '''class="biank"><div align="center"><a href="(.*?)"'''
    UrlSet = re.findall(Pattern, html, re.S)
    ret = {
        'politics':[],
        'math':[],
        'english':[]
    }
    for item in UrlSet:
        if [] != re.findall('zhengzhi', item, re.S) or [] != re.findall('politics', item, re.S):
            ret['politics'].append(item)
        elif [] != re.findall('yingyu', item, re.S) or [] != re.findall('english', item, re.S):
            ret['english'].append(item)
        elif [] != re.findall('shuxue', item, re.S) or [] != re.findall('math', item, re.S):
            ret['math'].append(item)
    return ret

def processContent():
    '''
    把网页内容处理成正常的内容
    :return:
    '''

def findAllSheet():
    '''
    通过findllUrl()找到的链接爬取网页内容
    :return:
    '''
    UrlLib = findAllUrl()
    SubjectSet = ['politics', 'math', 'english']
    for subject in SubjectSet:
        for item in UrlLib[subject]:
            response = urllib2.urlopen(item)
            html = response.read()
            


