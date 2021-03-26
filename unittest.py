# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:31:05 2021

@author: sword
"""
import nltk
from nltk.tag import pos_tag
import re, string
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
import unittest
import numpy as np

def lemma(s):
    # Make an array by tokenizing the sentence
    array = nltk.word_tokenize(s)
    newArray = []
    # Lemmatize the words in the array
    for word in array:
        newArray.append(l.lemmatize(word.lower()))
    return newArray

def word_bag(s, words):
    # Lemmatize the input sentence
    array = lemma(s)
    # empty array of 0
    bag = [0]*len(words)  
    for s in array:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word exists
                bag[i] = 1
                break
                
    return(np.array(bag))

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

class TestLemma(unittest.TestCase):
    def test_lemma(self):
        print("TESTING LEMMA():")
        # empty string
        test1 = ""
        actual1 = lemma(test1)
        expected1 = []  
        bool1 = actual1 == expected1
        print("Test 1 is " + str(bool1))
        
        # long text words
        test2 = "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way. On her way she met a copy. The copy warned the Little Blind Text, that where it came from it would have been rewritten a thousand times and everything that was left from its origin would be the word and and the Little Blind Text should turn around and return to its own, safe country. But nothing the copy said could convince her and so it didn’t take long until a few insidious Copy Writers ambushed her, made her drunk with Longe and Parole and dragged her into their agency, where they abused her for their projects again and again. And if she hasn’t been rewritten, then they are still using her. Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way. On her way she met a copy. The copy warned the Little Blind Text, that where it came from it would have been rewritten a thousand times and everything that was left from its origin would be the word and and the Little Blind Text should turn around and return to its own, safe country. But nothing the copy said could convince her and so it didn’t take long until a few insidious Copy Writers ambushed her, made her drunk with Longe and Parole and dragged her into their agency, where they abused her for their projects again and again. And if she hasn’t been rewritten, then they are still using her. Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way. On her way she met a copy. The copy warned the Little Blind Text, that where it came from it would have been rewritten a thousand times and everything that was left from its origin would be the word and the Little Blind Text should turn around and return to its own, safe country. But nothing the copy said could convince her and so it didn’t take long until a few insidious Copy Writers ambushed her, made her drunk with Longe and Parole and dragged her into their agency, where they abused her for their projects again and again. And if she hasn’t been rewritten, then they are still using her.Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It"
        actual2 = lemma(test2)
        expected2 = ['far', 'far', 'away', ',', 'behind', 'the', 'word', 'mountain', ',', 'far', 'from', 'the', 'country', 'vokalia', 'and', 'consonantia', ',', 'there', 'live', 'the', 'blind', 'text', '.', 'separated', 'they', 'live', 'in', 'bookmarksgrove', 'right', 'at', 'the', 'coast', 'of', 'the', 'semantics', ',', 'a', 'large', 'language', 'ocean', '.', 'a', 'small', 'river', 'named', 'duden', 'flow', 'by', 'their', 'place', 'and', 'supply', 'it', 'with', 'the', 'necessary', 'regelialia', '.', 'it', 'is', 'a', 'paradisematic', 'country', ',', 'in', 'which', 'roasted', 'part', 'of', 'sentence', 'fly', 'into', 'your', 'mouth', '.', 'even', 'the', 'all-powerful', 'pointing', 'ha', 'no', 'control', 'about', 'the', 'blind', 'text', 'it', 'is', 'an', 'almost', 'unorthographic', 'life', 'one', 'day', 'however', 'a', 'small', 'line', 'of', 'blind', 'text', 'by', 'the', 'name', 'of', 'lorem', 'ipsum', 'decided', 'to', 'leave', 'for', 'the', 'far', 'world', 'of', 'grammar', '.', 'the', 'big', 'oxmox', 'advised', 'her', 'not', 'to', 'do', 'so', ',', 'because', 'there', 'were', 'thousand', 'of', 'bad', 'comma', ',', 'wild', 'question', 'mark', 'and', 'devious', 'semikoli', ',', 'but', 'the', 'little', 'blind', 'text', 'didn', '’', 't', 'listen', '.', 'she', 'packed', 'her', 'seven', 'versalia', ',', 'put', 'her', 'initial', 'into', 'the', 'belt', 'and', 'made', 'herself', 'on', 'the', 'way', '.', 'when', 'she', 'reached', 'the', 'first', 'hill', 'of', 'the', 'italic', 'mountain', ',', 'she', 'had', 'a', 'last', 'view', 'back', 'on', 'the', 'skyline', 'of', 'her', 'hometown', 'bookmarksgrove', ',', 'the', 'headline', 'of', 'alphabet', 'village', 'and', 'the', 'subline', 'of', 'her', 'own', 'road', ',', 'the', 'line', 'lane', '.', 'pityful', 'a', 'rethoric', 'question', 'ran', 'over', 'her', 'cheek', ',', 'then', 'she', 'continued', 'her', 'way', '.', 'on', 'her', 'way', 'she', 'met', 'a', 'copy', '.', 'the', 'copy', 'warned', 'the', 'little', 'blind', 'text', ',', 'that', 'where', 'it', 'came', 'from', 'it', 'would', 'have', 'been', 'rewritten', 'a', 'thousand', 'time', 'and', 'everything', 'that', 'wa', 'left', 'from', 'it', 'origin', 'would', 'be', 'the', 'word', 'and', 'and', 'the', 'little', 'blind', 'text', 'should', 'turn', 'around', 'and', 'return', 'to', 'it', 'own', ',', 'safe', 'country', '.', 'but', 'nothing', 'the', 'copy', 'said', 'could', 'convince', 'her', 'and', 'so', 'it', 'didn', '’', 't', 'take', 'long', 'until', 'a', 'few', 'insidious', 'copy', 'writer', 'ambushed', 'her', ',', 'made', 'her', 'drunk', 'with', 'longe', 'and', 'parole', 'and', 'dragged', 'her', 'into', 'their', 'agency', ',', 'where', 'they', 'abused', 'her', 'for', 'their', 'project', 'again', 'and', 'again', '.', 'and', 'if', 'she', 'hasn', '’', 't', 'been', 'rewritten', ',', 'then', 'they', 'are', 'still', 'using', 'her', '.', 'far', 'far', 'away', ',', 'behind', 'the', 'word', 'mountain', ',', 'far', 'from', 'the', 'country', 'vokalia', 'and', 'consonantia', ',', 'there', 'live', 'the', 'blind', 'text', '.', 'separated', 'they', 'live', 'in', 'bookmarksgrove', 'right', 'at', 'the', 'coast', 'of', 'the', 'semantics', ',', 'a', 'large', 'language', 'ocean', '.', 'a', 'small', 'river', 'named', 'duden', 'flow', 'by', 'their', 'place', 'and', 'supply', 'it', 'with', 'the', 'necessary', 'regelialia', '.', 'it', 'is', 'a', 'paradisematic', 'country', ',', 'in', 'which', 'roasted', 'part', 'of', 'sentence', 'fly', 'into', 'your', 'mouth', '.', 'even', 'the', 'all-powerful', 'pointing', 'ha', 'no', 'control', 'about', 'the', 'blind', 'text', 'it', 'is', 'an', 'almost', 'unorthographic', 'life', 'one', 'day', 'however', 'a', 'small', 'line', 'of', 'blind', 'text', 'by', 'the', 'name', 'of', 'lorem', 'ipsum', 'decided', 'to', 'leave', 'for', 'the', 'far', 'world', 'of', 'grammar', '.', 'the', 'big', 'oxmox', 'advised', 'her', 'not', 'to', 'do', 'so', ',', 'because', 'there', 'were', 'thousand', 'of', 'bad', 'comma', ',', 'wild', 'question', 'mark', 'and', 'devious', 'semikoli', ',', 'but', 'the', 'little', 'blind', 'text', 'didn', '’', 't', 'listen', '.', 'she', 'packed', 'her', 'seven', 'versalia', ',', 'put', 'her', 'initial', 'into', 'the', 'belt', 'and', 'made', 'herself', 'on', 'the', 'way', '.', 'when', 'she', 'reached', 'the', 'first', 'hill', 'of', 'the', 'italic', 'mountain', ',', 'she', 'had', 'a', 'last', 'view', 'back', 'on', 'the', 'skyline', 'of', 'her', 'hometown', 'bookmarksgrove', ',', 'the', 'headline', 'of', 'alphabet', 'village', 'and', 'the', 'subline', 'of', 'her', 'own', 'road', ',', 'the', 'line', 'lane', '.', 'pityful', 'a', 'rethoric', 'question', 'ran', 'over', 'her', 'cheek', ',', 'then', 'she', 'continued', 'her', 'way', '.', 'on', 'her', 'way', 'she', 'met', 'a', 'copy', '.', 'the', 'copy', 'warned', 'the', 'little', 'blind', 'text', ',', 'that', 'where', 'it', 'came', 'from', 'it', 'would', 'have', 'been', 'rewritten', 'a', 'thousand', 'time', 'and', 'everything', 'that', 'wa', 'left', 'from', 'it', 'origin', 'would', 'be', 'the', 'word', 'and', 'and', 'the', 'little', 'blind', 'text', 'should', 'turn', 'around', 'and', 'return', 'to', 'it', 'own', ',', 'safe', 'country', '.', 'but', 'nothing', 'the', 'copy', 'said', 'could', 'convince', 'her', 'and', 'so', 'it', 'didn', '’', 't', 'take', 'long', 'until', 'a', 'few', 'insidious', 'copy', 'writer', 'ambushed', 'her', ',', 'made', 'her', 'drunk', 'with', 'longe', 'and', 'parole', 'and', 'dragged', 'her', 'into', 'their', 'agency', ',', 'where', 'they', 'abused', 'her', 'for', 'their', 'project', 'again', 'and', 'again', '.', 'and', 'if', 'she', 'hasn', '’', 't', 'been', 'rewritten', ',', 'then', 'they', 'are', 'still', 'using', 'her', '.', 'far', 'far', 'away', ',', 'behind', 'the', 'word', 'mountain', ',', 'far', 'from', 'the', 'country', 'vokalia', 'and', 'consonantia', ',', 'there', 'live', 'the', 'blind', 'text', '.', 'separated', 'they', 'live', 'in', 'bookmarksgrove', 'right', 'at', 'the', 'coast', 'of', 'the', 'semantics', ',', 'a', 'large', 'language', 'ocean', '.', 'a', 'small', 'river', 'named', 'duden', 'flow', 'by', 'their', 'place', 'and', 'supply', 'it', 'with', 'the', 'necessary', 'regelialia', '.', 'it', 'is', 'a', 'paradisematic', 'country', ',', 'in', 'which', 'roasted', 'part', 'of', 'sentence', 'fly', 'into', 'your', 'mouth', '.', 'even', 'the', 'all-powerful', 'pointing', 'ha', 'no', 'control', 'about', 'the', 'blind', 'text', 'it', 'is', 'an', 'almost', 'unorthographic', 'life', 'one', 'day', 'however', 'a', 'small', 'line', 'of', 'blind', 'text', 'by', 'the', 'name', 'of', 'lorem', 'ipsum', 'decided', 'to', 'leave', 'for', 'the', 'far', 'world', 'of', 'grammar', '.', 'the', 'big', 'oxmox', 'advised', 'her', 'not', 'to', 'do', 'so', ',', 'because', 'there', 'were', 'thousand', 'of', 'bad', 'comma', ',', 'wild', 'question', 'mark', 'and', 'devious', 'semikoli', ',', 'but', 'the', 'little', 'blind', 'text', 'didn', '’', 't', 'listen', '.', 'she', 'packed', 'her', 'seven', 'versalia', ',', 'put', 'her', 'initial', 'into', 'the', 'belt', 'and', 'made', 'herself', 'on', 'the', 'way', '.', 'when', 'she', 'reached', 'the', 'first', 'hill', 'of', 'the', 'italic', 'mountain', ',', 'she', 'had', 'a', 'last', 'view', 'back', 'on', 'the', 'skyline', 'of', 'her', 'hometown', 'bookmarksgrove', ',', 'the', 'headline', 'of', 'alphabet', 'village', 'and', 'the', 'subline', 'of', 'her', 'own', 'road', ',', 'the', 'line', 'lane', '.', 'pityful', 'a', 'rethoric', 'question', 'ran', 'over', 'her', 'cheek', ',', 'then', 'she', 'continued', 'her', 'way', '.', 'on', 'her', 'way', 'she', 'met', 'a', 'copy', '.', 'the', 'copy', 'warned', 'the', 'little', 'blind', 'text', ',', 'that', 'where', 'it', 'came', 'from', 'it', 'would', 'have', 'been', 'rewritten', 'a', 'thousand', 'time', 'and', 'everything', 'that', 'wa', 'left', 'from', 'it', 'origin', 'would', 'be', 'the', 'word', 'and', 'the', 'little', 'blind', 'text', 'should', 'turn', 'around', 'and', 'return', 'to', 'it', 'own', ',', 'safe', 'country', '.', 'but', 'nothing', 'the', 'copy', 'said', 'could', 'convince', 'her', 'and', 'so', 'it', 'didn', '’', 't', 'take', 'long', 'until', 'a', 'few', 'insidious', 'copy', 'writer', 'ambushed', 'her', ',', 'made', 'her', 'drunk', 'with', 'longe', 'and', 'parole', 'and', 'dragged', 'her', 'into', 'their', 'agency', ',', 'where', 'they', 'abused', 'her', 'for', 'their', 'project', 'again', 'and', 'again', '.', 'and', 'if', 'she', 'hasn', '’', 't', 'been', 'rewritten', ',', 'then', 'they', 'are', 'still', 'using', 'her.far', 'far', 'away', ',', 'behind', 'the', 'word', 'mountain', ',', 'far', 'from', 'the', 'country', 'vokalia', 'and', 'consonantia', ',', 'there', 'live', 'the', 'blind', 'text', '.', 'separated', 'they', 'live', 'in', 'bookmarksgrove', 'right', 'at', 'the', 'coast', 'of', 'the', 'semantics', ',', 'a', 'large', 'language', 'ocean', '.', 'a', 'small', 'river', 'named', 'duden', 'flow', 'by', 'their', 'place', 'and', 'supply', 'it', 'with', 'the', 'necessary', 'regelialia', '.', 'it']
        bool2 = actual2 == expected2
        print("Test 2 is " + str(bool2))
        
        # test on special characters
        test3 = "@elonmusk how are you doing w/ ur rocket & spaceship? Can I buy it for ~$100 +- 5? (btw here's my email hello@gmail.com) ^^"
        actual3 = lemma(test3)
        expected3 = ['@', 'elonmusk', 'how', 'are', 'you', 'doing', 'w/', 'ur', 'rocket', '&', 'spaceship', '?', 'can', 'i', 'buy', 'it', 'for', '~', '$', '100', '+-', '5', '?', '(', 'btw', 'here', "'s", 'my', 'email', 'hello', '@', 'gmail.com', ')', '^^'] 
        bool3 = actual3 == expected3
        print("Test 3 is " + str(bool3))
        
        totalbool = bool1 & bool2 & bool3
        self.assertTrue(totalbool)

class TestWordBag(unittest.TestCase):
    def test_word_bag(self):
        print("TESTING WORDBAG():")
        # empty string
        actual1 = word_bag("", ["hello","how","are","you"])
        expected1 = [0,0,0,0]
        for boo in actual1==expected1:
            if boo == False:
                bool1 = False
                break
            else:
                bool1 = True
        print("Test 1 is " + str(bool1))
        
        # empty array
        actual2 = word_bag("hello how are you?", [])
        expected2 = [0]
        if len(actual2)>0:
            for boo in actual2==expected2:
                if boo == False:
                    bool2 = False
                    break
                else:
                    bool2 = True
            print("Test 2 is " + str(bool2))
        else: 
            bool2 = True
            print("Test 2 is " + str(bool2))
            
        
        # both empty
        actual3 = word_bag("", [])
        expected3 = [1]
        if len(actual2)>0:
            for boo in actual3==expected3:
                if boo == False:
                    bool3 = False
                    break
                else:
                    bool3 = True
            print("Test 3 is " + str(bool3))
        else: 
            bool3 = True
            print("Test 3 is " + str(bool3))
        
        totalbool = bool1 & bool2 & bool3
        self.assertTrue(totalbool)

class TestRemoveNoise(unittest.TestCase):
    def test_remove_noise(self):
        print("TESTING REMOVE_NOISE():")
        # empty string
        test1 = ""
        actual1 = remove_noise(test1)
        expected1 = [] 
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

