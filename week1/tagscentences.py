import nltk
from urllib import request
url = "https://gist.githubusercontent.com/fogus/3674330/raw/2758d99632d66763fac18c987fc202e6e93d7ac9/d.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
sents = nltk.sent_tokenize(raw)
for sent in sents:
    tags = nltk.pos_tag(nltk.word_tokenize(sent))
    tupFilter = [tup for tup in tags if tup[1] == "NN"]
    print(tupFilter)
    