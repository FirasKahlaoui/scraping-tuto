import scrapy


class ExempleSpider(scrapy.Spider):
    name = "exemple"
    allowed_domains = ["exemple.com"]
    start_urls = ["https://exemple.com"]

    def parse(self, response):
        pass
