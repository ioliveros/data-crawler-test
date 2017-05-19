# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WebspiderBotItem(scrapy.Item):

    # define the fields for your item here like:    
	domain = scrapy.Field()
	article_link = scrapy.Field()
	author = scrapy.Field()
	headline = scrapy.Field()
	content = scrapy.Field()
	date = scrapy.Field()
	category = scrapy.Field()