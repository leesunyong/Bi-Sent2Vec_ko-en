from khaiii import KhaiiiApi
import nltk

api = KhaiiiApi()


def _get_morph_ko(sentence):
    morphs = []

    for word in api.analyze(sentence):
        length = len(word.morphs)

        for i in range(length):
            morphs.append(str(word.morphs[i]).replace("/", "_"))

    return morphs


def _get_morph_en(sentence):
    morphs = []

    tokens = nltk.word_tokenize(sentence)
    for tag in nltk.pos_tag(tokens):
        morphs.append(tag[0].lower() + "_" + tag[1])

    return morphs


def get_morpheme(sentence, lang):
    if lang == 'ko':
        return _get_morph_ko(sentence)
    elif lang == 'en':
        return _get_morph_en(sentence)
    else:
        print("Wrong language code, 'ko, en' only")
        return


def tok_to_sentence(tokens):
    return ' '.join(tokens)
