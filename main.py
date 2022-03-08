from data_structures import TreeNode, Stack, Queue 

root = TreeNode('Josh')
left_child = TreeNode('Manzano')
right_child = TreeNode('Capule')
left_child.add_child('Hello')
left_child.add_child('Hello2')
right_child.add_child('Hi')
right_child.add_child('Hi2')
root.add_child(left_child)
root.add_child(right_child)
root.dfs()