import nltk
from urllib import request
url = "https://gist.githubusercontent.com/fogus/3674330/raw/2758d99632d66763fac18c987fc202e6e93d7ac9/d.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
tokes = nltk.sent_tokenize(raw)
for toke in tokes:
    toke_harder = nltk.word_tokenize(toke)
    print(toke_harder)