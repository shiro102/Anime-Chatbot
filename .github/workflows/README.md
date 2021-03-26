# Automated Unit Tesing

## When it works: 

The automated testing process will be triggered everytime something is pushed to the main branch or a pull-request is created on the main branch.

## What it does everytime it is triggered: <br>

   - At first, the automated testing file is run on a system called ubuntu machine, which is a common operating system for cloud computing. It checkout the repository to that system and set up Python 3.9 as the environment. 

   - Then, it installs fundamental dependencies - pip, flake8, and pytest.Moreover, other packages can also be installed altogether such as nltk and numpy. After that, it reads these required dependencies into a txt file called requirements.txt. 
    
   - Next, the file lints with flake8 by running flake8 by some parameters so that the test will stop the  build if there are syntax errors or editing mistakes and treats all errors as warnings.
   - In the end, the automated testing runs all Python testing file to test the code.

## ***Test Cases***

1. lemma(s)
   - Test1: 
      - input: ""
      - expected output: []
      - actual output: []

   - Test2: 
      - input: "Far far away, behind the word mountains, far from the ... " (long text)
      - expected output: ['far', 'far', 'away', ',', 'behind', 'the', 'word', 'mountain', ',', 'far', 'from', 'the', ...] (long array)
      - actual output: ['far', 'far', 'away', ',', 'behind', 'the', 'word', 'mountain', ',', 'far', 'from', 'the', ...] (long array)

   - Test3: 
      - input: "@elonmusk how are you doing w/ ur rocket & spaceship? Can I buy it for ~$100 +- 5? (btw here's my email hello@gmail.com) ^^"
      - expected output: ['@', 'elonmusk', 'how', 'are', 'you', 'doing', 'w/', 'ur', 'rocket', '&', 'spaceship', '?', 'can', 'i', 'buy', 'it', 'for', '~', '$', '100', '+-', '5', '?', '(', 'btw', 'here', "'s", 'my', 'email', 'hello', '@', 'gmail.com', ')', '^^'] 
      - actual output: ['@', 'elonmusk', 'how', 'are', 'you', 'doing', 'w/', 'ur', 'rocket', '&', 'spaceship', '?', 'can', 'i', 'buy', 'it', 'for', '~', '$', '100', '+-', '5', '?', '(', 'btw', 'here', "'s", 'my', 'email', 'hello', '@', 'gmail.com', ')', '^^'] 

2. word_bag(s, words)

   - Test1: 
      - input: word_bag("", ["hello","how","are","you"])
      - expected output: [0,0,0,0]
      - actual output: [0,0,0,0]

   - Test2: 
      - input: word_bag("hello how are you?", [])
      - expected output: [0]
      - actual output: [0]

   - Test3: 
      - input: word_bag("", [])
      - expected output: [1]
      - actual output: [1]

3. remove_noise(tweet_tokens, stop_words = ())

   - Test1: 
      - input: ""
      - expected output: []
      - actual output: []

   - Test2: 
      - input: "!asda123$#@"
      - expected output: ['a', 's', 'd', 'a', '1', '2', '3']
      - actual output: ['a', 's', 'd', 'a', '1', '2', '3']

   - Test3: 
      - input: "你好，我正%在上C#OSC3!10"
      - expected output: ['你', '好', '，', '我', '正', '在', '上', 'c', 'o', 's', 'c', '3', '1', '0']
      - actual output: ['你', '好', '，', '我', '正', '在', '上', 'c', 'o', 's', 'c', '3', '1', '0']

