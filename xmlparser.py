import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET

class Xmlparser :

    def get_rss(self, url):
        rss_xml = requests.get(url)
        root_xml = ET.fromstring(rss_xml.text)
        return root_xml.findall('channel/item/link')
        # print(root_xml.tag)
        # for type_tag in root_xml.findall('channel/item/link'):
        #     value = type_tag.text
        #     print(value)
    def get_rss_xml(self, path):
        root_xml = ET.parse(path).getroot()
        return root_xml.findall('channel/item')

    def get_scraper_config(self, path):
        config_xml = ET.parse(path).getroot()
        return config_xml.findall('scraper/item')

    def sort_scraper_data(self, data):
        check = {}
        rss_link = data.find('link').text
        instrumentid = data.find('instrumentid').text
        article_sec = data.find('article_sec').text
        sec_id = data.find('sec_id').text
        scraping_data = data.find('data')
        for sdata in scraping_data:
            check[sdata.tag] = sdata.text

        return {'link': rss_link, 'instrumentid': instrumentid, 'sec_id': sec_id, 'article_sec': article_sec, 'scrape': check}

    def get_db_config(self, path):
        config_xml = ET.parse(path).getroot()
        db_congig =  config_xml.find('database')
        username = db_congig.find('user').text
        password = db_congig.find('password').text
        host = db_congig.find('host').text
        port = db_congig.find('port').text
        database = db_congig.find('database').text
        return {"user": username, "password":password, "host":host, "port":port, "database":database}

    def get_feedback_scrapeData(self, scrapedata):
        return scrapedata.find('feedbacks')

    def get_any_xml(self, text):
        root_xml = ET.fromstring(text)
        return root_xml

    def get_xml_find(self, doc, path):
       return doc.find(path)

    def get_xml_find_all(self,doc, path):
        return doc.findall(path)

# print(Xmlparser.get_db_config(Xmlparser,'config.xml'))