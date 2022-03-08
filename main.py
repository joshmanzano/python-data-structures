from data_structures import Node, LinkedList 
from test_structures import test_linked_list

green_line = LinkedList()
test_result = 'Passed!' if test_linked_list(green_line) else 'Failed!'
print(f'Testing linked list implementation... {test_result}')
green_line.add_to_head('Guting')
print(green_line)
green_line.add_to_head('Taipower')
green_line.add_to_head('Gongguan')
print(green_line)