class Solution(object):
    """
    Python solution using a stack for scope, 48ms

    Very brief explanation. Whenever '(' is scanned, we create new dictionary on a stack called scope. The
    dictionary will record three information: (1) the "MODE" of current scope (add, multi or let), (2) "VAL"(nums
    to calculate the return value of current scope, for "multi" or "add" the size is 2, for "let" the size is 1),
    and (3) variable value (v1, e1) (v2, e2) etc.

    Then when ')' is scanned, we will calculate the return value of last scope and pop the last scope. We pass
    the return value to updated last scope or simply return it if there is no scope left.

    Beside "(", ")", we can encounter three types of value: (1) key word of "MODE" like "add", "multi", and
    "let", it is always after '(' (2) variable name. If the MODE is "add" or "multi" or there is no space after,
    it actually represents a value, so we scan the scope reversely to find the innermost scope that has this
    variable, append the value to "VAL". If the MODE is "let" and there is a space after, this is a variable name
    and we store it in 'NXT' of current scope. (3) Value. If the MODE is "let" and there is a 'NXT', we assign
    this value to a variable, else we append this value to "VAL".
    """

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        scope = list()
        return self.evaluateWithScope(expression, scope)

    def evaluateWithScope(self, expression, scope):

        def insertVal(scope, val):
            if scope[-1]['MODE'] == 'let' and 'NXT' in scope[-1]:
                name = scope[-1].get('NXT')
                scope[-1][name] = val
                scope[-1].pop('NXT')
            else:
                scope[-1].setdefault('VAL', []).append(val)

        n = len(expression)
        i = 0

        while i < n:
            print(scope)
            if expression[i] == ' ':
                i += 1

            elif expression[i] == '(':
                scope.append(dict())
                j = expression.find(' ', i)
                scope[-1]['MODE'] = expression[i + 1:j]
                i = j + 1

            elif expression[i].isalpha():
                j = i
                while j < n and expression[j].isalnum():
                    j += 1

                name = expression[i:j]
                mode = scope[-1]['MODE']

                if mode == 'let' and expression[j] == ' ':
                    scope[-1]['NXT'] = name
                else:
                    for s in scope[::-1]:
                        if name in s:
                            val = s[name]
                            break
                    scope[-1][name] = val
                    scope[-1].setdefault('VAL', []).append(val)

                i = j

            elif expression[i].isdigit() or expression[i] == '-':
                j = i + 1
                while j < n and expression[j].isdigit():
                    j += 1
                val = int(expression[i:j])

                insertVal(scope, val)

                i = j

            elif expression[i] == ')':
                i += 1
                val = None
                mode = scope[-1]['MODE']
                VAL = scope[-1]['VAL']

                if mode == 'let':
                    val = VAL[0]
                elif mode == 'add':
                    val = VAL[0] + VAL[1]
                elif mode == 'mult':
                    val = VAL[0] * VAL[1]

                scope.pop()
                if len(scope) == 0:
                    return val
                else:
                    insertVal(scope, val)


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
