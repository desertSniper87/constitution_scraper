import re

import scrapy

class LawsSpider(scrapy.Spider):
    BASE_URL = 'http://bdlaws.minlaw.gov.bd'
    name = "laws"

    def start_requests(self):
        urls = [ self.BASE_URL + '/act-957.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        laws = response.css('p.act-section-name > a')
        for law in laws:
            law_title = law.xpath("text()").get().strip()
            law_link = law.xpath("@href").get().strip()

            law_url = self.BASE_URL + law_link
            law_description = self.parse_subpage(law_url)


            print(law_title, law_link)

    def parse_subpage(self, page_url):
        pass

