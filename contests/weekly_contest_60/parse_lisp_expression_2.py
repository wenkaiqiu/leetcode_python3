import re


class Solution(object):
    """
    Somewhat concise python solution, mutual recursion, global dict of stacks
    """
    def evaluate(self, e):
        """
        :type expression: str
        :rtype: int
        """

        def evl(start, resolve=True):
            """eval a sexp. return the value, and the past-end index"""
            if e[start] == " ":
                start += 1

            m = re.match("[(](?:(let)|(add|mult))|(-?[0-9]+)|([^ )]+)", e[start:])
            assert (m)
            s = m.group(0)
            if m.group(1):
                return let(start)
            elif m.group(2):
                return addmult(start)
            elif m.group(3):
                val = int(s)
            else:
                print(s)
                var = s
                val = d[var][-1] if resolve else var
            return val, start + len(s)

        def let(start):
            """eval a let. return the value, and the past-end index"""
            vrs = []
            start += 5
            while True:
                var, start = evl(start, resolve=False)
                if e[start] == ")":
                    val = var if isinstance(var, int) else d[var][-1]
                    for v in vrs:
                        d[v].pop()
                    assert (e[start] == ')')
                    return val, start + 1
                else:
                    vrs.append(var)
                    val, start = evl(start)
                    d.setdefault(var, []).append(val)

        def addmult(start):
            """eval an add or mult. return the value, and the past-end index"""
            add = e[start + 1] == 'a'
            start += 5 if add else 6
            a, start = evl(start)
            b, start = evl(start)
            assert (e[start] == ')')
            return (a + b if add else a * b), start + 1

        d = {}
        val, end = evl(0)
        assert (len(e) == end)
        return val


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
