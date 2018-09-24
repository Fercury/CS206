#
# A circular doubly-linked list
#

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class CircularList:
  def __init__(self, el):
    n = Node(el)
    n.next = n
    n.prev = n
    self._head = n
  
  def first(self):
    return self._head

  def __repr__(self):
    res = "["
    n = self.first()
    while True :
        res += str(n.el)
        if n.next == self.first() :
            break
        n = n.next
        res += ", "
    res += "]"
    return res

  def remove(self, p):
    if len(self) == 1 :
        raise ValueError("Cannot remove only node of a CircularList")
    if p is self.first() :
        self._head = p.next
    p.prev.next = p.next
    p.next.prev = p.prev

  def __len__(self):
    cnt = 1
    n = self.first()
    while n.next != self.first() :
        cnt += 1
        n = n.next
    return cnt

  def insert(self, p, el):
    n = Node(el, p, p.prev)
    p.prev.next = n
    p.prev = n

  def append(self, x):
    self.insert(self.first(), x)