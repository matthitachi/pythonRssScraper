from xmlparser import Xmlparser
from pdbmodel import PdbModel
from scrapermodel import scraper
from maya import Maya
from bs4 import BeautifulSoup
import lxml
# scraper = scraper
xmlparser = Xmlparser()
# db = PdbModel('atscraper')

# Get scraperconfig for this site
get_config = xmlparser.get_scraper_config('config.xml')
db_config = xmlparser.get_db_config('config.xml')
db = PdbModel(db_config.get("database"))
globes_config = xmlparser.sort_scraper_data(get_config[1])

url = "https://maya.tase.co.il/reports/company?q=%7B%22DateFrom%22:%222018-11-14T22:00:00.000Z%22,%22DateTo%22:%222019-11-14T21:00:00.000Z%22,%22Page%22:1,%22entity%22:373,%22events%22:%5B%5D,%22subevents%22:%5B%5D,%22IsBreakingAnnouncement%22:true%7D"

sql = 'Select corp_id from securities'
allInstrumenIDs = db.fetchall(sql)
for insID in allInstrumenIDs :
    instrumentId =insID[0]
    # print(insID[1])
    history_url = "https://maya.tase.co.il/reports/company?q=%7B%22DateFrom%22:%222018-11-14T22:00:00.000Z%22,%22DateTo%22:%222019-11-14T21:00:00.000Z%22,%22Page%22:1,%22entity%22:"+str(instrumentId)+",%22events%22:%5B%5D,%22subevents%22:%5B%5D,%22IsBreakingAnnouncement%22:true%7D"
    print("URL: "+ history_url)
    document = scraper.get_doc(scraper, history_url)
    # document = open("C:\\Users/ITACHI\\PycharmProjects\\Atscraper\\maya_history.html", encoding="utf8").read()
    article_links = scraper.get_history_links(scraper, document, 'self.soup.select("maya-reports .feedItemMessage > a")')
    print("Records: " + str(len(article_links)))
    for at_link in article_links:
        # print(at_link['href'])
        if(at_link):
            link = "https://maya.tase.co.il/"+at_link['href']
            header = at_link.text
            print("Header and Link", header, link)
            scraper_obj = scraper('maya.html', {})
            if (scraper_obj.db.articleExist(link)):
                continue
            else:
                Maya.scrapeMaya(Maya, scraper_obj, link, header)


    break
