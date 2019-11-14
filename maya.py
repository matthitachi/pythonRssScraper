
from scrapermodel import scraper
# scraper = scraper
from bs4 import BeautifulSoup
import lxml
import requests
import re
from xmlparser import Xmlparser
from urllib.request import urlopen
from urllib.parse import urlparse
from pdbmodel import PdbModel
from dateutil import parser
from datetime import datetime

import time


class Maya():
    def __init__(self):
        xmlparser = Xmlparser()
        db_config = xmlparser.get_db_config('config.xml')
        self.pdbmodel = PdbModel(db_config.get("database"))
    def scrapeMaya(self, scraper_obj, link,  header):
        scraper_obj = scraper_obj
        soup = scraper_obj.soup
        # soup = BeautifulSoup(open("C:\\Users/ITACHI\\PycharmProjects\\Atscraper\\maya.html", encoding="utf8").read(), 'lxml')
        datetime = soup.select_one(".messageDate.ng-binding")
        date, time = None, None
        if (datetime):
            date_split = datetime.text.split()
            date = parser.parse(date_split[0])
            time = date_split[1]

        crop_ids = soup.find_all('a', href=re.compile('company/(.*)?view=reports'))
        alltags = []
        for a in crop_ids:
            # print(str(a))
            chec = re.findall(r"company/(.*)\?view=reports", str(a))
            alltags.append(chec[0])

        alltags = list(dict.fromkeys(alltags))
        print('TAGS ==>', alltags)
        self.createMayaArticle(link, header, date, time, alltags)

    def createMayaArticle(self, url, title, date=None, timee=None, tags=None):
        url = self.pdbmodel.postgres_escape_string(url)
        website = self.pdbmodel.postgres_escape_string(url.split("://")[1].split("/")[0])
        title = self.pdbmodel.postgres_escape_string(title)
        date = self.pdbmodel.postgres_escape_string(str(date))
        timee = self.pdbmodel.postgres_escape_string(timee)
        secondsSinceEpoch = time.time()
        dateobj = time.localtime(secondsSinceEpoch)
        created_at = self.pdbmodel.postgres_escape_string(str('%d-%d-%d %d:%d:%d' % (
            dateobj.tm_year, dateobj.tm_mon, dateobj.tm_mday, dateobj.tm_hour, dateobj.tm_min, dateobj.tm_sec)))
        sql = "insert into scrapedata (url, website, header, date, time, created_at)  values (%s, %s, %s, %s, %s, %s) RETURNING id"
        self.pdbmodel.execute(sql, (url, website, title, date, timee, created_at))
        self.pdbmodel.connection.commit()
        if (tags):
            # print(self.getLastInsertID())
            self.insertTagsData(self.pdbmodel.getLastInsertID(), tags)
        self.pdbmodel.close()

    def insertTagsData(self, insertId, tags):
        for tag in tags:
            if tag:
                import time
                secondsSinceEpoch = time.time()
                dateobj = time.localtime(secondsSinceEpoch)
                sec_id = self.pdbmodel.sortSecId(tag)
                sec_id = sec_id[0] if sec_id else None
                dt = str('%d-%d-%d %d:%d:%d' % (
                    dateobj.tm_year, dateobj.tm_mon, dateobj.tm_mday, dateobj.tm_hour, dateobj.tm_min, dateobj.tm_sec))
                sql = "insert into atsecdata (article_id, sec_id, created_at, crop_id) VALUES (%s, %s, %s, %s)"
                self.pdbmodel.exec(sql, (insertId, sec_id, dt, tag))









                        # scrapeMaya(pdbmodel, 'https://maya.tase.co.il/reports/details/1262734', 'The first Maya Header')