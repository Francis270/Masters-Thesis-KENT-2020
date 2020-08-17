import string
import nltk

#nltk.download('punkt')                                  # first-time use only
#nltk.download('wordnet')                                # first-time use only

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Subject:

    def __init__(self, name, dir):
        self.name = name
        f = open(dir + '/' + self.name + '.txt', 'r')
        self.content = f.read().lower()

        self.sent_tokens = nltk.sent_tokenize(self.content)
        self.word_tokens = nltk.word_tokenize(self.content)

        self.lemmer = nltk.stem.WordNetLemmatizer()
        self.remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemTokens(self, tokens):
            return [self.lemmer.lemmatize(token) for token in tokens]

    def LemNormalize(self, text):
        return self.LemTokens(nltk.word_tokenize(text.lower().translate(self.remove_punct_dict)))
    
    def response(self, user_response):
        self.sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=self.LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        return self.sent_tokens[idx] if req_tfidf != 0 else 'I am sorry! I don\'t understand'