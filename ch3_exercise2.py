import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.nst.com.my/news/nation/2018/05/374266/inappropriate-respond-1mdb-questions-now-najib"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
raw = bsObj.find("article", {"id": "node-374266"}).get_text()
# raw = bsObj.body.h1.get_text()
tokens = word_tokenize(raw)
print("Tokens: " + str(tokens))
print("------------------------")

# change to NLTK Text object
print()
text = nltk.Text(tokens)
print("Text object: "+ str(type(text)))
text.concordance("Najib")