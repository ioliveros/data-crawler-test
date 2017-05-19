# *********************
#  data-crawler-test 
# *********************

This is a simple solution for the Data-Engineer Test from Isentia

A simple spider crawler that utilizes the scrapy framework and crawls for articles from a news website, cleanses the response, stores in a mongo database then makes it available to search via an API.

# INSTALLING DEPENDENCIES

	1. pip install virtualenv
	(note: make sure that pip is installed)

	2. create amd activate virtualenv:
		
		>> virtualenv --no-site-packages <name_of_folder>

		WINDOWS:
		>> <name_of_folder>\Scripts\activate
		
		LINUX:
		>> source <name_of_folder>/bin/activate

		>> pip install -r requirements.txt 


# This application meets and solves the following:


- It is primarily built on Python and scrapes for - www.bbc.com (as a resource for demo purposes) - 
   this can be changed by adding the correct xpath queries on xpath_template.py

- Scrapes for the following content related the ff. attribute:

	(domain, article_link, author, headline, content, date, category)

	this can be extended by adding the proper xpath queries on webspider_bot/xpath_template.py and additional 
	attributes on /spiders/items.py

- Collected contents are stored on MongoDB and hosted at compose.io

To run the webspider bot user:

	python testrun.py "http://www.bbc.com/" "http://www.bbc.com/"

To test the API:

	run:

		python run_app.py

	- there are two methods to check the api commands 

		1. via command line on (cmd or shell terminal)
			eg. python run_api.py search <key_word>

		2. using browser to fetch via http request:
			eg. http://localhost:5000/search/<key_word>

	Note: flask should be installed in order for this to work (you can refer to the installing dependencies section)
