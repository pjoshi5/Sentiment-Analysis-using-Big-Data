#!/usr/bin/env python
"""mapper.py"""

import sys
#import pandas as pd
import re as re
#from nltk.corpus import stopwords
#from textblob import TextBlob
#from nltk.stem import PorterStemmer
#st = PorterStemmer()
#stop = stopwords.words('english')
stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
other_stopwords = ['i','or','is','he','also','like','of','but','in','it','and','a','by','to','for','of','an','by','it','am','he','said','would','mr','year','rt','amp','man','cfrp','called','want','one','get','dems','maybe','dont','come','go','el','secur','make']
stop = stop + other_stopwords

#file_name_given = 'nytimes_withtop50.txt'
#if file_name_given:
#    inf = open(file_name_given,encoding="utf8")
#else:
#    inf = sys.stdin

## read the top 500 words


#top_500_words = inf[0]
# input comes from STDIN (standard input)
#inf = inf[1:]
#print(type(inf),inf)    

file_list = []
for line in sys.stdin:
#for line in inf:
    # remove leading and trailing whitespace
    #print(line)
    file_list.append(line)
#print("file_list[0]",len(file_list[0]),type(file_list[0]))
top_50_words = file_list[0].split(",")
#print(type(top_50_words),len(top_50_words))
file_list = file_list[1:]
for word_search in top_50_words:
    #print("word_search",word_search)
    for line in file_list:
        line = line.strip()
        #print("\n",line)
    
        # split the line into words
        words = line.split()
        #print(words)
        for pos in range(len(words) - 1):            
            word = words[pos].lower()
            word = re.sub('[^A-Za-z0-9]+', '', word)
            if word not in stop and not word.isdigit() and word not in (None, ''):
                #print("word_search",word_search)
                #print("word",word)
                #word = st.stem(word)
                if word == word_search:
                    word2 = words[pos+1].lower()
                    word2 = re.sub('[^A-Za-z0-9]+', '', word2)
                    if word2 not in stop and not word2.isdigit() and word2 not in (None, ''):
                        cooccuring_words = word+"-"+word2
                        print "%s\t%s" % (cooccuring_words,1)


