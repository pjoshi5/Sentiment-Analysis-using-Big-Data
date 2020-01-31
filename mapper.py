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
#print(stop)
other_stopwords = ['i','or','is','he','also','like','of','but','in','it','and','a','by','to','for','of','an','by','it','am','he','said','would','mr','year','de','rt','amp','man','cfrp','called','want','one','dems','maybe','dont','come','go','el','secur','make']
stop = stop + other_stopwords


#file_name_given = 'tweets.txt'
#if file_name_given:
#    inf = open(file_name_given,encoding="utf8")
#else:
#    inf = sys.stdin

# input comes from STDIN (standard input)
for line in sys.stdin:
#for line in inf:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    #print(type(words))
    
    

    
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        
        
        ## remove unwanted punctuation i.e. remove anything but words and spaces by blank
        word = re.sub(r'\W+', '', word)
        ## converting words to lower case
        word = word.lower()
        #word = ''.join(e for e in word if e.isalnum())
        word = re.sub('[^A-Za-z0-9]+', '', word)
        #print(word)
        #and not word.isdigit
        ## Removing Stop Words and digits
        if word not in stop and not word.isdigit() and word not in (None, ''):
            #word = st.stem(word)
            print '%s\t%s' % (word, 1)





