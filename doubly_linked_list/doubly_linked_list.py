"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # check to see if current doubly-linked list is empty
    if not self.length:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      # dont need to remove prev pointers as this is the head
      self.head.insert_before(value)
      self.head = self.head.prev
      # increment list length
      self.length += 1

  def remove_from_head(self):
    # store removed head value for later return
    old_head = self.head.value
    # check to see if the dll will be empty after removal
    if self.length == 1:
      self.head.delete()
      self.head = None
      self.tail = None
    # oterhwise reassign head to the next val
    else:
      self.head = self.head.next
      self.head.prev.delete()
    # decerement dll length and return removed head
    self.length -= 1
    return old_head

  def add_to_tail(self, value):
    # wrap value in new node without method if the dll is empty
    if not self.length:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    # otherwise create the node using the insert_after method
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    # increment list length
    self.length += 1

  def remove_from_tail(self):
    # store removed tail value for later return
    old_tail = self.tail.value
    # check to see if the dll will be empty after removal
    if self.length == 1:
      self.tail.delete()
      self.head = None
      self.tail = None
    # oterhwise reassign tail to the previous val
    else:
      self.tail = self.tail.prev
      self.tail.next.delete()
    # decerement dll length and return removed tail
    self.length -= 1
    return old_tail

  def move_to_front(self, node):
    # check if the node has previous and next nodes
    if node.next and node.prev:
      node.prev.next = node.next
      node.next.prev = node.prev
    # check if the node just has a previous node
    elif node.prev:
      node.prev.next = None
    # check if the tail needs to be reassigned
    if self.length == 2:
      self.tail = self.head
    # reassign next/previous on moving node
    node.next = self.head
    self.head.prev = node
    # reassign head
    self.head = node
    node.prev = None

  def move_to_end(self, node):
    # check if the node has previous and next nodes
    if node.next and node.prev:
      node.prev.next = node.next
      node.next.prev = node.prev
    # check if the node just has a next node
    elif node.next:
      node.next.prev = None
    # check if the head needs to be reassigned
    if self.length == 2:
      self.head = self.tail
    # reassign next/previous on moving node
    node.prev = self.tail
    self.tail.next = node
    # reassign tail
    self.tail = node
    node.next = None

  def delete(self, node):
    # if the list length is 1, reset the dll
    if self.length == 1:
      self.head = None
      self.tail = None
      node.delete()
    # if the passed node is the head
    elif self.head == node:
      self.head = self.head.next
      node.delete()
    # if the passed node is the tail
    elif self.tail == node:
      self.tail = self.tail.prev
      node.delete()
    # if the passed node is neither the head nor the tail
    else:
      node.delete()
    # decrement list length by 1 in all cases
    self.length -= 1
    
  def get_max(self):
    # initialize current node and current max_val
    current = self.head
    max_val = self.head.value
    # loop over the list using .next
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next
    # return max value
    return max_val
