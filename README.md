<div>
  <h1 align="center">hacker-news-scraper</h1>
  <h4 align="center">
    A example web scraper for Hacker News exposed through a REST API
  </h4>
</div>

## Production

```bash
docker image build -t hacker-news-scrapper .
```

```bash
docker run -d -p 5000:5000 hacker-news-scrapper
```

## Development

### Execute

```bash
docker-compose -f ./docker-compose.dev.yml up --build
```

Then visit:

```
http://0.0.0.0:5000
```

### Shutdown

Focus the terminal where the session is running and excute `Ctrl + C`.
Then execute:

```bash
docker-compose -f ./docker-compose.dev.yml down
```

### HTTP Server

An HTTP Server acts as the interface to consume this application.
Endpoints are enumerated in the following table:

Method | URI | Description
--- | --- | ---
`GET` | `/crawl` | Executes the `HackerNewsBotSpider` and retrieves the state
`GET` | `/results` | Retrieves the results from the `/crawl` process if available
`GET` | `/context` | Retrieves the current state for relevant values

In order to execute any of these HTTP requests you must first follow the
[Execute](#execute) section and an HTTP client such as _cURL_.

Example of a cURL call to this API while running.

```bash
curl http://0.0.0.0:5000/crawl
```

### Scraper

Scrapy is used as _web crawler_/_scraper_ solution to retrieve posts from
Hacker News in this project.

The _Scrapy_ project is stored under `src/scraper` and contains the:
`HackerNewsBotSpider`.

In order to use _Scrapy_ shell you must [execute the docker-compose](#execute)
and use `docker exec` to SSH into the running container.

1. Execute `docker ps` to gather container details

```bash
docker ps
```

2. Copy the relevant `CONTAINER ID` to your clipboard

3. Execute `docker exec -it <CONTAINER ID> bash`

> At this point you will be using the container's BASH instance.

4. Change directory to `src/scraper` and then execute the _Scrapy_ shell

```bash
scrapy shell
```

With the Scrapy shell you will be able to debug and test CSS selectors to
gather data from the website in question.

### Running _Scrapy_ Spider

As mentioned above, a `HackerNewsBotSpider` is available, the purpose of this
spider is to retrieve post details from Hacker News.

Following the ["Scraper" instructions](#scraper) to the third step, run

```bash
scrapy crawl hacker_news_bot
```

instead of:

```bash
scrapy shell
```

To have the bot executed. This command should output the scraped data as part of
the debug output in the terminal.

### Dependencies

- **Flask**: Lightweight WSGI (Web Server Gateway Interface) web application
framework
- **crochet**: Makes it easier to use Twisted from regular blocking code
- **Scrapy**: DOM Scraper useful for crawling the web
- **Twisted**: Multi-purpose event based framework

