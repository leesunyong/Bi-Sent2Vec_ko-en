import os
import zipfile
import shutil


def download(args):
    if args == 'all':
        _download_all()

    elif args == 'khaiii':
        if not os.path.isdir('./khaiii'):
            _download_khaiii()
        else:
            print("khaiii is already installed.")

    elif args == 'nltk_data':
        _download_nltk_data()


def _download_all():
    _download_package()
    _download_khaiii()
    _download_nltk_data()


def _download_package():
    # install requirements
    print("Download python packages.")
    os.system("pip3 install -r requirements.txt")


def _download_khaiii():
    # download khaiii from Github
    print("Download Khaiii")
    os.system("git clone https://github.com/kakao/khaiii.git")

    # build python
    os.system("mkdir khaiii/build")
    os.system("cd khaiii/build && cmake ..")

    os.system("cd khaiii/build && make all && make resource && ctest")

    # Python binding
    os.system("cd khaiii/build && make package_python")
    os.system("cd khaiii/build/package_python && pip3 install .")


def _download_nltk_data():
    nltk_data_url = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/"

    _download_tokenizer(nltk_data_url)
    _download_tagger(nltk_data_url)


def _download_tokenizer(url):
    punkt_url = "tokenizers/punkt.zip"
    os.system("wget " + url + punkt_url)
    _unzip('./punkt.zip', './')
    tokenizer_uri = "/usr/local/share/nltk_data/tokenizers"

    try:
        shutil.move('punkt', tokenizer_uri)
    except:
        shutil.rmtree('punkt')


def _download_tagger(url):
    averaged_perceptron_tagger = "taggers/averaged_perceptron_tagger.zip"
    os.system("wget " + url + averaged_perceptron_tagger)
    _unzip('./averaged_perceptron_tagger.zip', './')
    tagger_uri = "/usr/local/share/nltk_data/taggers"

    try:
        shutil.move('averaged-perceptron-tagger', tagger_uri)
    except:
        shutil.rmtree('averaged_perceptron_tagger')


def _unzip(filename, target):
    zip_file = zipfile.ZipFile(filename)
    zip_file.extractall(target)
    zip_file.close()

    os.remove(filename)
