import nltk, re, pprint
from nltk import word_tokenize


# error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte if we do this
'''
file = open("The_Prince.txt")
print("Type: "+str(type(file)))
raw = file.read()
'''

# b means read as binary so contents will remain a bytes. No decoding attempt will happen this way.
with open("The_Prince.txt", "rb") as f:
    print("Type: "+str(type(f)))
    raw = f.read()

    tokens = word_tokenize(raw.decode("utf16")) # strange why is this utf 16 when the web says this is utf 8
    print(str(tokens[:50]))
    text = nltk.Text(tokens)
    text.dispersion_plot(["Prince", "principle", "moral"])
