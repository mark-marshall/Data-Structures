class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    self.size += 1
  
  def dequeue(self):
    if self.size:
      dequeue_el = self.storage[-1]
      del self.storage[-1]
      self.size -= 1
      return dequeue_el
    else:
      return None

  def len(self):
    return self.size
