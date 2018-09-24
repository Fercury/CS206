#
# Dissociated Press
#

import random

# Read a text file and return a list of words
def read_text(fname):
  fd = open(fname, "r")
  wl = [ "." ]
  for s in fd.readlines():
    line = s.rstrip()
    words = line.split()
    for w in words:
      word = w.rstrip(",.':;?!-_\"").lstrip('\'"_').lower()
      wl.append(word)
      if w[-1] == "." and w.lower() != "dr.":
        wl.append(".")
  return wl

# take a list of words, and return set of all n-grams
def find_ngrams(wl, n):
  totlen = len(wl)
  ret = set()
  for i in range(totlen-n+1) :
      t = tuple(wl[i:i+n])
      ret.add(t)
  return ret

# given a set of ngrams, return a list of ngrams whose first word is "."
def find_starters(ngrams):
  ret = list()
  for word in ngrams :
      if word[0] == '.' :
        ret.append(word)
  return ret

# take set of n-grams, and return a map that maps (n-1)-grams
# to the set of all possible last words
def make_ngram_map(ngrams):
  ret = dict()
  n = len(list(ngrams)[0])
  for word in ngrams :
    key = word[0:n-1]
    if key in ret :
        ret[key].add(word[n-1])
    else :
        ret[key] = {word[n-1]}
  return ret

 
def print_word(w):
  if w != ".":
    print(" ", end="")
  print(w, end="")

#
# Generate and print a text consisting of count words,
# 
def dissociated_press(fname, n, count):
  words = read_text(fname)
  ngrams = find_ngrams(words, n)
  ngmap = make_ngram_map(ngrams)
  # start with a random n-gram that starts with a "period"
  starters = find_starters(ngrams)
  current = random.choice(starters)
  # skip period at the beginning and print first word without leading space
  print(current[1], end="")
  for w in current[2:]:   
    print_word(w)
  wcount = n
  while wcount < count:
    head = current[1:]                # take last n-1 words printed so far
    choices = ngmap.get(head)         # find n-grams starting with head
    if choices is None:
      print()
      return                          # cannot continue
    w = random.choice(list(choices))  # pick a random word 
    current = head + (w,)
    print_word(w)
    wcount += 1
  print()

if __name__ == "__main__":
  dissociated_press("kaist.txt", 2, 100)
  print()
  dissociated_press("independence.txt", 3, 100)
  print()
  dissociated_press("president.txt", 3, 100)
  print()
  dissociated_press("alice.txt", 4, 200)
