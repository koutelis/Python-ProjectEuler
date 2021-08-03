#PROBLEM 18 – Maximum path sum I
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
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
    for line in read_file('./files/0018_triangle.txt').split('\n'):
        nums = line.split()
        depth = len(nums) - 1
        all_nodes += [Node(int(num), depth) for num in nums]

    # feed list of Nodes to Tree
    tree = Tree(all_nodes)
    print(tree.max_path())
