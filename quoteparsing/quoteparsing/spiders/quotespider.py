import scrapy
from scrapy.http.response import Response


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response: Response):
        quotes = response.css("div.quote")

        for q in quotes:
            yield {
                "quote": q.css("span.text::text").get(),
                "author": q.css("small.author::text").get(),
                "tags": [tag.css("::text").get() for tag in q.css("a.tag")],
            }

        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            next_page = "https://quotes.toscrape.com" + next_page
            yield response.follow(url=next_page, callback=self.parse)
