import random
import feedparser
import html
import sys


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
            print("Got a random quote!")
            quote = random.choice(quotes)
            update_file(quote[1], out_folder+"quote.txt")
            update_file(quote[0], out_folder+"author.txt")
            update_file(quote[2], out_folder+"link.txt")
        else:
            print("No quotes found for the specified user!")
    else:
        print("Invalid number of arguments! Expected 4, got " + str(len(sys.argv)) + ".")

