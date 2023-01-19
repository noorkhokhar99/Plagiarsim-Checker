# module to check cosine similarity of two strings

import re
import math
from collections import Counter

WORD = re.compile(r'\w+')

# returns cosine similarity of two vectors
# input: two vectors
# output: integer between 0 and 1.

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
#      print(intersection)
    matchWords = {}
    for i in intersection:
        if(vec1[i] > vec2[i]):
            matchWords[i] = vec2[i]
        else:
            matchWords[i] = vec1[i]
        # print(i)
    # print(matchWords)
	
    # calculating numerator
    numerator = sum([vec1[x] * matchWords[x] for x in intersection])
    # print(numerator)
    # calculating denominator
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([matchWords[x]**2 for x in matchWords.keys()])
    # print(sum1,sum2)
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    # print(denominator)
    # checking for divide by zero
    if denominator == 0:
        return 0.0
    else:
        return float(numerator) / denominator

# converts given text into a vector

def text_to_vector(text):
    # uses the Regular expression above and gets all words
    words = WORD.findall(text)
    # returns a counter of all the words (count of number of occurences)
    return Counter(words)

# returns cosine similarity of two words

def cosineSim(text1, text2):
    t1 = text1.lower()
    t2 = text2.lower()
    # print('t1 : ',t1, '\nt2 : ', t2)
    vector1 = text_to_vector(t1)
    vector2 = text_to_vector(t2)
    cosine = get_cosine(vector1, vector2)
    return cosine