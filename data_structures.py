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
    if type(new_node) != Node:
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
    if type(new_node) != Node:
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
    self.queue = LinkedList()
  def __repr__(self):
    return f'Queue of size {len(self.queue)}'
  def enqueue(self, new_element):
    self.queue.add_to_tail(new_element)
  def dequeue(self):
    return self.queue.remove_head().value
  def peek(self):
    return self.queue.head_node.value
  def is_empty(self):
    return self.queue.head_node == None and self.queue.tail_node == None

class Stack:
  def __init__(self, max_size=None):
    self.stack = []
    self.max_size = max_size
    self.size = 0
  def __repr__(self):
    return str(self.stack)
  def is_empty(self):
    return self.size <= 0
  def has_space(self):
    if self.max_size:
      return self.size < self.max_size
    else:
      return True
  def push(self, new_element):
    if self.has_space():
      self.stack.append(new_element)
      self.size += 1
    else:
      raise Exception('Stack has no more space.')
  def pop(self):
    if self.is_empty():
      raise Exception('Stack is empty.')
    else:
      top_element = self.stack.pop(-1)
      self.size -= 1
      return top_element 
  def peek(self):
    return self.stack[-1]
    
class TreeNode:
  def __init__(self, value=None):
    self.value = value
    self.children = []
  def __repr__(self):
    return str(self.value)
  def add_child(self, child_node):
    if type(child_node) != TreeNode:
      child_node = TreeNode(child_node)
    self.children.append(child_node)
  def get_children(self):
    return self.children
  def get_value(self):
    return self.value
  def bfs(self):
    level = 0
    nodes_to_visit = Queue()
    nodes_to_visit.enqueue(self)
    while not nodes_to_visit.is_empty():
      current_node = nodes_to_visit.dequeue()
      print(current_node)
      for child in current_node.get_children():
        nodes_to_visit.enqueue(child)
  def dfs(self):
    nodes_to_visit = Stack()
    nodes_to_visit.push(self)
    while not nodes_to_visit.is_empty():
      current_node = nodes_to_visit.pop()
      print(current_node)
      for child in current_node.get_children():
        nodes_to_visit.push(child)