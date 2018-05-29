import nltk, re, pprint
from nltk import word_tokenize
from urllib import request


url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode("utf8")

# to find starting location
start_loc = raw.find("PART I")
end_loc = raw.rfind("End of Project Gutenberg’s Crime and Punishment")
raw = raw[start_loc:end_loc]
print("-----start------")

print(type(raw))
print(len(raw))
print(raw[:75])
print("---------------")


# tokenize raw txt
tokens = word_tokenize(raw)
print("Type of tokens: " + str(type(tokens)))
print("Len of tokens: " + str(len(tokens)))
print("Token contents first 10: " + str(tokens[:10]))
print("---------------")

# making this a NLTK Text
text = nltk.Text(tokens)
print("Type of text: " + str(type(text)))
print("Len of text: " + str(len(text)))
print("First 10: " + str(text[1024:1062]))
text.collocations()  # this thing prints. but returns None.
print("---------------")




