from collections import deque

'''
Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

'''

d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())




d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
d                                # show the representation of the deque


d.pop()                          # return and remove the rightmost item

d.popleft()                      # return and remove the leftmost item

list(d)                          # list the contents of the deque

d[0]                             # peek at leftmost item

d[-1]                            # peek at rightmost item


list(reversed(d))                # list the contents of a deque in reverse

'h' in d                         # search the deque

d.extend('jkl')                  # add multiple elements at once
d

d.rotate(1)                      # right rotation
d

d.rotate(-1)                     # left rotation
d


deque(reversed(d))               # make a new deque in reverse order

d.clear()                        # empty the deque
d.pop()                          # cannot pop from an empty deque

     
    


d.extendleft('abc')              # extendleft() reverses the input order
d