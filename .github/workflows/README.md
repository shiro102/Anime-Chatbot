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
      - input: 
      - expected output: 
      - actual output: 

   - Test2: 
      - input: 
      - expected output: 
      - actual output: 

   - Test3: 
      - input: 
      - expected output: 
      - actual output: 

2. word_bag(s, words)

   - Test1: 
      - input: 
      - expected output: 
      - actual output: 

   - Test2: 
      - input: 
      - expected output: 
      - actual output: 

   - Test3: 
      - input: 
      - expected output: 
      - actual output: 

3. remove_noise(tweet_tokens, stop_words = ())

   - Test1: 
      - input: 
      - expected output: 
      - actual output: 

   - Test2: 
      - input: 
      - expected output: 
      - actual output: 

   - Test3: 
      - input: 
      - expected output: 
      - actual output: 

