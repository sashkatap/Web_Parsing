# Web parsing studying

Here are examples of my studying parsing tasks with libraries and frameworks:

## Libraries requests & BeautifulSoup (bs4)

[bs4.ipynb](https://github.com/sashkatap/scraping/blob/main/bs4.ipynb) - I parsed [the studing site](https://books.toscrape.com/) containing many books.
My goal was to get all 20 books from a page.

[bs4_pages.ipynb](https://github.com/sashkatap/scraping/blob/main/bs4_pages.ipynb) - In the next case I parsed all 20 books from all 50 pages of [the site](https://books.toscrape.com/).

## Scrapy framework

[Books folder](https://github.com/sashkatap/scraping/tree/main/books) - Here I created a spider file [books_crawl.py](https://github.com/sashkatap/scraping/blob/main/books/books/spiders/books_crawl.py) to get the same 20 books from the first page of [the site](https://books.toscrape.com/).

As a result I got [books.json](https://github.com/sashkatap/scraping/blob/main/books/books.json) and [books.csv](https://github.com/sashkatap/scraping/blob/main/books/books.csv) files with image, title and price of each book on a page.

### Multiple pages scraping with Scrapy

[Books_pages folder](https://github.com/sashkatap/scraping/tree/main/books_pages) - Here I created a spider file again [pages_crawl.py](https://github.com/sashkatap/scraping/blob/main/books_pages/books_pages/spiders/pages_crawl.py) for this time to get all books from all pages of [the site](https://books.toscrape.com/). Summury 1000 books in a minute.

As a result I got [books_pages_all.json](https://github.com/sashkatap/scraping/blob/main/books_pages/books_pages_all.json) file with image, title, price, description and UPC of each book.

Also, I added a line to correct encoding `FEED_EXPORT_ENCODING = 'utf-8'` in [settings.py](https://github.com/sashkatap/scraping/blob/main/books_pages/books_pages/settings.py) , so in both cases we've got correct GBP currency symbol.

## Scrapy & JavaScript integration through Splash

For scraping data from JavaScript sites, is requaired to add [the library provides Scrapy and JavaScript integration using Splash](https://github.com/scrapy-plugins/scrapy-splash).

To test local Splash server, run Docker container:

```
sudo docker run -p 8050:8050 scrapinghub/splash
```

Web interfase is avalible on the `localhost:8050` in your browser.

Try to get content of JavaScript site for test.

For that add following code to web console:

```
function main(splash, args)
    url = args.url
    assert(splash:go(url))
    return splash:html()
end
```

For correct working of the script:

1. According to the instruction of Splash author, I add in [settings.py](https://github.com/sashkatap/scraping/blob/main/quotes/quotes/settings.py) : 1 - 4 points and encoding utf-8
2. Than run Docker container by the command above
3. And start the [qt_splash.py script](https://github.com/sashkatap/scraping/blob/main/quotes/quotes/spiders/qt_splash.py)

My goal is parse all 100 quotes from 10 pages of [the javascript site](https://quotes.toscrape.com/js/).

As a result I got [quotes.json](https://github.com/sashkatap/scraping/blob/main/quotes/quotes.json) file with 10 quotes from 1st page, and [all_quotes.json](https://github.com/sashkatap/scraping/blob/main/quotes/all_quotes.json) file with 100 quotes from all pages.

## Selenium Framework

> Selenium WebDriver for your current version browser should be installed before starting the script!

The goal of the [login.py script](https://github.com/sashkatap/scraping/blob/main/Selenium/login.py) is auto login [on the site](https://quotes.toscrape.com/login).

As a result, browser Chrome starts automatically, logined to the site and gets html code of the page after login.

The goal of the [infinite_scroll.py script](https://github.com/sashkatap/scraping/blob/main/Selenium/infinite_scroll.py) is to find all quotes on [the endless scroll site](https://quotes.toscrape.com/scroll)

As a result, browser Chrome starts automatically, scrolls down the site to the end, finds all quotes and counts it (100).
