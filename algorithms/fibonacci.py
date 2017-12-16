#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def fbis(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


def main():
    result = fbis(10)
    for i, num in enumerate(result):
        print("第%d个数是: %d" % (i, num))
        time.sleep(1)

if __name__ == '__main__':
    main()
