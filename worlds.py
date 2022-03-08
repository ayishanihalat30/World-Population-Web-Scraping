# -*- coding: utf-8 -*-
import scrapy


class WorldsSpider(scrapy.Spider):
    name = 'worlds'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        rows=response.xpath('//tr')

        for row in rows:
            Countries=row.xpath('./td/a/text()').get()
            Population=row.xpath('./td[3]/text()').get()
            Yearly_change=row.xpath('./td[4]/text()').get()
            Density = row.xpath('./td[6]/text()').get()
            Land_area = row.xpath('./td[7]/text()').get()
            Migrants = row.xpath('./td[8]/text()').get()
            Med_age = row.xpath('./td[10]/text()').get()
            Urban_pop = row.xpath('./td[11]/text()').get()

            yield {
            'Countries':Countries,
            'Population':Population,
            'Yearly_change':Yearly_change,
            'Density':Density,
            'Land_area':Land_area,
            'Migrants':Migrants,
            'Med_age':Med_age,
            'Urban_pop':Urban_pop,
            }
