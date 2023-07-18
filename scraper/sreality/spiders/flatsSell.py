import scrapy
from sreality.items import Flat


class FlatsSellSpider(scrapy.Spider):
    name = "flatsSell"
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']
    item_scraped_count = 0
    items_to_scrape = 500

    def parse(self, response):
        div_elements = response.xpath('//div[contains(@class, "dir-property-list")]/div[contains(@class, "property")]')

        flat = Flat()
        for div_element in div_elements:
            if self.item_scraped_count >= self.items_to_scrape:
                return
            self.item_scraped_count += 1
            
            img_element = div_element.xpath('.//img[1]')
            span_element = div_element.xpath('.//span[contains(@class, "name")]')

            img_url = img_element.attrib.get('src') if img_element else ""
            title = span_element.xpath('string()').get().strip() if span_element else ""

            flat['title'] = title
            flat['img_url'] = img_url
            yield flat
            
        next_page = response.css('li.paging-item a.paging-next::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
