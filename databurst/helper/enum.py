from enum import Enum


class SpiderInfo(Enum):
    """
    Enum class that holds information about the spider.

    Enum Values:
        NAME (str): The name of the spider.
        START_URLS (list of str): A list of URLs to start crawling.
        FILE_NAME (str): CSV file name .
        PATH (str): The XPath selector to select specific elements from the web pages.
    """
    NAME = "databurst_spider"
    FILE_NAME = "databurst/ducs/text.csv"
    START_URLS = ["https://databurst.ir"]
    PATH = '//*[(@id = "features")]//*[contains(concat( " ", @class, " " ), concat( " ", "text-base", " " )) and contains(concat( " ", @class, " " ), concat( " ", "text-gray-500", " " ))]'