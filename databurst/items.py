import scrapy


class DataburstItem(scrapy.Item):
    """
    A Scrapy item class for storing extracted data.

    Fields:
        text_content (scrapy.Field): The field to store the extracted text content.
    """
    text_content = scrapy.Field()
