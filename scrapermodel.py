import os

from bs4 import BeautifulSoup
import lxml
import requests
import re
from xmlparser import Xmlparser
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from pdbmodel import PdbModel
from dateutil import parser
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from Logger import logger

class scraper:
    def __init__(self, url, scrapedata, logfile=None):
        self.scrapedata = scrapedata
        self.url = url
        doc = self.get_doc(url)
        self.soup = BeautifulSoup(doc, 'lxml')
        xmlparser = Xmlparser()
        db_config = xmlparser.get_db_config('config.xml')
        self.db = PdbModel(db_config.get("database"), logfile)
        self.logger = logger(logfile)
        # print(self.gerUrlSec_id())
        # print(eval('self.soup.find(itemprop="headline").text'))
        # print(eval('self.soup.find(itemprop="description").text'))
        # print(eval('self.soup.find(rel="author").text'))
        # print(eval('self.soup.find("time", itemprop="datePublished").text'))
        # print(len(eval('self.soup.select("ol > li[role=article]")')))
    def selenium_get_doc(self, link, proxy=None):
        # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        if proxy:
            options.add_argument('--proxy-server = %s' % proxy)
        driver = webdriver.Chrome(ChromeDriverManager().install(),  chrome_options=options)
        driver.get(link)
        page_source =driver.page_source
        driver.close()
        return page_source


    def test(self):
      # print(eval('re.findall(r"[\w\.-]+@[\w\.-]+", self.soup.select("div.articleInfo > a")[0]["href"])[0]'))
      return eval("self.soup.find_all('a', href=re.compile('/stocks/home/0,7340,L-3959-(.*?)'))")
      # print(eval('(self.soup.select("div.articleInfo > a")) and self.soup.select("div.articleInfo > a")[0].text or self.soup.select_one("div.articleInfo > span").text'))
      # print(eval('self.soup.select("div.articleInfo > a")[0].text'))
      # print(eval('self.soup.find("span", class_="tb-counter adom ShualBold")'))
      # print(eval('self.soup.select("time > span")[0].text'))
      # print(eval('self.soup.select("time > span")[1].text'))
      # print(eval('eval(self.soup.find("span", class_="count").text)'))
      # print(eval('self.soup.find("span", class_="count").text'))
      # print(eval('self.soup.select_one("div.articleInfo > span").text'))
      # print(eval('re.findall(r"[\w\.-]+@[\w\.-]+", self.soup.select("div.art-launch-date > a")[0]["href"])[0]'))
      # print(eval('self.soup.find("time", itemprop="datePublished").text'))
    # print(len(eval('self.soup.select("ol > li[role=article]")')))

    def trystuff(self):
        print(eval('(1, 2)')[0])

    def get_doc(self, url, proxy=None):
        if proxy:
            proxies = {'http': 'http://%s' %proxy}
            proxy_support = urllib.request.ProxyHandler(proxies)
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            html = urlopen(url)
        else:
            html = urlopen(url)
        return html.read()
        # return requests.get(url).text

    def get_feedback_data(self):
        try:
            result = eval(self.scrapedata['scrape']['feedbacks'])
        except AttributeError:
            result = 0
        except Exception:
            result = 0
        return result

    def find_secid(self, code, sec):
        # chec = self.soup.find_all('a', href=re.compile('https://finance\.themarker\.com/quote/\?mador=1&documentId=(.*?)'))
        result = eval(code)
        # print(result)
        alltags = []
        # alltags.append(self.gerUrlSec_id())
        # links = [re.findall(r""+sec+"", str(a))[0] for a in result]
        # chec = re.findall(r"https://finance\.themarker\.com/quote/\?mador=1\&amp;documentId=(.*?)?\"", '<a data-mador-id="1" data-section-id="" href="https://finance.themarker.com/quote/?mador=1&amp;documentId=1131523" target="_blank">מגדלי הים התיכון</a>')
        # chec = re.findall(r"https://finance\.themarker\.com/quote/\?mador=1\&amp;documentId=(.*?)?\"", str(chec[0]))
        # return links
        for a in result:
            # print(str(a))
            chec = re.findall(r""+sec+"", str(a))

            chec = self.checkInstrumentID(chec)
            # if (int(self.scrapedata['instrumentid'])):
                # print("Check for Instrument ID", self.scrapedata['instrumentid'])
                # chec = self.db.sortInstrumentId(chec[0])
            if(chec):
                alltags.append(chec[0])

        alltags = list( dict.fromkeys(alltags) )
        self.logger.info('TAGS ==>'+ str(alltags))
        return alltags

        # print(chec)
    def checkInstrumentID(self, id):
        if (int(self.scrapedata['instrumentid'])):
            # print("Check for Instrument ID", self.scrapedata['instrumentid'])
            id = self.db.sortInstrumentId(id[0])
        return id

    def gerUrlSec_id(self):
        sec_id = eval(self.scrapedata['article_sec'])

        self.logger.info('secid' + str(self.url))
        self.logger.info('secid' + str(sec_id))
        # sec_id = self.checkInstrumentID(sec_id[0])
        # print(sec_id)
        # return  sec_id[0]
    def test_secid(self):
        chec = self.soup.find_all(onclick=re.compile("document.location.href='/capitalmarket/quote/generalview/(.*?)'"))
        chec = re.findall(r"document.location.href='/capitalmarket/quote/generalview/(.*?)?'", str(chec[0]))
        self.logger.info(chec)

    def get_data(self):
        if self.db.articleExist(self.url):
            return
        else :
            data_text = {}
            # print(self.scrapedata['scrape'])

            # if(1):
            for i in self.scrapedata['scrape']:
                try:
                    tag = i
                    text = self.scrapedata['scrape'][i]
                    result = {}
                    if (tag == 'tag'):
                        res = self.find_secid(text, self.scrapedata['sec_id'])


                    elif (tag == 'feedback'):
                       res = len(eval(text))
                    else:
                        res = eval(text)

                    data_text[tag] = res
                except AttributeError:
                    data_text[tag] = None
                except Exception:
                    data_text[tag] = None
            # print(data_text)
            self.compute(data_text)

    def get_history_links(self, doc, code):
        self.soup = BeautifulSoup(doc, 'lxml')
        return eval(code)

    def validateAllData(self, data):
        for i in data:
            if(data[i]) :
                return 1

        return None
    def searchSecurities(self, dbData):
        data = dbData.copy()
        sql = 'Select * from securities'
        allSecurities = self.db.fetchall(sql)
        for sID in allSecurities:
            secId = sID[0]
            secName = sID[1]
            keywords = self.soup.find_all(string=re.compile(re.escape(secName)))
            if len(keywords) > 0:
                for keyword in keywords:
                    data['secId'] = secId
                    data['keyword'] = keyword
                    # print(secId, keyword, "second")
                    self.db.createAlert(data)

    def compute(self, data):
        # print(data)
        #{'link': 'https://www.bizportal.co.il/shukhahon/messRss2.xml', 'instrumentid': '0', 'sec_id': "document.location.href='/capitalmarket/quote/generalview/(.*?)?'", 'scrape': {'header': 'self.soup.find("h1", itemprop="headline").text', 'sub-header': 'self.soup.find("div", itemprop="description").text', 'writer_name': 'self.soup.select_one("address > a > span[itemprop=\\\'name\\\']").text', 'date': 'self.soup.select("time > span")[0].text', 'time': 'self.soup.select("time > span")[1].text', 'feedbacks': 'eval(self.soup.find("span", class_="count").text)', 'tag': 'self.soup.find_all(onclick=re.compile("document.location.href=\'/capitalmarket/quote/generalview/(.*?)\'"))'}}
        dbData = {}
        # url = self.scrapedata['link']
        url = self.url
        # parsed_uri = urlparse('url')
        website = url.split("://")[1].split("/")[0]
        dbData['url'] = url
        dbData['website'] = website
        # dateobj = datetime.now()
        secondsSinceEpoch = time.time()
        dateobj = time.localtime(secondsSinceEpoch)
        dbData['created_at'] = str('%d-%d-%d %d:%d:%d' % (
dateobj.tm_year, dateobj.tm_mon, dateobj.tm_mday, dateobj.tm_hour, dateobj.tm_min, dateobj.tm_sec))
        tags = []
        if(self.validateAllData(data)):
            for i in data:
                if(i == 'tag'):
                    dbData['sec_id'] = str(len(data[i]))
                    tags = data[i]
                elif(i == 'date'):
                    if 'time' in data.keys():
                        dt = parser.parse(data[i],dayfirst=True)
                        date = dt.date()
                        times = dt.time()
                        dbData['date'] = str(date)
                        dbData['time'] = str(times)
                    else:
                        try:
                            dbData['date'] =  str(parser.parse(data[i],dayfirst=True))
                        except Exception:
                            dbData['date'] = str(None)
                else:
                    dbData[i] = str(data[i])
        if len(tags) == 0:
            self.searchSecurities(dbData)
        self.db.insertScrapeData(dbData, tags)

    def testParser(self, dt):
        return str(parser.parse(dt,dayfirst=True))




# scrap = scraper('http://www.bizportal.co.il/shukhahon/biznews02.shtml?mid=767561',{})
# print(scrap.soup.prettify())
# scrap.test()
# scrap.trystuff()
# scrap.test_secid()
# print(scrap.find_secid("self.soup.find_all('a', href=re.compile('/stocks/home/0,7340,L-3959-(.*?)'))", '/stocks/home/0,7340,L-3959-(.*?)?,'))

# scrapr = scraper('https://www.calcalist.co.il/markets/articles/0,7340,L-3771999,00.html', {})
#
# print(scrapr.selenium_get_doc('https://www.google.com'))