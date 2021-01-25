from binarytree import tree, bst, Node, build


class MyNode:
    def __init__(self, value, left=None, right=None, date=None):
        self.date = date
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return f'{self.value} {self.left} {self.right}'


a = tree(height=3, is_perfect=True)
print(a)
b = bst(height=3, is_perfect=True)
print(b)

root = Node(42)
root.left = Node(21)
root.right = Node(69)
root.left.left = Node(12)

# root = MyNode(42)
# root.left = MyNode(21)
# root.right =MyNode(69)

print(root)

r = build([1, 2, 3, 4, 5, 6, 7])
print(r)

bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input("Целое число для поиска: "))


def go(bin_tree, number, path=''):
    if number == bin_tree.value:
        return f'Число {number} находится по следующему пути: \nКорень{path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return go(bin_tree.left, number, path=f'{path}\nШаг в лево')
    if number > bin_tree.value and bin_tree.right is not None:
        return go(bin_tree.right, number, path=f'{path}\nШаг в право')


print(go(bt, num))
