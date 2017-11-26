class Solution:
    class Tree:
        def __init__(self, val):
            self.nodes = []
            self.val = val

        def to_json(self):
            item = {'value': self.val, 'nodes': []}
            for node in self.nodes:
                item['nodes'].append(node.to_json())
            return item

    def build_tree_node(self, expression, parent):
        index = 0
        if index >= len(expression):
            return
        if expression[index] == ' ':
            index += 1
        if expression[index] == '(':
            op, rest = expression[index + 1:].split(' ', 1)
            new_node = self.Tree(op)
            parent[-1].nodes.append(new_node)
            parent.append(new_node)
            self.build_tree_node(rest, parent)
        elif expression[index] == ')':
            index += 1
            parent.pop()
            self.build_tree_node(expression[index:], parent)
        elif expression[index].isdigit() or expression[index]=='-':
            j = index
            while index < len(expression) and (expression[index].isdigit() or expression[index]=='-'):
                index += 1
            parent[-1].nodes.append(self.Tree(int(expression[j:index])))
            self.build_tree_node(expression[index:], parent)
        elif expression[index].isalpha():
            j = index
            while index < len(expression) and expression[index].isalnum():
                index += 1
            new_node = self.Tree(expression[j:index])
            parent[-1].nodes.append(new_node)
            self.build_tree_node(expression[index:], parent)

    def calc(self, tree, dict_in):
        dict = dict_in.copy()
        val = tree.val
        nodes = tree.nodes
        if val == 'let':
            length = len(nodes)
            i = 0
            while i < length - 1:
                var = nodes[i + 1].val
                dict[nodes[i].val] = var if type(var) is int else self.calc(nodes[i + 1], dict)
                i += 2
            return self.calc(nodes[-1], dict)
        elif val == 'add':
            return self.calc(nodes[0], dict) + self.calc(nodes[1], dict)
        elif val == 'mult':
            return self.calc(nodes[0], dict) * self.calc(nodes[1], dict)
        elif type(val) is int:
            return val
        else:
            return dict[val]

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        op, rest = expression[1:].split(' ', 1)
        tree = self.Tree(op)
        self.build_tree_node(rest, [tree])
        return self.calc(tree, {})


if __name__ == '__main__':
    expression = [
        '(add 1 2)',
        '(mult 3 (add 2 3))',
        '(let x 2 (mult x 5))',
        '(let x 2 (mult x (let x 3 y 4 (add x y))))',
        '(let x 3 x 2 x)',
        '(let x 1 y 2 x (add x y) (add x y))',
        '(let x 2 (add (let x 3 (let x 4 x)) x))',
        '(let a1 3 b2 (add a1 1) b2)',
        '(let x -2 y x y)'
    ]
    output = [
        3,
        15,
        10,
        14,
        2,
        5,
        6,
        4,
        -2
    ]
    for i in range(len(expression)):
        sol = Solution().evaluate(expression[i])
        print(sol)
        print("solution is right" if sol == output[i] else "solution is wrong")
