# -*- coding: utf-8 -*-
from bookstore.items import BookstoreItem

__author__ = 'khainguyen'
import scrapy


class Bookbuy(scrapy.Spider):
    name = "bookbuy"
    allowed_domains = ["bookbuy.vn"]
    start_urls = [
        'http://bookbuy.vn/sach-hay-nen-doc/p1'
    ]

    def parse(self, response):
        for url in response.xpath('//div[@class="product-item"]//div[@class="t-view"]/a/@href').extract():
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_data)
        next_page = response.xpath(
            '//li[@class="PagedList-skipToNext"]/a/@href').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
    def parse_data(self,response):
        item = BookstoreItem()
        item['book_name'] = response.xpath('//h1[@itemprop="name"]/text()').extract_first('').strip()
        item['price'] = response.xpath('//div[@itemprop="price"]/text()').extract_first('').strip()
        item['thumbnail'] = response.urljoin(response.xpath('//img[@class="product-zoom slimmage"]/@src').extract_first('').strip())
        item['description'] = response.xpath('string(//div[@itemprop="description"])').extract_first('').strip()
        item['author'] = response.xpath('string(//div[@class="author-list"])').extract_first('').strip()
        return item
