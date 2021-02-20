import re

import scrapy

class LawsSpider(scrapy.Spider):
    name = "laws"

    def start_requests(self):
        urls = ['http://bdlaws.minlaw.gov.bd/act-957.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        laws = response.css('p.act-section-name > a')
        for law in laws:
            law_title = law.xpath("text()").get().strip()
            law_link = law.xpath("@href").get().strip()

            print(law_title, law_link)

