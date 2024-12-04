# Monprojet

Monprojet is a web scraping project built using Scrapy. It includes spiders to scrape data from various websites.

## Project Structure

```plaintext
monprojet/
    __init__.py
    pycache/
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        pycache/
        exemple.py
        quotes_spider.py
    quotes.json
README.md
scrapy.cfg
```

## Spiders

### Exemple Spider

The `ExempleSpider` is defined in [monprojet/spiders/exemple.py](monprojet/spiders/exemple.py). It scrapes data from `exemple.com`.

### Quotes Spider

The `QuotesSpider` is defined in [monprojet/spiders/quotes_spider.py](monprojet/spiders/quotes_spider.py). It scrapes quotes from `quotes.toscrape.com`.

## Middleware

The project includes custom middleware defined in [monprojet/middlewares.py](monprojet/middlewares.py):

- `MonprojetSpiderMiddleware`
- `MonprojetDownloaderMiddleware`

## Pipelines

The project includes an item pipeline defined in [monprojet/pipelines.py](monprojet/pipelines.py):

- `MonprojetPipeline`

## Settings

The project settings are configured in [monprojet/settings.py](monprojet/settings.py). Key settings include:

- `BOT_NAME`
- `SPIDER_MODULES`
- `NEWSPIDER_MODULE`
- `ROBOTSTXT_OBEY`

## Running the Spiders

To run a spider, use the following command:

```sh
scrapy crawl <spider_name>
```

For example, to run the quotes_spider, use:

```sh
scrapy crawl quotes_spider
```

The scraped data is saved in `quotes.json`.
