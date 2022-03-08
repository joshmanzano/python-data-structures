# Double Link
class Node:
  def __init__(self, value=None):
    self.value = value
    self.prev_node = None
    self.next_node = None
  def set_prev_node(self, new_node):
    self.prev_node = new_node
  def set_next_node(self, new_node):
    self.next_node = new_node

# Doubly Linked List
class LinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  def __len__(self):
    length = 0
    current_node = self.head_node
    while current_node:
      length += 1
      current_node = current_node.next_node
    return length
  def __iter__(self):
    list = []
    current_node = self.head_node
    while current_node:
      list.append(current_node.value)
      current_node = current_node.next_node
    return iter(list)
      
  def __repr__(self):
    repr = f'A doubly linked list of length {len(self)}:\n'
    repr += '<-> '
    current_node = self.head_node
    head_node = self.head_node
    tail_node = None
    while current_node:
      repr += str(current_node.value) + ' <-> '
      if current_node.next_node == None:
        tail_node = current_node
      current_node = current_node.next_node
    repr += '\n'
    if head_node and tail_node:
      repr += f'Head: {str(head_node.value)}, Tail: {str(tail_node.value)}'
    else:
      repr += f'Head: {None}, Tail: {None}'
    return repr
  def add_to_head(self, new_node):
    if new_node is not Node:
      new_node = Node(new_node)
    if self.head_node == None:
      self.head_node = new_node
      assert self.tail_node == None
      self.tail_node = new_node
    else:
      new_node.set_next_node(self.head_node)
      self.head_node.set_prev_node(new_node)
      self.head_node = new_node
  def add_to_tail(self, new_node):
    if new_node is not Node:
      new_node = Node(new_node)
    if self.tail_node == None:
      self.tail_node = new_node
      assert self.head_node == None
      self.head_node = new_node
    else:
      new_node.set_prev_node(self.tail_node)
      self.tail_node.set_next_node(new_node)
      self.tail_node = new_node
  def remove_head(self):
    current_head = self.head_node
    if self.head_node == None:
      return None
    if self.head_node.next_node == None:
      self.head_node = None
      self.tail_node = None
    else:
      self.head_node = self.head_node.next_node
      self.head_node.prev_node = None
    return current_head
  def remove_tail(self):
    current_tail = self.tail_node
    if self.tail_node == None:
      return None
    if self.tail_node.prev_node == None:
      self.head_node = None
      self.tail_node = None
    else:
      self.tail_node = self.tail_node.prev_node
      self.tail_node.next_node = None
    return current_tail
    
  def get_head(self):
    return self.head_node
    
  def get_tail(self):
    return self.tail_node

class Queue:
  def __init__(self):
    pass