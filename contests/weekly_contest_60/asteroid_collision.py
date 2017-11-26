# 735. Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        tag = False
        length = len(asteroids) - 1
        i = 0
        while i < length:
            if asteroids[i] > 0 > asteroids[i + 1]:
                abs_cur = abs(asteroids[i])
                abs_post = abs(asteroids[i + 1])
                if abs_cur > abs_post:
                    asteroids.pop(i + 1)
                    length -= 1
                if abs_cur < abs_post:
                    asteroids.pop(i)
                    length -= 1
                if abs_cur == abs_post:
                    asteroids.pop(i + 1)
                    asteroids.pop(i)
                    length -= 2
                tag = True
            i += 1
        if tag:
            return self.asteroidCollision(asteroids)
        else:
            return asteroids


if __name__ == '__main__':
    asteroids = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [-2, -2, 1, -2],
    ]
    output = [
        [5, 10],
        [],
        [10],
        [-2, -2, -2]
    ]
    for i in range(len(asteroids)):
        sol = Solution().asteroidCollision(asteroids[i])
        print(sol)
        print("solution is right" if sol == output[i] else "solution is wrong")
