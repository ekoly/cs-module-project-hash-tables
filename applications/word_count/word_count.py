import re
from collections import defaultdict
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

def word_count(s):
    words = [
        re.sub(r"[^a-z0-9]", "", t.lemma_.lower()).strip() for t in tokenizer(s)
        if t.text.strip() and not t.is_punct
    ]
    w2c = defaultdict(lambda: 0)
    for word in words:
        if not word:
            continue
        w2c[word] += 1
    return {**w2c}



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
