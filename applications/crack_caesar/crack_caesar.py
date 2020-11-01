# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

frequencies = """
|   E    |    11.53   |
|   T    |     9.75   |
|   A    |     8.46   |
|   O    |     8.08   |
|   H    |     7.71   |
|   N    |     6.73   |
|   R    |     6.29   |
|   I    |     5.84   |
|   S    |     5.56   |
|   D    |     4.74   |
|   L    |     3.92   |
|   W    |     3.08   |
|   U    |     2.59   |
|   G    |     2.48   |
|   F    |     2.42   |
|   B    |     2.19   |
|   M    |     2.18   |
|   Y    |     2.02   |
|   C    |     1.58   |
|   P    |     1.08   |
|   K    |     0.84   |
|   V    |     0.59   |
|   Q    |     0.17   |
|   J    |     0.07   |
|   X    |     0.07   |
|   Z    |     0.03   |
"""
import re

letter_to_freq = {}
for row in frequencies.split("\n"):
    m = re.match(r"\|\s+(?P<letter>[A-Z])\s+\|\s+(?P<number>\d+\.\d+)\s+|", row)
    if m and m.group("letter") and m.group("number"):
        letter_to_freq[m.group("letter")] = float(m.group("number"))/100.

freq_to_letter = {v: k for k, v in letter_to_freq.items()}

with open("ciphertext.txt") as f:
    text = f.read()

from collections import defaultdict
letter_counts = defaultdict(lambda: 0)
for letter in text:
    letter = letter.upper()
    if 'A' <= letter and letter <= 'Z':
        letter_counts[letter] += 1

def get_closest(freq):
    return min(freq_to_letter.keys(), key=lambda x: abs(x-freq))

total = sum(x for x in letter_counts.values())
for letter, count in letter_counts.items():
    freq = count/total
    closest = freq_to_letter[get_closest(freq)].lower()
    text = text.replace(letter, closest)

print(text)
