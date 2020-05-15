from soundex import Soundex
from collections import defaultdict
from wordfreq import word_frequency

soundex = Soundex().soundex

sound_words = defaultdict(set)

with open('eff_short_wordlist_1.txt','r') as fh:
    for line in fh:
        word = line.split()[1]
        sound = soundex(word)
        if len(sound) > 1: # and sound not in ('i245', 't651'):
            sound_words[sound].add(word)

for word_set in sound_words.values():
    if len(word_set) > 1:
        word_list = [ (word_frequency(word, 'en'), word) for word in word_set ]
        word_list.sort()
        print(word_list[-1][-1])
    else:
        print(list(word_set)[0])
