import scrapy
import logging
from webspider_bot.items import WebspiderBotItem
from webspider_bot import settings
from webspider_bot.mongo_connector import fetch_article_link
from webspider_bot.xpath_template import XpathTemplate

class CrawlArticle(scrapy.Spider):

	name = 'crawl-article'		
		
	def __init__(self, name=None, **kwargs):
	
		self.start_urls = []
		if 'start_urls' in kwargs:
			self.start_urls = kwargs.pop('start_urls').split(',')
	
		self.allowed_domain = []
		if 'allowed_domain' in kwargs:
			self.allowed_domain = kwargs.pop('allowed_domain').split(',')

		super(CrawlArticle, self).__init__(name, **kwargs)
		self.crawl_count = 0
	
	def parse(self, response):
	
		if self.allowed_domain and self.start_urls:

			# this will check first if links is already scraped
			# if true skip saving content and proceed
			# to the next page
			
			scraped_links = fetch_article_link()
			if response.url not in scraped_links:
								
				# this will check first if article is valid
				# if true it will call the pipeline and store the data to MongoDB 				

				item = WebspiderBotItem()		
				item['article_link'] = response.url
				item['headline'] = self._get_headline(response,xpath_tmp=XpathTemplate.headline)
				item['content'] = self._get_contents(response,xpath_tmp=XpathTemplate.content)									

				if item['content'] and item['headline']:		

					# if article is valid save to mongoDB
					item['author'] = self._get_author(response)
					item['category'] = self._get_category(response,xpath_tmp=XpathTemplate.category)			
					item['date'] = self._get_date_time(response,xpath_tmp=XpathTemplate.date)						

					self.crawl_count += 1
					print("SAVING NEW ARTICLE : {0} : COUNT : {1}".format(response.url,self.crawl_count))
					yield item

			
			# crawler will proceed to next page until the system Keyboard interrupt	or
			# bandwidth exceeds limit or all related links are crawled			

			next_page = response.xpath(XpathTemplate.next_page_tmp).extract()				
			if next_page:
				for url in next_page:
					if not url.startswith(XpathTemplate.next_page_regex): continue	
					next_page_url = self.allowed_domain[0] + url
					request = scrapy.Request(url=next_page_url)
					yield request

		else:
			logging.warning("Please specific allowed_domain & start_urls eg. scrapy crawl <spider_name> -a <value=name> ")


	def _get_author(self, response, xpath_tmp=None):		
		if not xpath_tmp: return 
		return response.xpath(xpath_tmp).extract_first()

	def _get_headline(self, response, xpath_tmp=None):
		if not xpath_tmp: return 
		return response.xpath(xpath_tmp).extract_first()

	def _get_contents(self, response, xpath_tmp=None):
		if not xpath_tmp: return 
		line_arr = [line for line in response.xpath(xpath_tmp).extract() if line]		
		return "\n".join(line_arr)

	def _get_date_time(self, response, xpath_tmp=None):
		if not xpath_tmp: return 
		return response.xpath(xpath_tmp).extract_first()

	def _get_category(self, response, xpath_tmp=None):
		if not xpath_tmp: return 
		return response.xpath(xpath_tmp).extract_first()