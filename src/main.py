import crochet
crochet.setup()

import json

from flask import Flask
from scrapy.crawler import CrawlerRunner
from scraper.scraper.spiders.hacker_news_bot import HackerNewsBotSpider

app = Flask('Hacker News Scraper')
crawl_runner = CrawlerRunner()
results = []
scrape_in_progress = False
scrape_complete = False

@app.route('/crawl')
def crawl_posts():
  """
  Crawl for posts in Hacker News
  """
  global scrape_in_progress
  global scrape_complete

  if not scrape_in_progress:
    scrape_in_progress = True
    global results

    if len(results) > 0:
      results = []

    scrape_with_crochet(results)
    return 'Initialized a new scrape process'

  if scrape_complete:
    return 'Scrape completed'

  return 'Scrape process already initialized'

@app.route('/results')
def get_results():
  """
  Retrieves the `results` array contents if the
  spider have completed
  """
  global scrape_complete
  global results

  if scrape_complete:
    return json.dumps(results)

  return 'Scrape process still running'

@app.route('/context')
def get_context():
  """
  Retrieves current application context for debugging
  purposes
  """
  global results
  global scrape_in_progress
  global scrape_complete

  return json.dumps({
    'results': results,
    'scrape_in_progress': scrape_in_progress,
    'scrape_complete': scrape_complete,
  })

def finished_scrape(null):
  """
  A callback executed after scrape has completed.
  """

  global scrape_complete
  global scrape_in_progress

  scrape_complete = True
  scrape_in_progress = False

@crochet.run_in_reactor
def scrape_with_crochet(_results):
  eventual = crawl_runner.crawl(HackerNewsBotSpider, results=_results)
  eventual.addCallback(finished_scrape)

if __name__ == '__main__':
  app.run('0.0.0.0', 5000)
