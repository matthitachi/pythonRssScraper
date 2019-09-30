from xmlparser import Xmlparser
from pdbmodel import PdbModel
from scrapermodel import scraper
import math
import json
# scraper = scraper
xmlparser = Xmlparser()
db = PdbModel('atscraper')



# Get scraperconfig for this site
get_config = xmlparser.get_scraper_config('config.xml')
globes_config = xmlparser.sort_scraper_data(get_config[3])
# print(globes_config)

# get all Instrumement id
sql = 'Select * from instrumentids'
allInstrumenIDs = db.fetchall(sql)
for insID in allInstrumenIDs :
    instrumentId =insID[2]
    # print(insID[1])
    history_xml = "https://www.bizportal.co.il/capitalmarket/quote/AjaxRequests/SectorNews_Ajax?paperId="+instrumentId
    # https: // www.calcalist.co.il / Ext / Comp / Allday / CdaStockNews_Xml / 0, 15250, L - 604611 - 1 - 0 - 71 - 353, 0
    # history_url = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-"+instrumentId+"--4,00.html"
    document = scraper.get_doc(scraper, history_xml)
    doc = json.loads(document)
    # print(doc['Total'])
    total_at = int(doc['Total'])
    pagesize = 50
    take = 50
    # skip = 0
    total_pages = math.ceil(total_at/pagesize)
    # print(total_pages)
    for i in range(0, int(total_pages)):
        skip = take*i
        start_document = json.loads(scraper.get_doc(scraper, "https://www.bizportal.co.il/capitalmarket/quote/AjaxRequests/SectorNews_Ajax?paperId=%s&take=%s&skip=%s&page=%s&pageSize=%s" % (instrumentId, take, skip, i+1, pagesize)))

    #
        items = start_document['Data']
    #     # print(items)
        if (items):
            for item in items:
                link = item['ArticleLink']
                # print(link)
                scrape = scraper(link, globes_config)
                scrape.get_data()
    #
    #





