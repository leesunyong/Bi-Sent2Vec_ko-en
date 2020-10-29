# Bi-Sent2Vec_ko-en
## Run

    python main.py

## Setting

    pip install -r requirements.txt
### Khaiii
Download khaiii

    git clone https://github.com/kakao/khaiii.git
    
Build Khaiii

    mkdir khaiii/build && cd khaiii/build
    cmake ..
    
    make all
    make resource

Test Khaiii is perfectly installed
    
    ctest

The result should be like below

        Start 1: test_khaiii
    1/1 Test #1: test_khaiii ......................   Passed    0.10 sec
    
    100% tests passed, 0 tests failed out of 1
    
Python binding
    
    make install
    make package_python
    
    cd package_python
    pip install .

<hr>
Khaiii Usage
    
    from Kahiii import KhaiiiApi
    
    api = KhaiiiApi()
    sentence = "곰 세마리가 한 집에 있어."
    for word in api.analyze(sentence)
        print(word)
        
Result
    
    곰	곰/NNG
    세마리가	세마리/NNG + 가/JKS
    한	한/MM
    집에	집/NNG + 에/JKB
    있어.	있/VV + 어/EF + ./SF

### nltk
Download nltk 'punkt': http://www.nltk.org/nltk_data/ <br>
Extract punkt.zip and move it to:
    
    /usr/local/share/nltk_data/tokenizers
Download nltk 'averaged_perceptron_tagger': http://www.nltk.org/nltk_data/ <br>
Extract averaged_perceptron_tagger.zip and move it to:
    
    /usr/local/share/nltk_data/taggers