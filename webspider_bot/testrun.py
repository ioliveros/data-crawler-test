import sys
import os

"""
This is a simple implementation of scrapy that serves as a simplified wrapper for running the crawler via
command line using sys.argv 

there are two commands:

	<domain>		- root domain of the crawler
	<start_urls> 	- starting point url where the crawler will start scraping content

eg:

	python app.py <domain> <start_urls>
	scrapy crawl crawl-article -a start_urls="http://www.bbc.com" -a allowed_domain="http://www.bbc.com"
	scrapy crawl crawl-article -s LOG_ENABLED=False

"""

if __name__ == '__main__':
	try:
		domain = sys.argv[1]
		start_urls = sys.argv[2]
		command = "scrapy crawl crawl-article -a start_urls={0} -a allowed_domain={1} -s LOG_ENABLED=False".format(domain,start_urls)
		os.system(command)
	except KeyboardInterrupt as e:
		print('exiting crawler')