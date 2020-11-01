import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
import re
from collections import defaultdict
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

w2w = defaultdict(lambda: [])
words = [re.sub(r"[^a-z0-9]", "", t.lemma_.lower()).strip() for t in tokenizer(words)
         if not t.is_punct and t.text.strip()]
for word1, word2 in zip(words, words[1:]):
    w2w[word1].append(word2)


# TODO: construct 5 random sentences
# Your code here
import random

for _ in range(5):
    word = random.choice(list(w2w.keys()))
    sentence = [word]
    for _ in range(random.randint(4, 12)):
        following = w2w[word]
        if following:
            word = random.choice(following)
            sentence.append(word)
        else:
            break
    print(" ".join(sentence))
