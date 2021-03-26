# -*- coding: utf-8 -*-

import nltk
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import re, string
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
import unittest

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


class TestRemoveNoise(unittest.TestCase):
    def test_remove_noise(self):
        # empty string
        test1 = ""
        actual1 = remove_noise(test1)
        expected1 = ""  
        bool1 = actual1 == expected1
        print("Test 1 is " + str(bool1))
        
        # text with actual noise
        test2 = "!asda123$#@"
        actual2 = remove_noise(test2)
        expected2 = ['a', 's', 'd', 'a', '1', '2', '3']
        bool2 = actual2 == expected2
        print("Test 2 is " + str(bool2))
        
        # text with Chinese characters
        test3 = "你好，我正%在上C#OSC3!10"
        actual3 = remove_noise(test3)
        expected3 = ['你', '好', '，', '我', '正', '在', '上', 'c', 'o', 's', 'c', '3', '1', '0']
        bool3 = actual3 == expected3
        print("Test 3 is " + str(bool3))
        
        totalbool = bool1 & bool2 & bool3
        self.assertTrue(totalbool)


if __name__ == '__main__':
    unittest.main()

