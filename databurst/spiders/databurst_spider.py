import scrapy
# import logging.config
from scrapy.loader import ItemLoader
from databurst.items import DataburstItem
from databurst.helper.enum import SpiderInfo


# logging.config.fileConfig('databurst/config/log/config.toml')
# logger = logging.getLogger(__name__)

class DataburstSpider(scrapy.Spider):
    """
    A Scrapy spider for scraping data from web pages using XPath selectors.
    It extracts text content from specific elements on the page and stores it in a DataburstItem.

    Attributes:
        name (str): The name of the spider.
        start_urls (list of str): A list of URLs to start crawling.

    Methods:
        parse(response): The main method that handles the response received from the start URLs.
    """
    name = SpiderInfo.NAME.value
    start_urls = SpiderInfo.START_URLS.value
    
    def parse(self, response):
        """
        Parse the response received from the start URLs.
        Extracts data from the response using XPath selectors and stores it in a DataburstItem.
        
        Args:
            response: The response received from the start URLs.

        Yields:
            DataburstItem: An item containing the extracted data.
        """
        # logger.info("Parsing Is Started ...")
        elements = response.xpath(SpiderInfo.PATH.value)
        for element in elements:
            loader = ItemLoader(item=DataburstItem(), selector=element)
            loader.add_xpath('text_content', 'string()')
            yield loader.load_item()