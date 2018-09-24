#
# DoublyLinkedList with Mergesort
#

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
  def __init__(self, *els):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
    for el in els:
      self.append(el)
  
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

# --------------------------------------------------------------------

  def median(self):
    "Returns the node in the middle of the list."
    a = self.first()
    b = self.last()
    while a != b :
        b = b.prev
        if a == b:
            return a
        a = a.next
    return a

  def split(self, n):
    "Removes all nodes after n from this list and returns them in a new DoublyLinkedList object."
    ret = DoublyLinkedList()
    try :
        m = self.last()
    except EmptyListError :
        return ret

    if n != m :
        ret._front.next = n.next
        n.next.prev = ret._front

        m.next = ret._rear
        ret._rear.prev = m

        n.next = self._rear
        self._rear.prev = n

    return ret


  def steal(self, other):
    "Moves first node in other list to the end of this list."
    n = other.first()
    try :
        m = self.last()
    except EmptyListError :
        m = self._front
  
    m.next = n
    n.prev = m

    other._front.next = n.next
    n.next.prev = other._front

    n.next = self._rear
    self._rear.prev = n

  def merge(self, other):
    "Merges elements from sorted other list into this sorted list."
    left = self.split(self._front)  # move all elements to a new list
    # now merge left and other
    n = left._front.next
    m = other._front.next
    while m.el != None and n.el != None :
        if n.el > m.el :
            self.steal(other)
            m = other._front.next
        else :
            self.steal(left)
            n = left._front.next

    while n.el != None :
        self.steal(left)
        n = left._front.next

    while m.el != None :
        self.steal(other)
        m = other._front.next


# --------------------------------------------------------------------

  def sort(self):
    # is length <= 1 ?
    if self.is_empty() or self._front.next.next == self._rear:
      return
    other = self.split(self.median())
    self.sort()
    other.sort()
    self.merge(other)

# --------------------------------------------------------------------