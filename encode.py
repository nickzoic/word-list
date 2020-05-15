with open("word_list.txt","r") as fh:
    words = [ w.strip() for w in fh.readlines() ]

import sys

while True:
    s = sys.stdin.buffer.read(8)
    if len(s) == 0: break
    ww = [ words[c+n%2*256] for n, c in enumerate(s) ]
    print(" ".join(ww))
