import scrapy
from scrapy.http.response import Response

from ..items import QuoteparsingItem


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response: Response):
        quotes = response.css("div.quote")

        for q in quotes:
            item = QuoteparsingItem()
            item["quote"] = q.css("span.text::text").get()
            item["author"] = q.css("small.author::text").get()
            item["tags"] = [tag.css("::text").get() for tag in q.css("a.tag")]
            # yield {
            #     "quote": q.css("span.text::text").get(),
            #     "author": q.css("small.author::text").get(),
            #     "tags": [tag.css("::text").get() for tag in q.css("a.tag")],
            # }
            yield item

        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            next_page = "https://quotes.toscrape.com" + next_page
            yield response.follow(url=next_page, callback=self.parse)
