import csv
import scrapy
# import logging.config
from scrapy.loader import ItemLoader
from databurst.items import DataburstItem
from databurst.helper.enum import SpiderInfo
from databurst.helper.messages import CsvMessage


# logging.config.fileConfig('databurst/config/log/config.toml')
# logger = logging.getLogger(__name__)

class DataburstSpider(scrapy.Spider):
    """
    A Scrapy spider for scraping data and writing it to a CSV file.

    Attributes:
        name (str): The name of the spider.
        start_urls (list): A list of URLs to start the spider's crawling process.
        file_name (str): The name of the CSV file.
    """
    name = SpiderInfo.NAME.value
    start_urls = SpiderInfo.START_URLS.value
    file_name = SpiderInfo.FILE_NAME.value
    
    def parse(self, response):
        """
        Parse the response and extract data from the web page.

        Args:
            response: The response received from the web page.

        Raises:
            csv.Error: If an error occurs while writing to the CSV file.
        """
        # logger.info("Parsing Is Started ...")
        elements = response.xpath(SpiderInfo.PATH.value)
        for element in elements:
            loader = ItemLoader(item=DataburstItem(), selector=element)
            loader.add_xpath('text_content', 'string()')
            yield loader.load_item()
            try:
                with open(self.file_name, 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(loader.get_collected_values('text_content'))
            except csv.Error:
                print(CsvMessage.CSV_ERROR)