#
# Implementation of dict using a Binary Search Tree
#  WITHOUT recursion for insertion and deletion
#

class _Node():
  def __init__(self, key, value, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

  # This method is still recursive
  # We will only use it for small trees to test your methods
  def _description(self, level):
    ls = self.left._description(level+1) if self.left else ""
    rs = self.right._description(level+1) if self.right else ""
    return ls + str(self.key) + ("(%d) " % level) + rs

  def _find_first(self):
    p = self
    while p.left is not None:
      p = p.left
    return p

  def _find_last(self):
    p = self
    while p.right is not None:
      p = p.right
    return p

  def _find(self, key):
    while self != None :
        if key == self.key :
            return self
        elif key > self.key :
            self = self.right
        else :
            self = self.left
    return None

  def _insert(self, key, value):
    while True :
        if key == self.key :
            self.value = value
            break
        elif key > self.key :
            if self.right == None :
                self.right = _Node(key, value)
                break
            else :
                self = self.right
        else :
            if self.left == None :
                self.left = _Node(key, value)
                break
            else :
                self = self.left

  # Remove node with smallest key in the subtree rooted at this node
  # Returns the new root.
  def _remove_first(self):
    root = self
    if root.left == None :
        return root.right
    while self.left.left != None :
        self = self.left
    self.left = self.left.right
    return root


  # Returns the new root.
  def _remove(self, key):
    root = self
    bnode = self
    rbnode = self
    dnode = self._find(key)

    if dnode is None :
        return root


    while not (bnode is dnode or bnode.left is dnode or bnode.right is dnode) :
        if key > bnode.key :
           bnode = bnode.right
        else :
           bnode = bnode.left

    if bnode is dnode :
        bnode = None

    if dnode.left != None :
        if dnode.right != None :
            rnode = dnode.right._find_first()
            
            while not (rbnode.left is rnode or rbnode.right is rnode) :
                if rnode.key > rbnode.key :
                   rbnode = rbnode.right
                else :
                   rbnode = rbnode.left

            if rbnode != dnode :
                rbnode.left = rnode.right 

                if rnode != dnode.right :
                    rnode.right = dnode.right
                rnode.left = dnode.left

            else :
                rnode.left = dnode.left

            if bnode is not None :
                if bnode.left is dnode :
                    bnode.left = rnode
                else : 
                    bnode.right = rnode
            else :
                root = rnode
                
        else :
            if bnode is not None :
                if bnode.left is dnode :
                    bnode.left = dnode.left
                else : 
                    bnode.right = dnode.left
            else :
                root = dnode.left
    else :
        if bnode is not None :
            if bnode.left is dnode :
                bnode.left = dnode.right
            else : 
                bnode.right = dnode.right
        else :
            root = dnode.right

    return root
# --------------------------------------------------------------------

class dict():
  def __init__(self):
    self._root = None

  def __str__(self):
    return self._root._description(0) if self._root else "[]"

  def _find(self, key):
    return self._root._find(key) if self._root else None

  def __getitem__(self, key):
    n = self._find(key)
    if n is None:
      raise KeyError(key)
    return n.value 

  def get(self, key, v = None):
    n = self._find(key)
    return n.value if n else v

  def __contains__(self, key):
    return self._find(key) is not None

  def __setitem__(self, key, value):
    if self._root is None:
      self._root = _Node(key, value)
    else:
      self._root._insert(key, value)

  def firstkey(self):
    return self._root._find_first().key if self._root else None

  def lastkey(self):
    return self._root._find_last().key if self._root else None

  def __delitem__(self, key):
    if self._root:
      self._root = self._root._remove(key)

# --------------------------------------------------------------------
