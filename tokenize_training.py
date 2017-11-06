import nltk

from nltk.tokenize import sent_tokenize

# w tym module znajduja sie funkcja ktore odpowiadaja za przetwarzanie jezyka naturalego (rowniez wersje testowe)
# wykorzystujaca biblioteki nltk funkcja znajdujaca czesci mowy
def training(sample_text):
    try:
        for i in sent_tokenize(sample_text):
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            return tagged

    except Exception as e:
        print(str(e))