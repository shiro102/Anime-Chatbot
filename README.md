# Individual Chat bot Project by Anshul Dhariwal

# Individual Project Demo:

Github URL: <br>https://github.com/shiro102/Chat-bot-team-20/tree/Anshul
=======
## Describe your topic/interest (context of the chatbot, who will use it, etc. )

In this project, we developed an interactive conversational agent that responds to user input. In response to the user, the agent generates sentences as output. There are 2 types of target users. The first type of target users includes anime and manga lovers who would love to talk about them and know more about it. The second type of target users includes anyone who are interested in Japanese culture. There are 2 types of topics as well. The first type of topic of the conversation is about the general information and personal preference of anime. The second type of topic of the conversation is about the general information of Japan such as people, religion, food, samurai and so on.

<br>

## How the code works

### **How to run it:** 

To compile the code, we run in terminal these 2 files of code - “train.py” and “chatbot.py”. The first code is to train the model which is used by the chatbot to generate responses. The second code is to run the app. Further instructions are in the README file in the CODE folder.

### **Stages of development:**

There are five stages of the development for the code: data importing and loading, data preprocessing, data training and testing, model building, and GUI developing.

### **How the classes are organized:**

There are 12 classes used in the code: nltk, json, pickle, numpy, keras, and tkinter, Wikipedia, Stanford Corenlp, Sentimental Analyser, GUI, Home, and Recent.

- Class “nltk” contains a group of libraries which provide statistical processing for English Language and is commonly used for Natural Language Processing. It is used throughout all the developing stages except the model building stage and the GUI development stage. 

- There are 4 critical methods within this class: “nltk.stem.wordnetlemmatizer”, “nltk.word_tokenize”, “nltk.pos_tag” (instead of Stanfordnlp’s POS tagging to simplify the implementation) and “nltk.corpus” 

        1. The first method, “nltk.stem.wordnetlemmatizer”, converts a word into its lemma form, groups different words to be analyzed as a single item based on similar meaning, and then creates a pickle file to store the Python objects which we will use while predicting. 

        2. The second method, “nltk.word_tokenize”, is used to cleanup and break the whole text into small parts, such as words.

        3. The third method, “nltk.pos_tag”, tags every word as “Proper Nouns”, “Verb”, “Adjectives” etc. It is used for one of the new features we added - POS tagging - and it works in the similar pattern as Stanford Corenlp’s POS tagging. We will explain Stanford Corenlp later.

        4. The fourth method, “nltk.corpus”, is used to access “wordnet” which helps us to implement a new feature that we added to this code - synonym recognition. 

- Class “json” is the data file which predicts the user inputs and gives responses. It is used for importing and loading data, preprocessing data, and getting random responses for the GUI. Json is also used implicitly throughout the program as the fundamental data in chatbot - conversation patterns.

- Class “pickle” is to make the data operations more efficient by removing object hierarchy when dumping our data or when loading our data from the dataset as it converts/treats the data as a single stream. Pickle is used throughout the stages except the data importing stage and the GUI development stage. It was also used to save a model for one of the new features that we added to this code - sentiment analysis. 

- Class “numpy” is to increase the efficiency of the operation of lists in python. It is used in 2 stages - “creating data for training and testing” and “predicting classes for GUI”.

- Class “keras'' is to build and import the deep neural network model for the trained data. It is used in the stages of building and importing the model to GUI. 

- Class “tkinter” is used to develop a graphical user interface by powerful libraries and functions within the class. It is used to develop the final GUI.

- Class “Wikipedia” is used to initiate online searches on Wikipedia in real time. It is an additional feature for our chatbot that functions when the chatbot doesn’t recognize a “Proper Noun” that is found by one of the new features we added - POS tagging.

- Class “Stanford Corenlp” is a service for natural language processing. Instead of creating a wrapper ourselves, we used a wrapper for this class called stanfordcorenlp. The link is put under the reference list at the end of the README file.

- “Sentimental Analyser” is a different python file created to help us with Sentiment Analysis. We create a naïve bayes model to decide between “Negative” and “Positive” Sentences. This model is used to analyze how users react to it.

- “GUI” is a class that is used to initialize everything related to our Graphical User Interface such as images, pages, etc.

- Class “Home” is the class for our home page in the Graphical User Interface and it contains all features present on that page.

- Class “Recent”, is used to record and store recent conversation dialogue in our recent conversation page in the Graphical User Interface. It contains all features present on that page.
- # Update
- Class "FlickrAPI" is used in our chatbot to import and show images from "flickr.com". It is integrated with "wikipedia" so that bot tries search for image based of the wikipedia search results and displays them besides it.
- Class "googletrans" is used to generate translation based on "Google Translator". So it detects the language and if it is not in English then our chatbot replies with the language detected.

<br>

## Data Flow Diagrams (DFD)

- Level 0: 

    - Image: ![Level-0 DFD](https://media.discordapp.net/attachments/798946362313408572/825163035822915614/Level_0.png)

    - Explain: This is our level 0 DFD, as you can see we have two entities namely, the user that is using the chatbot and the developers, which would be our entire team. The way the developers interact with the chatbot is by implementing new features fixing any bugs etc.


- Level 1: 

    - Image: ![Level-1 DFD](https://media.discordapp.net/attachments/798946362313408572/824776257337032764/DFD_Level_1.jpeg?width=942&height=718)

    - Explain: This right here is our level 1 DFD. Like the level 0 DFD we still have our developer and user as our entities. We have our synonym recognition, POS tagging and sentiment analysis as our processes. Our synonym recognition process works on the intents that is already in the dataset. Whereas the POS and sentimental works when only when the user has typed something on the UI and the bot prepares its response by picking required response from the dataset which is symbolized by the datastore at the bottom. We have another datastore that stores the conversation log named “conversation log”, the option to store this conversation comes from the UI.

<br>

## A List of 5 features that can be shared to others as API

- POS Tagging: includes the ability to searching on wikipedia and give responses based on that.

- Python file "SentimentalAnalyzer": a file that implements sentiment analysis

- Our chat bot: an application for others to view and modify.

- The method "remove_noise": removes all unnecessary words from a sentence

- Our Graphical User Interface

<br>

## Features: 

- Synonym recognition

    - Function: It identifies synonyms within sentences and give corresponding answers. It allows users to make inputs more diversified and give correct answers at the same time

    - Snippet: ![Synonym Recognition](https://media.discordapp.net/attachments/798946362313408572/825077522916048986/Screen_Shot_2021-03-26_at_11.42.51_AM.png)

- Sentiment analysis

    - Function: It recognizes user input that contains positive, negative, or neutral emotions and give corresponding answers without us having to code. It makes dialogue turns more lively and realistic.

    - Snippet: ![Sentiment Analysis](https://media.discordapp.net/attachments/798946362313408572/823878297989546004/unknown.png)

- POS tagging

    - Function: It gets the information about Proper Nouns that our bot doesn't know and searching them real time on wikipedia. With this feature, our chatbot is able to answer topics that are outside of our designed topic and the users might get more satisfaction throughout conversations.

    - Snippet: ![POS Tagging](https://media.discordapp.net/attachments/798946362313408572/823878799355674624/unknown.png)

- Recent Conversation Page (Updated)

    - Function: It saves dialogue information everytime our users say "bye" or close the app. With this feature, our users are able to check the dialogue history which is convenient.

    - Snippet: ![Recent Conversation Page](https://media.discordapp.net/attachments/798946362313408572/823879216525344768/unknown.png)
    
    - Update: Now the recent conversations also save the wikipedia searches which it didn't in the previous version.
  
    - Snippet: ![New Recent Converstion Page](https://cdn.discordapp.com/attachments/672366653585096736/832031078914457630/unknown.png)


# For Individual Project:
- Wikipedia (Update):
    - Function: To search the wikipedia if encountered by 'Proper Nouns' in the user input. Earlier there were some errors in which you had nouns with more than one word then if won't search the complete phrase/nouns instead just part of it. Also, wikipedia tried to provide suggestions in the searches made which gave errors and wrong results. These things were removed and auto suggestions was turned off to provide better output.
    - Before: ![Old Wikipedia](https://cdn.discordapp.com/attachments/672366653585096736/832034208758497290/unknown.png)
        
    - After: ![New Wikipedia](https://cdn.discordapp.com/attachments/672366653585096736/832033247949094952/unknown.png)\
    
    - Code: ![Auto Suggest](https://cdn.discordapp.com/attachments/672366653585096736/832035190494068746/unknown.png)

- Flickr:
    - Function: Topped with wikipedia search, this API searches for relevent images on "flickr.com". It also checks if the image exists on the flickr and if doesn't then it informs the user about it.
    - Example: ![Flickr Example](https://cdn.discordapp.com/attachments/672366653585096736/832037460384022609/unknown.png)

    - Code part 1: ![Code Flickr1](https://cdn.discordapp.com/attachments/672366653585096736/832040190242717738/unknown.png)
     
    - Code part 2: ![Code Flickr2](https://cdn.discordapp.com/attachments/672366653585096736/832040190242717738/unknown.png)
- Google Translator:
    - Function: It detects the input language by the user and converses in that language. This encloses the searches made using wikipedia and also the recent conversation also is stored in that language.
    - Example 1: ![Trans1](https://cdn.discordapp.com/attachments/672366653585096736/832051581946953728/unknown.png)
    
    - Example 2: ![Trans2](https://cdn.discordapp.com/attachments/672366653585096736/832056008704131102/unknown.png)
    
    - Code 1: ![Trans Code 1](https://cdn.discordapp.com/attachments/672366653585096736/832056866770911303/unknown.png)
    
    - Code 2: ![Trans Code 2](https://cdn.discordapp.com/attachments/672366653585096736/832057205904769075/unknown.png)
    
    - Code 3: ![Trans Code 3](https://cdn.discordapp.com/attachments/672366653585096736/832057619417399316/unknown.png)

<br>

## References

Here is the link of an open-source program that helps us build our chatbot
https://data-flair.training/blogs/python-chatbot-project/

Here is the link of stanfordcorenlp which is a Python wrapper for Stanford CoreNLP.
https://github.com/Lynten/stanford-corenlp
