import nltk
import os

proxy = 'http://anubhav.apurva%40hpe.com:Linkinpark%408@web-proxy.atl.hp.com:8088'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sid.polarity_scores('happy')


from nltk.corpus import sentiwordnet as swn
#nltk.download('sentiwordnet')
#nltk.download('wordnet')
swn.senti_synsets('happy', 'a')
swn.senti_synsets('happy', 'a')[0].neg_score()
