# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class QuoteparsingItem(scrapy.Item):
    # define the fields for your item here like:
    quote = Field()
    author = Field()
    tags = Field()
    pass
