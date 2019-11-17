from xmlparser import Xmlparser
from pdbmodel import PdbModel
from scrapermodel import scraper
import math
from Logger import logger
# scraper = scraper
xmlparser = Xmlparser()



logger = logger('catalist_history.log')
# Get scraperconfig for this site
get_config = xmlparser.get_scraper_config('config.xml')
db_config = xmlparser.get_db_config('config.xml')
db = PdbModel(db_config.get("database"), 'catalist_history.log')
globes_config = xmlparser.sort_scraper_data(get_config[2])
# print(globes_config)

# get all Instrumement id
sql = 'Select sec_id from securities'
allInstrumenIDs = db.fetchall(sql)
for insID in allInstrumenIDs :
    instrumentId =insID[0]
    # print(insID[1])
    history_xml = "https://www.calcalist.co.il/Ext/Comp/Allday/CdaStockNews_Xml/0,15250,L-"+instrumentId+"-1-0-1-249,00.xml"
    # https: // www.calcalist.co.il / Ext / Comp / Allday / CdaStockNews_Xml / 0, 15250, L - 604611 - 1 - 0 - 71 - 353, 0
    # history_url = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-"+instrumentId+"--4,00.html"
    logger.info(history_xml)
    document = scraper.get_doc(scraper, history_xml)
    doc = xmlparser.get_any_xml(document)
    total_at = int(xmlparser.get_xml_find(doc, 'total').text)
    total_pages = math.ceil(total_at/30)
    logger.info(total_pages)
    for i in range(1, int(total_pages)):
        start_document = xmlparser.get_any_xml(scraper.get_doc(scraper, "https://www.calcalist.co.il/Ext/Comp/Allday/CdaStockNews_Xml/0,15250,L-"+instrumentId+"-1-0-"+str(i)+"-249,00.xml"))

        items = xmlparser.get_xml_find_all(start_document, "Item/link")
        # print(items)
        if (items):
            for item in items:
                link = "https://www.calcalist.co.il"+item.text
                print(link)
                scrape = scraper("https://www.calcalist.co.il"+item.text, globes_config, 'catalist_history.log')
                scrape.get_data()







