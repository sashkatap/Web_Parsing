# Web parsing studying

Here are examples of my scraping with frameworks:

## Requests & BeautifulSoup

[bs4.ipynb](https://github.com/sashkatap/scraping/blob/main/bs4.ipynb) - I scraped [the studing site](https://books.toscrape.com/) containing many books.
My goal was to get all 20 books from a page.

[bs4_pages.ipynb](https://github.com/sashkatap/scraping/blob/main/bs4_pages.ipynb) - In the next case I scraped all books from all pages of [the site](https://books.toscrape.com/).

## Scrapy

[Books folder](https://github.com/sashkatap/scraping/tree/main/books) - Here I created a spider file [books_crawl.py](https://github.com/sashkatap/scraping/blob/main/books/books/spiders/books_crawl.py) to get the same 20 books from the first page of [the site](https://books.toscrape.com/).

As a result I got [books.json](https://github.com/sashkatap/scraping/blob/main/books/books.json) and [books.csv](https://github.com/sashkatap/scraping/blob/main/books/books.csv) files with image, title and price of each book on a page.

### Multiple pages scraping with Scrapy

[Books_pages folder](https://github.com/sashkatap/scraping/tree/main/books_pages) - Here I created a spider file again [pages_crawl.py](https://github.com/sashkatap/scraping/blob/main/books_pages/books_pages/spiders/pages_crawl.py) for this time to get all items (books) from all pages of [the site](https://books.toscrape.com/). Summury 1000 books in a minute.

As a result I got [books_pages_all.json](https://github.com/sashkatap/scraping/blob/main/books_pages/books_pages_all.json) file with image, title, price, description and UPC of each book.

Also, I added a line to correct encoding `FEED_EXPORT_ENCODING = 'utf-8'` in [settings.py](https://github.com/sashkatap/scraping/blob/main/books_pages/books_pages/settings.py) , so in both cases we've got correct GBP currency symbol.
