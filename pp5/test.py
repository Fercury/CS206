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

def find_starters(ngrams):
  ret = set()
  for word in ngrams :
      if word[0] == '.' :
        ret.add(word)
  return ret

ng3 = {('of', 'the', 'bees'), ('bee', 'is', 'the'), ('the', 'bee', 'is'), 
       ('is', 'the', 'bee'), ('bee', 'of', 'the'), ('the', 'bee', 'of')}

s = dict()
n = 3
for word in ng3 :
    key = word[0:n-1]
    if key in s :
        s[key].add(word[n-1])
    else :
        s[key] = {word[n-1]}
print(s)