import scrapy
from sreality.items import Flat


class FlatsSellSpider(scrapy.Spider):
    name = "flatsSell"
    headers = {'User-Agent': 'Googlebot'}

    def start_requests(self):
        url = "https://www.sreality.cz/hledani/prodej/byty"
        headers = {'User-Agent': 'facebot'}

        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        div_elements = response.xpath('//div[contains(@class, "dir-property-list")]/div[contains(@class, "property")]')

        flat = Flat()
        for div_element in div_elements:
            img_element = div_element.xpath('.//img[1]')
            span_element = div_element.xpath('.//span[contains(@class, "name")]')

            img_url = img_element.attrib.get('src') if img_element else ""
            title = span_element.xpath('string()').get().strip() if span_element else ""

            flat['title'] = title
            flat['img_url'] = img_url
            yield flat
