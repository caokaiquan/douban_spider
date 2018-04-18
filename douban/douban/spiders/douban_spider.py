# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import DoubanItem




class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/26853356/comments/']

    def parse(self, response):
        jpy = PyQuery(response.text)
        print('resonse.status_code')
        for i in jpy('#comments > ul:nth-child(1) > li').items():
            item = DoubanItem()
            item['comment'] = i('div.comment > p.comment-content').text()
            yield item

        #翻页
        next_page = jpy('#content > div > div.article > div > div.paginator-wrapper > ul > li:nth-child(3) > a').attr('href')
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)




