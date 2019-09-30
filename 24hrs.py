from xmlparser import Xmlparser
from pdbmodel import PdbModel
from scrapermodel import scraper

config_map = {'www.themarker.com': 0, 'www.bizportal.co.il': 3, 'www.calcalist.co.il': 2, 'www.globes.co.il': 1}

sql = """SELECT website, url
FROM scrapedata
WHERE created_at::date <= NOW() - INTERVAL '48 HOURS'
AND ck_feedback = '0'
ORDER BY created_at DESC"""

db = PdbModel('atscraper')
results = db.fetchall(sql)
# Get scraperconfig for this site
xmlparser = Xmlparser()
for result in results:
    get_config = xmlparser.get_scraper_config('config.xml')
    config = xmlparser.sort_scraper_data(get_config[config_map[result[0]]])
    if 'feedbacks' in config['scrape']:
        scrape = scraper(result[1], config)
        count = scrape.get_feedback_data()
        db.updateFeedback(count)
        print(scrape.get_feedback_data())


# print(result)
