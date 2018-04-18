# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):
    def open_spider(self,spider):
        self.file = open('doubandata.txt','w',encoding='utf-8')
        print('打开文件了')


    def process_item(self, item, spider):
        self.file.write('{}\n'.format(json.dumps(dict(item),ensure_ascii=False)))
        return item

    def close_spider(self,spider):
        self.file.close()
        print('关闭文件了')