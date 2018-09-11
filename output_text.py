import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import random
from thesaurus import Word

def break_response(text):
    words = nltk.tokenize.word_tokenize(text)
    wordlist = [word for word in words if word.isalpha()]
    return wordlist

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    features = wordlist.keys()
    return features
#features = get_word_features(wordlist)

def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and not word.startswith('#')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
#wordcloud_draw(features)

def reccomend_word(wordlist):
    benedict = nltk.FreqDist(words)
    target_word = benedict.max()
    candidate_words = Word(target_word).synonyms(relevance=1)
    stop_words = set(stopwords.words('english')) 
    filtered_candidates = [w for w in candidate_words if w not in stop_words] 
    reccomendation = filtered_candidates[random.randint(0,len(filtered_candidates)+1)]
    return reccomendation