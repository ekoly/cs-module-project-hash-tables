# Your code here

import sys
import re
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer
from collections import Counter

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

with open(sys.argv[1]) as f:
    text = f.read()

words = [re.sub(r"[^a-z0-9]", "", t.lemma_.lower()).strip() for t in tokenizer(text)
         if not t.is_punct and t.text.strip()]
word_counts = Counter(words)

for word, count in word_counts.most_common():
    print(f"{word}" + " "*(16-len(word)) + "#"*count)
