from bs4 import BeautifulSoup
import lxml
import requests
from scrapermodel import scraper
import re
from xmlparser import Xmlparser
from urllib.request import urlopen
from urllib.parse import urlparse
from pdbmodel import PdbModel
from dateutil import parser
from datetime import datetime
from maya import Maya




xmlparser = Xmlparser()

rss_link = 'https://maya.tase.co.il/rss/maya.xml'
rss_xml = xmlparser.get_rss_xml('maya.xml')
for item in rss_xml:
    link = item.find('link').text
    header = item.find('title').text.split('-')[-1]
    scraper_obj = scraper(link, {})
    if (scraper_obj.db.articleExist(link)):
        continue
    else:
        Maya.scrapeMaya(Maya, scraper_obj, link, header)