
"""

This is where the template for XPATH for different items on website:
in this example template we are crawling each article for http://www.bbc.com/

"""

class XpathTemplate(object):
	
	#	this defines the xpath for locating the next page of
	#	the succeeding article
	#	
	#	next_page_regex - locates the path with the specified <wildcard>
	#	next_page_tmp - locates the links that are related to the current page
	#

	next_page_regex = "/news/"
	next_page_tmp = "//a/@href"

	#
	#	this defines the xpath template the whole news articles
	#	xpath query for each website would vary depending on the html template
	#	template should be followed depending on the root:domain

	#	eg.
	#	<attribute_name> = "<xpath_query"
	#

	article_link = ".//h1[@class=\"story-body__h1\"]/text()"	
	headline = ".//h1[@class=\"story-body__h1\"]/text()"
	author = ""

	content = "//div[@class=\"column--primary\"]/div[@class=\"story-body\"]/\
		div[@property=\"articleBody\"]/p/text()"
	
	date = "//div[@class=\"column--primary\"]/div[@class=\"story-body\"]\
		/div[@class=\"with-extracted-share-icons\"]/div[@class=\"story-body__mini-info-list-and-share\"]\
		/div[@class=\"story-body__mini-info-list-and-share-row\"]/div[@class=\"mini-info-list-wrap\"]\
		/ul[@class=\"mini-info-list\"]/li[@class=\"mini-info-list__item\"]/div[@class=\"date date--v2\"]/text()"

	category = "//div[@class=\"site-brand site-brand--height\"]\
		/div[@class=\"secondary-navigation secondary-navigation--wide\"]\
		/nav[@class=\"navigation-wide-list navigation-wide-list--secondary\"]/a/span/text()"