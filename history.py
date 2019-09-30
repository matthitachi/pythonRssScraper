from xmlparser import Xmlparser
from scrapermodel import scraper
# scraper = scraper
xmlparser = Xmlparser()

get_all_work = xmlparser.get_scraper_config('config.xml')

for scraperdata in get_all_work :
    config_scraper_data = xmlparser.sort_scraper_data(scraperdata)
    if(config_scraper_data['history']):
        scrapedata = config_scraper_data['scrape']
        rss_link = config_scraper_data['link']
        rss_xml = xmlparser.get_rss(rss_link)
    # scrape_Rss_Links(rss_xml, config_scraper_data)