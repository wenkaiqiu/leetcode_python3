from typing import Dict


class Solution:
    """
    Python Easy-to-understand Recursive solution
    """
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        return self.eval_with_env(expression, {})

    def match_parenthesis(self, expression: str) -> Dict[int, int]:
        parenthesis = {}
        stack = []
        for i in range(len(expression)):
            if expression[i] == '(':
                stack.append(i)
            elif expression[i] == ')':
                j = stack.pop()
                parenthesis[j] = i
        return parenthesis

    def eval_with_env(self, expr: str, env: Dict[str, int]) -> int:
        if expr.startswith('('):
            parenthesis = self.match_parenthesis(expr)
            if expr.startswith("add", 1):  # (add operand1 operand2)
                if expr[5].isalpha() or expr[5].isnumeric() or expr[5] == '-':
                    sub_expr = expr[5:-1]  # type: str
                    operand_1, operand_2 = sub_expr.split(" ", 1)
                    return self.eval_with_env(operand_1, env.copy()) + self.eval_with_env(operand_2, env.copy())
                elif expr[5] == '(':
                    operand_1 = expr[5:parenthesis[5] + 1]
                    operand_2 = expr[parenthesis[5] + 2:-1]
                    return self.eval_with_env(operand_1, env.copy()) + self.eval_with_env(operand_2, env.copy())
            elif expr.startswith("mult", 1):  # (mult operand1 operand2)
                if expr[6].isalpha() or expr[6].isnumeric() or expr[6] == '-':
                    sub_expr = expr[6:-1]  # type: str
                    operand_1, operand_2 = sub_expr.split(" ", 1)
                    return self.eval_with_env(operand_1, env.copy()) * self.eval_with_env(operand_2, env.copy())
                elif expr[6] == '(':
                    operand_1 = expr[6:parenthesis[6] + 1]
                    operand_2 = expr[parenthesis[6] + 2:-1]
                    return self.eval_with_env(operand_1, env.copy()) * self.eval_with_env(operand_2, env.copy())
            elif expr.startswith("let", 1):  # (let identifier expr ... expr)
                rest = expr[5:-1]
                while True:

                    identifier, rest = rest.split(" ", 1)  # type: str, str
                    if rest[0].isnumeric() or rest[0] == '-':
                        value, rest = rest.split(" ", 1)
                        env[identifier] = int(value)
                    elif rest[0].isalpha():
                        sub_expr, rest = rest.split(" ", 1)
                        env[identifier] = self.eval_with_env(sub_expr, env.copy())
                    elif rest[0] == '(':
                        close_parenthesis_pos = self.match_parenthesis(rest)[0]
                        sub_expr = rest[:close_parenthesis_pos + 1]
                        rest = rest[close_parenthesis_pos + 2:]
                        env[identifier] = self.eval_with_env(sub_expr, env.copy())

                    if rest[0] == '(' or rest[0].isnumeric() or rest[0] == '-' or \
                            (rest[0].isalpha() and rest.find(" ") == -1):
                        return self.eval_with_env(rest, env.copy())

        elif expr[0].isnumeric() or expr[0] == '-':
            return int(expr)
        elif expr[0].isalpha():
            expr = expr.strip()
            return env[expr]


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
    ]
    for i in range(len(expression)):
        sol = Solution().evaluate(expression[i])
        print(sol)
        print("solution is right" if sol == output[i] else "solution is wrong")
