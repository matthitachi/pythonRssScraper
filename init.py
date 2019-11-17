from xmlparser import Xmlparser
from scrapermodel import scraper
from Logger import logger
# scraper = scraper
xmlparser = Xmlparser()
logger = logger('init_rss.log')

get_all_work = xmlparser.get_scraper_config('config.xml')

def scrape_Rss_Links(links, scrapedata):
    global scraper
    for link in links:
        value = link.text
        logger.info(value)
        scraper_obj = scraper(value, scrapedata, 'init_rss.log')
        # print(scrapedata)
        if(scraper_obj.db.articleExist(value)):
            # print(scraper_obj.get_data())
            continue
        else:
            scraper_obj.get_data()

            # print(scraper_obj.get_data())


for scraperdata in get_all_work :
    config_scraper_data = xmlparser.sort_scraper_data(scraperdata)
    scrapedata = config_scraper_data['scrape']
    rss_link = config_scraper_data['link']
    rss_xml = xmlparser.get_rss(rss_link)
    scrape_Rss_Links(rss_xml, config_scraper_data)
