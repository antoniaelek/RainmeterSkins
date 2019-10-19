import random
import feedparser
import html
import sys
import requests
import re
from selectolax.parser import HTMLParser


def get_quotes(user_id, user_name, sort=False):
    url = 'https://www.goodreads.com/quotes/list_rss/' + user_id + '-' + user_name
    quotes = []
    page = 1
    while True:
        try:
            new_quotes = _parse_rss_page(url + '?page=' + str(page))
            if len(new_quotes) == 0:
                break
            quotes.extend(new_quotes)
            page = page + 1
        except:
            break

    if sort:
        quotes.sort()

    return quotes


def _parse_rss_page(url):
    feed = feedparser.parse(url)
    page_quotes = []

    for entry in feed.entries:
        try:
            summary = entry.summary
            sep = summary.rfind('-- ')
            quote = html.unescape(summary[1:sep - 2])
            author = html.unescape(summary[sep + 3:])
            link = html.unescape(entry.link)
            page_quotes.append((author, quote, link))
        except:
            continue

    return page_quotes


def _parse_quote_page(url):
    data = requests.get(url)
    dom = HTMLParser(data.text)
    for tag in dom.css('a.authorOrTitle'):
        if 'href' in tag.attributes:
            return (tag.text(), tag.attributes['href'])

    return None


def update_file(text, file):
    if text != "":
        f = open(file,"w+", encoding='utf-8')
        f.write(text)
        f.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        out_folder = sys.argv[1]
        print(out_folder)
        
        user_id = sys.argv[2]
        print(user_id)

        user_name = sys.argv[3]
        print(user_name)
        
        quotes = get_quotes(user_id, user_name, sort=True)
        if (len(quotes)>0):
            quote_obj = random.choice(quotes)
            author = quote_obj[0]
            quote = quote_obj[1]
            link_quote = quote_obj[2]
            link_book = "https://www.goodreads.com"
            
            book_obj = _parse_quote_page(link_quote)
            if book_obj != None:
                author = author + ", " + book_obj[0]
                link_book = "https://www.goodreads.com" + book_obj[1]
            
            print("Got a random quote!")

            update_file(quote, out_folder+"quote.txt")
            update_file(author, out_folder+"author.txt")
            update_file(link_quote, out_folder+"link_quote.txt")
            update_file(link_book, out_folder+"link_book.txt")
        else:
            print("No quotes found for the specified user!")
    else:
        print("Invalid number of arguments! Expected 4, got " + str(len(sys.argv)) + ".")

