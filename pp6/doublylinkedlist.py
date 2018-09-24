
class EmptyListError(Exception):
  pass

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class DoublyLinkedList:
  def __init__(self):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
  
  def is_empty(self):
    return self._front.next == self._rear

  def first(self):
    if self.is_empty():
      raise EmptyListError
    return self._front.next

  def last(self):
    if self.is_empty():
      raise EmptyListError
    return self._rear.prev

  def __repr__(self):
    res = "["
    p = self._front.next
    while p != self._rear:
      res += str(p.el)
      if p.next != self._rear:
        res += ", "
      p = p.next
    res += "]"
    return res

  def __len__(self):
    p = self._front.next
    count = 0
    while p != self._rear:
      count += 1
      p = p.next
    return count

  def insert_after(self, n, el):
    p = Node(el, n.next, n)
    n.next.prev = p
    n.next = p

  def prepend(self, el):
    self.insert_after(self._front, el)
  
  def append(self, el):
    self.insert_after(self._rear.prev, el)

  def remove(self, n):
    n.prev.next = n.next
    n.next.prev = n.prev

  def find_first(self, x):
    if self.is_empty() :
        return None
    n = self.first()
    while n != self._rear :
        if n.el == x :
            return n
        n = n.next
    if n == self._rear :
        return None

  def find_last(self, x):
    if self.is_empty() :
        return None
    n = self.last()
    while n != self._front :
        if n.el == x :
            return n
        n = n.prev
    if n == self._front :
        return None

  def count(self, x): 
    n = self._front
    cnt = 0
    while n != self._rear :
        if n.el == x :
            cnt += 1
        n = n.next
    return cnt

  def remove_first(self, x):
    n = self.find_first(x)
    if n == None :
        return
    n.prev.next = n.next
    n.next.prev = n.prev

  def remove_last(self, x):
    n = self.find_last(x)
    if n == None :
        return
    n.prev.next = n.next
    n.next.prev = n.prev

  def remove_all(self, x):
    n = self.find_first(x)
    while n != None :
        self.remove_first(x)
        n = self.find_first(x)

  def takeout(self, n, m):
    n.prev.next = m.next
    m.next.prev = n.prev
    ret = DoublyLinkedList()
    ret._front.next = n
    ret._rear.prev = m
    n.prev = ret._front
    m.next = ret._rear
    return ret


