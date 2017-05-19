#
# data-crawler-test
# 

# This is a simple solution for the Data-Engineer Test from Isentia
#
# A simple spider crawler that utilizes the scrapy framework and crawls for articles from a news website, cleanses the response, stores in a mongo database then makes it available to search via an API.
#
# This application meets and solves the following:

	1. Write an application to crawl an online news website, e.g. www.theguardian.com/au or www.bbc.com using the scrapy crawler framework (http://scrapy.org/) - build the application in Java, Python or Scala.

		- it is primarily build on Python and scrapes for - www.bbc.com (as a resource for demo purposes) - this can be change by adding the correct xpath queries on xpath_template.py

	2. This appliction should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html.

		- this application primarily scrapes for the following content related the ff. attribute:

			1. domain
			2. article_link
			3. author
			4. headline
			5. content
			6. date
			7. category

		this can be extended by adding the proper xpath queries on webspider_bot/xpath_template.py and additional attributes on /spiders/items.py

	3. Store the data in a hosted mongo database, e.g. compose.io/mongo, for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original.

		- the application is currently hosted on compose.io

	4. Write an API that provides access to the content in the mongo database. The user should be able to search for articles by keyword.

		- to test the api for data-crawler-test 

			eg. python test_run.py search <key_word>	