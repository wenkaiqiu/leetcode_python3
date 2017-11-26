# 733. Flood Fill
class Solution:
    situation = [
        [0, 1],  # up
        [1, 0],  # right
        [0, -1],  # down
        [-1, 0]  # left
    ]

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        image = image[:][:]
        lc = len(image)
        lr = len(image[0])
        old_color = image[sr][sc]
        image[sr][sc] = newColor
        for i in range(4):
            nc = sc + self.situation[i][0]
            nr = sr + self.situation[i][1]
            if 0 <= nc < lr and 0 <= nr < lc:
                if image[nr][nc] == old_color and image[nr][nc] != newColor:
                    self.floodFill(image, nr, nc, newColor)
        return image


if __name__ == '__main__':
    image = [
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        [[0, 0, 0], [0, 0, 0]]
    ]
    sr = [1, 0]
    sc = [1, 0]
    newColor = [2, 2]

    output = [
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        [[2, 2, 2], [2, 2, 2]]
    ]
    for i in range(len(image)):
        sol = Solution().floodFill(image[i], sr[i], sc[i], newColor[i])
        print(sol)
        print(sol == output[i])
