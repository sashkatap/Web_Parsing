import scrapy
from scrapy_splash import SplashRequest   # add Splash

'''To start the script, print to console:  scrapy crawl qt_splash -o all_quotes.json '''

class QtSplashSpider(scrapy.Spider):
    name = 'qt_splash'
    allowed_domains = ['quotes.toscrape.com']

    script = '''
        function main(splash, args)
            url = args.url
            assert(splash:go(url))
            return splash:html()
        end
    '''

    def start_requests(self):
    # Go to the link and parse the content using "script" above and transmit it bottom function     
        yield SplashRequest(url='https://quotes.toscrape.com/js/', callback=self.parse, endpoint='execute', args={
            'lua_source': self.script
        })

    def parse(self, response):
    # Getting author, text and all tags from each quote
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'author': quote.xpath(".//small[@class='author']/text()").get(),
                'text': quote.xpath(".//span[@class='text']/text()").get(),
                'tags': quote.xpath(".//a[@class='tag']/text()").getall()
            }
    # Get a next page link, if it is, go there and execute the function again 
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        
        if next_page:             # the same, but not right: url = 'quotes.toscrape.com' + next_page  
            url = response.urljoin(next_page)  # add "allowed_domains" link to short link "next_page"
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={
                'lua_source': self.script
            })
            # the same script was done earlier, but this time it gets new link to next page each time