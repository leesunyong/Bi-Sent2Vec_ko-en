# Bi-Sent2Vec_ko-en
### Setting
Set up virtual environment


## Install Requirements

    python main.py download [params]
    
#### download all requirements
    python main.py download all
    
#### download only khaiii
    python main.py download khaiii
    

### nltk
Download nltk 'punkt': http://www.nltk.org/nltk_data/ <br>
Extract punkt.zip and move it to:
    
    /usr/local/share/nltk_data/tokenizers
Download nltk 'averaged_perceptron_tagger': http://www.nltk.org/nltk_data/ <br>
Extract averaged_perceptron_tagger.zip and move it to:
    
    /usr/local/share/nltk_data/taggers
    
## Implementation

    python main.py [module] [file name]
    
example
    
    python main.py process ko-en_sentences.txt
