class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check to see if the value needs to go down LHSS or RHS of node
    # if LHS
    if value < self.value:
      if not self.left:
        # insert at self.left if the node currently doesn't have one
        self.left = BinarySearchTree(value)
      else:
        # otherwise recursively go over the steps above with self.left
        self.left.insert(value)
    # if  RHS
    elif value >= self.value:
      if not self.right:
        # insert at self.right if the node currently doesn't have one
        self.right = BinarySearchTree(value)
      else:
        # otherwise recursively go over the steps above with self.right
        self.right.insert(value)

  def contains(self, target):
    # return True if target is equal to self.value
    if target == self.value:
      return True
    # else if target is smaller, search left
    elif target < self.value:
      if self.left:
        # if self.left exists, call contains method
        return self.left.contains(target)
      else:
        # otherwise, return False
        return False
    # else if target is larger, search right
    elif target >= self.value:
      if self.right:
        # if self.right exists, call contains method
        return self.right.contains(target)
      else:
        # otherwise, return False
        return False
  
  def get_max(self):
    # check to see if we're already at the max value
    if not self.right:
      return self.value
    # otherwise keep moving right
    else:
      return self.right.get_max()

  def for_each(self, cb):
    # cb on current node
    cb(self.value)
    # check to see if node has a left and a right
    if self.left:
      # initiate cb on left
      self.left.for_each(cb)
    if self.right:
      # initate cb on right
      self.right.for_each(cb)
      