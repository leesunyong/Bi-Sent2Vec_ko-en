from analyzer import *


# split sentence by whitespace tab('\t')
def _split_sentence(sentence):
    return sentence.split('\t')


# To use Bi-Sent2Vec all tokens should be tagged like '형태소_ko' or 'WORD_en'
def _tok_to_tagged_sent(tokens, lang):
    return ('_%s ' % lang).join(tokens)


def _tag_sentence(sentence, lang):
    tokens = get_morpheme(sentence, lang)
    return _tok_to_tagged_sent(tokens, lang)


def process_data_file(file_name):
    processed_file = "ko-en.txt"

    i = 0
    with open(processed_file, "w") as f:
        with open(file_name, "r") as f_raw:
            while True:
                sentence = f_raw.readline()

                if sentence is None:
                    break

                ko_sent_raw, en_sent_raw = _split_sentence(sentence)

                ko_sent = _tag_sentence(ko_sent_raw, "ko")
                en_sent = _tag_sentence(en_sent_raw, "en")

                f.write("%s <<split>> %s\n" % (ko_sent, en_sent))

                i += 1
                if i % 10000 == 0:
                    print("{0:,d} sentences are written.".format(i))
