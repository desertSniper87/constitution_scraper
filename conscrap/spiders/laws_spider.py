import scrapy

class LawsSpider(scrapy.Spider):
    name = "laws"

    def start_requests(self):
        urls = ['http://bdlaws.minlaw.gov.bd/act-957.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
