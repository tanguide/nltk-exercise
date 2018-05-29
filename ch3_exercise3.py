'''
In this exercise, we try to pull from a RSS feed
'''
import nltk, re, pprint
# new, need to pip install this
import feedparser
from bs4 import BeautifulSoup
from nltk import word_tokenize
from urllib import request

# latest news from CNA's latest news feed
llog = feedparser.parse("https://www.channelnewsasia.com/rssfeeds/8395986")
print("Title - " + str(llog["feed"]["title"]))
print("Length - " + str( len(llog.entries) ))

post = llog.entries[2]
print("Entry 3 - " + post.title)
print("Type of post - " + str(type(post)))

# post is a dictionary
'''
for k,v in post.items():
    print("Key: "+ str(k) + " Value: " + str(v))


'''
content = post.get("summary")
print("70 char of first content - " + str(content[:70]))

print("Start of BS -------------")
raw = BeautifulSoup(content, "html.parser").get_text()
tokens = word_tokenize(raw)
print("Tokenised")
print(str(tokens))

