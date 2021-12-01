import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
"""The template was made by scrapy, then edited since rules and further.
It parses all books 1000 from all 20 pages of the studying site https://books.toscrape.com/
To start script and save to .json or .csv file print to the console: 
scrapy crawl pages_crawl -o books_pages.json
After that check it console 'item_scraped_count': 1000 (books on 20 pages)"""

class PagesCrawlSpider(CrawlSpider):
    name = 'pages_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']   #add httpS <-- here

    #at 1st rule add restrict_xpathS for getting all 20 books from one page
    #2nd rule for going to the next page
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")) 
    )

    def parse_item(self, response):
    #The function get 5 items from each book    
        item = {}
        item['title'] = response.xpath('//div[contains(@class, "product_main")]/h1/text()').get()
        item['price'] = response.xpath('//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').get()
        item['image'] = response.xpath('//div[@id="product_gallery"]/div[class="thumbnail"]/\
            div[class="carousel-inner"]/div[contains(@class, "item")]/img/@src').getall()
        #/../p it mean that we're to go to the netx element p, where we take text
        item['description'] = response.xpath('//div[@id="product_description"]/../p/text()').get()
        item['upc'] = response.xpath('//th[contains(text(), "UPC")]/../td/text()').get()
        return item
