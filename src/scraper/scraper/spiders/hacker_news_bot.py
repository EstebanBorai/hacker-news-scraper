import scrapy

class HackerNewsBotSpider(scrapy.Spider):
    name = 'hacker_news_bot'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        titles = response.css('.title .storylink::text').extract()
        ranks = response.css('.rank::text').extract()
        scores = response.css('.subtext .score::text').extract()
        users = response.css('.hnuser::text').extract()
        times = response.css('.age::attr(title)').extract()
        domain = response.css('.sitestr::text').extract()

        for item in zip(titles, ranks, scores, users, times, domain):
            self.results.append({
                'title': item[0],
                'rank': item[1],
                'score': item[2],
                'user': item[3],
                'time': item[4],
                'domain': item[5],
            })

        return True
