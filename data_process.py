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


def process_data_file(file_name, lang1, lang2):
    processed_file = "%s-%s.txt" % (lang1, lang2)

    i = 0
    with open(processed_file, "a") as f:
        with open(file_name, "r") as f_raw:
            while True:
                sentence = f_raw.readline()

                if sentence is None:
                    break

                lang1_sent_raw, lang2_sent_raw = _split_sentence(sentence)

                lang1_sent = _tag_sentence(lang1_sent_raw, lang1)
                lang2_sent = _tag_sentence(lang2_sent_raw, lang2)

                f.write("%s <<split>> %s\n" % (lang1_sent, lang2_sent))

                i += 1
                if i % 10000 == 0:
                    print("{0:,d} sentences are written.".format(i))
