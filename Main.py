#coding=utf-8
#Movie_spider2 Version 1.0 By Bluemit
import chardet
import gzip
import json
import random
from bs4 import BeautifulSoup
import urlparse
import urllib2
import re
from time import sleep

import StringIO


class UrlManager(object):
    def __init__(self):
        self.new_urls = []
        self.old_urls = set()
        fin=open("3.txt", "r")
        i=0
        while True:
            line = fin.readline()
            i+=1
            if (line and (i-1)%7==0):
                line=line.strip('\n')
                self.new_urls.append(line)    # do something here
            else :
                if line:
                    continue
                else:
                    break
        fin.close()
        print self.new_urls

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            # print self.old_urls
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


class Downloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        # print response.read()
        print "ss"
        if response.info().get('Content-Encoding', "") == 'gzip':
            buf = StringIO.StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            content = f.read()
        else:
            content = response.read()
        # print content

        return content


class Movie_Parser(object):
# 网页解析器

    def _get_new_data0(self, page_url, soup):
        jss=json.loads(soup.encode("utf-8"))
        js=jss['data2']
        for j in js:
            print j['BoxOffice']
            fout=open('result3.html','a')
            fout.write(j['BoxOffice'])
            fout.write("<br>")
            fout.close()
        print 'title'

        print 'OKOK'

        return title
    def _get_new_data1(self, page_url, soup):
        res_data = {}
        # print soup
        title=soup.find('img',style="height:260px;")
        fout=open('result.html','a')
        fout.write(title['alt'].encode('utf-8'))
        fout.write('&nbsp;&nbsp;&nbsp;&nbsp;')
        fout.close()
        print 'OKOK'


        # print conts


        # print title.get_text()
        # print 'title'
        #赞同数代码：<span class="count">273</span>
        #答案号代码：<a class="zg-anchor-hidden" name="answer-30358716"></a>
    #    answers = soup.find_all('div', class_="zm-item-vote-info")
        # print answers
        # print 'answers'
        # answer_urls=soup.find_all('a', class_="count")
    #
            # if en.find('K')!=-1:
            #     res_data['counts'] = en
            #     res_data['status'] = 0
            #     print "to1"
            #     break
            # if eval(en)<100:
            #     print 777
            #     print answer.get_text()
            #     continue
            # else:
            #     # print 888
            #     if(eval(en)>maxcount):
            #         maxcount=eval(en)
            #         res_data['counts'] = maxcount
            #         res_data['status'] = 1
#
        return title
    def _get_new_data2(self, page_url, soup):
        res_data = {}
        # print soup
        contsss = soup.find('div',class_='ziliaofr')
        contss=contsss.find('div',class_='cont')
        conts=contss.find_all('p')
        i=0
        fout=open('result.html','a')
        for cont in conts:
            i+=1
            if(i==3 or i==5 or i==7):
                fout.write(cont.get_text().strip().encode('utf-8'))
                fout.write('&nbsp;&nbsp;&nbsp;&nbsp;')
        fout.close()
        print 'ends'
        try:
            title = soup.find('table', class_='datebg datebg01 datebg03')
        except:
            fout=open('result.html','a')
            fout.write("<br>")
        # print title
        # print "title"
        # print title
        try:
            ress = title.find_all('td')
        except:
            fout=open('result.html','a')
            fout.write("<br>")
        inver=[]
        i=0
        print 'OK00'
        fout=open('result.html','a')

        for res in ress:
            i+=1
            if((i-3)%5==0):
                inver.append(res.get_text().encode('utf-8'))
            if((i-5)%5==0 and eval(res.get_text().encode('utf-8'))<=7):
                break
        print 'OK01'

        l=len(inver)-1
        if(l==-1):
            fout=open('result.html','a')
            fout.write("<br>")
            return res
        while(l>=0):
            print 'OK02'
            fout.write(inver[l])
            fout.write('&nbsp;&nbsp;&nbsp;&nbsp;')
            l-=1
        fout.write('<br>')
        print 'OK03'

        print inver
        print '\n'
        print '\n'

        # print title.get_text()
        # print 'title'
        #赞同数代码：<span class="count">273</span>
        #答案号代码：<a class="zg-anchor-hidden" name="answer-30358716"></a>
    #    answers = soup.find_all('div', class_="zm-item-vote-info")
        # print answers
        # print 'answers'
        # answer_urls=soup.find_all('a', class_="count")
    #
            # if en.find('K')!=-1:
            #     res_data['counts'] = en
            #     res_data['status'] = 0
            #     print "to1"
            #     break
            # if eval(en)<100:
            #     print 777
            #     print answer.get_text()
            #     continue
            # else:
            #     # print 888
            #     if(eval(en)>maxcount):
            #         maxcount=eval(en)
            #         res_data['counts'] = maxcount
            #         res_data['status'] = 1
#
        return ress

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_data1 = self._get_new_data0(page_url, soup)
        return new_data1



class Outputer(object):
    def __init__(self):
        self.datas=[]


    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout=open('result3.html','a')
        fout.write("</p>")
        fout.write('<br /><br /><p style="text-align:center">The end</p>')
        fout.write("</body>")
        fout.write("</html>")


class SpiderMain():
    def craw(self):
        fout=open('result3.html','w')
        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8"></meta>')
        fout.write("<title>电影信息爬虫结果</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h2 style="text-align:center" >电影信息爬虫结果</h2>')
        fout.write('<h3 style="text-align:center"> 2016-3-31</h3>')
        fout.write('<p style="text-align:center">Power By Bluemit</p><p style="align=center">')
        fout.close()
        while UrlManager.has_new_url():
            try:
                new_url=UrlManager.get_new_url()
                print "\n crawling "
                print new_url.decode('utf-8')
                html_cont=Downloader.download(new_url)
                print html_cont
                print "Download OK"
                new_data=Parser.parse(new_url,html_cont)
                # print 111
                Outputer.collect_data(new_data)
                time0=random.uniform(8,12);
                sleep(time0)
            except:
                print "crawl failed"
                time0=random.uniform(8,12);
                sleep(time0)
        Outputer.output_html()


if __name__=="__main__":
    print "Welcome to Movie spider"

    UrlManager = UrlManager()
    Downloader = Downloader()
    Parser = Movie_Parser()
    Outputer = Outputer()

        

    SpiderMain = SpiderMain()
    SpiderMain.craw()
    print "\nEverything is done. Result is in result.html ."