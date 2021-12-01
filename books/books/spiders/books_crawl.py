import scrapy
"""The template was made by scrapy, then edited since function and further.
It scraps just one page of the studying site https://books.toscrape.com/
To start script and save to .json or .csv file print to the console: 
scrapy crawl books_crawl -o books.json
scrapy crawl books_crawl -o books.csv
After that check it console 'item_scraped_count': 20 (books on a page)"""

class BooksCrawlSpider(scrapy.Spider):
    name = 'books_crawl'
    allowed_domains = ['books.toscrape.com']        # without https
    start_urls = ['https://books.toscrape.com/']    # delite double https

    def parse(self, response):
        # the pass to each book on the page https://books.toscrape.com/
        books = response.xpath("//ol[@class='row']/li")
        for book in books:
            yield {     #'.' for each book in dict, if not it'll be only the first one
                'image': book.xpath(".//div[@class='image_container']/a/img/@src").get(),
                'title': book.xpath(".//h3/a/@title").get(),
                'price': book.xpath(".//p[@class='price_color']/text()").get()
            }