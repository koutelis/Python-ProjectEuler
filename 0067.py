#PROBLEM 67 – Maximum path sum II
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in 0067_triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, as there are 299 altogether! 
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
"""

class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node
    
    def is_leaf(self):
        return self.left is None and self.right is None


class Tree:
    def __init__(self, nodes):
        self.memo = {node: None for node in nodes}  # memoization map
        self.nodes = nodes
        self.root = nodes[0]
        self.__arrange()

    def __str__(self):
        res = ''
        depth = self.root.depth
        for node in self.nodes:
            if node.depth != depth:
                depth = node.depth
                res += '\n'
            res += str(node) + ' '

        return res

    def __arrange(self):
        for i in range(len(self.nodes)):
            current = self.nodes[i]
            left_pos = current.depth + i + 1
            right_pos = left_pos + 1
            if left_pos < len(self.nodes):
                self.nodes[i].add_left(self.nodes[left_pos])
                self.nodes[i].add_right(self.nodes[right_pos])
    
    def max_path(self):
        return self._max_path(self.root)
    
    def _max_path(self, node):
        # base case
        if node.is_leaf():
            return node.value
        # recursion with memoization
        if self.memo[node] is None:
            self.memo[node] = max(self._max_path(node.left), self._max_path(node.right))
        return node.value + self.memo[node]


def read_file(filepath):
    # return inp
    with open(filepath, 'r') as f:
        return f.read()


if __name__ == "__main__":
    # get list of Nodes from input
    all_nodes = []
    for line in read_file('./0067_triangle.txt').split('\n'):
        nums = line.split()
        depth = len(nums) - 1
        all_nodes += [Node(int(num), depth) for num in nums]

    # feed list of Nodes to Tree
    tree = Tree(all_nodes)
    print(tree.max_path())
