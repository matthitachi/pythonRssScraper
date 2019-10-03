from xmlparser import Xmlparser
from pdbmodel import PdbModel
from scrapermodel import scraper
# scraper = scraper
xmlparser = Xmlparser()
# db = PdbModel('atscraper')



# Get scraperconfig for this site
get_config = xmlparser.get_scraper_config('config.xml')
db_config = xmlparser.get_db_config('config.xml')
db = PdbModel(db_config.get("database"))
globes_config = xmlparser.sort_scraper_data(get_config[1])
# print(globes_config)

# get all Instrumement id
sql = 'Select * from instrumentids'
allInstrumenIDs = db.fetchall(sql)
for insID in allInstrumenIDs :
    instrumentId =insID[1]
    # print(insID[1])
    history_url = "https://www.globes.co.il/portal/instrument.aspx?instrumentid="+instrumentId+"&mode=news"
    document = scraper.get_doc(scraper,history_url)
    article_links = scraper.get_history_links(scraper, document, 'self.soup.select(".mainArticletitle > a")')
    for at_link in article_links:
        # print(at_link['href'])
        if(at_link):
            scrape = scraper("https://www.globes.co.il"+at_link['href'], globes_config)
            scrape.get_data()






# get_all_work = xmlparser.get_scraper_config('config.xml')
#
# for scraperdata in get_all_work :
#     config_scraper_data = xmlparser.sort_scraper_data(scraperdata)
#     if(config_scraper_data['history']):
#         scrapedata = config_scraper_data['scrape']
#         rss_link = config_scraper_data['link']
#         rss_xml = xmlparser.get_rss(rss_link)
    # scrape_Rss_Links(rss_xml, config_scraper_data)