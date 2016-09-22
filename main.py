#coding:utf-8
import urllib
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
    Pattern = u'''class="biank"><div align="center"><a href="(.*?).shtml"'''
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

def processContent(content, Title):
    '''
    把网页内容处理成正常的内容并打印
    网页有可能是试卷内容或者试卷的链接，如果是链接的话直接下载，
    如果是试卷内容的话就处理字符串并下载
    :return:
    '''
    #确定学科以便确定路径
    subject = ""
    if [] != re.findall(u'政治', Title):
        subject = u"politic//"
    elif [] != re.findall(u'英语', Title):
        subject = u"english//"
    elif [] != re.findall(u'数学', Title):
        subject = u"math//"

    #先查看是否有链接，有的话直接下载
    DirDownloadUrlSet = re.findall('''<a target="_blank" href="(.*?)">''', content)
    if [] != DirDownloadUrlSet:
        #有链接
        urllib.urlretrieve(DirDownloadUrlSet[0], subject + u"//" + Title + u".doc")
    else:
        #没有链接




def printSheet(path):
    '''
    处理每一套真题
    :param path: 真题的路径（不带 .shtml ，方便进行每页的处理）
    :param subject : 当前处理的科目，方便docx命名
    :return:
    '''
    Response = urllib2.urlopen(path)
    Html = Response.read()
    #找到title
    Title = re.findall(u'''<title>(.*?)-考研-中国教育在线</title>''', Html)[0]
    #找到页数
    SheetCount = int(re.findall('''_PAGE_COUNT="(.*?)"''', Html)[0])
    PaperContent = ""

    # 获取每一页
    for index in range(0, SheetCount):
        PagePath = path
        #生成每个页面的链接
        if 0 != index:
            PagePath = PagePath + '_' + str(index)
        PagePath = PagePath + '.shtml'
        #拿到html的内容
        PageResponse = urllib2.urlopen(PagePath)
        PageHtml = PageResponse.read()
        PageContent = re.findall('''<div class="TRS_Editor">(.*?)</div>''', PageHtml, re.S)[0]
        #添加到试卷内容中
        PaperContent = PaperContent + PageContent
    #处理内容中的标签并且打印到docx中
    processContent(PaperContent, Title)

def printAllPaper():
    '''
    通过findllUrl()找到的链接爬取网页内容
    :return:
    '''
    UrlLib = findAllUrl()
    SubjectSet = ['politics', 'math', 'english']
    for subject in SubjectSet:#每个科目
        for item in UrlLib[subject]:#每个链接


            


