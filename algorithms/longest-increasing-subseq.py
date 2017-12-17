from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


def rec_lis(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        print(res)
        return res

    return max(L(i) for i in range(len(seq)))


def basic_lis(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)


from bisect import bisect


def lis(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        print('-------------------------')
        print(f'end {end}')
        print(f'val {val}')
        print(f'idx {idx}')
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    return len(end)


if __name__ == '__main__':
    print(lis([1, 0, 7, 2, 8, 3, 4, 9]))
