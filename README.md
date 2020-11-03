# Bi-Sent2Vec_ko-en
## Setting
Set up virtual environment

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

### nltk
Download nltk 'punkt': http://www.nltk.org/nltk_data/ <br>
Extract punkt.zip and move it to:
    
    /usr/local/share/nltk_data/tokenizers
Download nltk 'averaged_perceptron_tagger': http://www.nltk.org/nltk_data/ <br>
Extract averaged_perceptron_tagger.zip and move it to:
    
    /usr/local/share/nltk_data/taggers
    
##Implementation

    python main.py [file name]
    
example
    
    python main.py ko-en_sentences.txt 
    
    
    
### Gensim Installation Error