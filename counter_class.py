from collections import Counter

c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))
print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)


print(c.total())                      # total of all counts
c.clear()                       # reset all counts
print(list(c))                         # list unique elements
print(set(c))                          # convert to a set
print(dict(c))                         # convert to a regular dictionary
print(c.items())                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# +c                              # remove zero and negative counts

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c+d)                      # add two counters together:  c[x] + d[x]

print(c - d)                      # subtract (keeping only positive counts)

print(c & d)                    # intersection:  min(c[x], d[x])

print(c | d)                     # union:  max(c[x], d[x])

print(c == d)                    # equality:  c[x] == d[x]

print(c <= d)


