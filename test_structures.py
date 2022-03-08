import random
from data_structures import LinkedList

def test_linked_list(linked_list):
  amount = random.randint(10, 20)
  
  def populate_linked_list(linked_list):
    copy = []
    for _ in range(amount//2):
      value = random.randint(0, 100)
      linked_list.add_to_head(value)
      copy = [value] + copy
    for _ in range(amount//2):
      value = random.randint(0, 100)
      linked_list.add_to_tail(value)
      copy = copy + [value]
    return copy

  assert linked_list.head_node == None
  assert linked_list.tail_node == None
  
  ground_truth = populate_linked_list(linked_list)
  assert list(linked_list) == ground_truth
  assert linked_list.head_node.value == ground_truth[0]
  assert linked_list.tail_node.value == ground_truth[-1]

  for _ in range(amount//3):
    del ground_truth[0]
    linked_list.remove_head()
    assert list(linked_list) == ground_truth
    
  for _ in range(amount//3):
    del ground_truth[-1]
    linked_list.remove_tail()
    assert list(linked_list) == ground_truth

  while len(ground_truth) > 1:
    if random.randint(0,1):
      linked_list.remove_head()
      del ground_truth[0]
    else:
      linked_list.remove_tail()
      del ground_truth[-1]
    assert list(linked_list) == ground_truth
    assert linked_list.head_node.value == ground_truth[0]
    assert linked_list.tail_node.value == ground_truth[-1]
  
  linked_list.remove_head()  
  assert linked_list.head_node == None
  assert linked_list.tail_node == None

  return True

if __name__ == '__main__':
  pass