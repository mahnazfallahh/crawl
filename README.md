# Databurst Spider

Databurst Spider is a Scrapy spider that can be used for scraping data from web pages and writing it to a CSV file. It extract information from databurst website.

## Installation

To use Databurst Spider, you need to have Python and pip installed on your system. You can install Databurst Spider and its dependencies using pipenv, a popular Python dependency management tool.

1. Clone the repository:

   ````shell
   git clone https://github.com/mahnazfallahh/crawl.git
   

2. Change directory to the project folder:

   ````shell
   cd databurst
   

3. Install the dependencies with pipenv:

   ````shell
   pipenv install
   

## Usage

1. Activate the pipenv shell:

   ````shell
   pipenv shell
   ```

2. Run the spider:

   ````shell
   scrapy crawl databurst_spider
   ```

3. The scraped data will be saved in a CSV file specified by the `file_name` attribute.

## Configuration

You can customize the behavior of the Databurst Spider by modifying the attributes in the `DataburstSpider` class.

- `name`: The name of the spider.
- `start_urls`: A list of URLs to start the spider's crawling process.
- `file_name`: The name of the CSV file to save the scraped data.

## Error Handling

The spider includes error handling for writing data to the CSV file. If an error occurs while writing to the file, a `csv.Error` exception is raised and the error message is printed.


