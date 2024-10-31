# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import json

from .items import QuoteparsingItem


class QuoteparsingPipeline:
    def process_item(self, item: QuoteparsingItem, spider):  # default method
        # calling dumps to create json data.
        line = "," if self.printcomma else ""
        line = line + json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.printcomma = True
        # converting item to dict above, since dumps only intakes dict.
        self.file.write(line)  # writing content in output file.
        return item

    def open_spider(self, spider):
        self.file = open("result.json", "w", encoding="utf8")
        self.file.write("[\n")
        self.printcomma = False

    def close_spider(self, spider):
        self.file.write("]\n")
        self.file.close()
