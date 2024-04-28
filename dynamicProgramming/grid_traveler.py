from pprint import pprint
"""
Given a grid of dimensions m X n, starting in the top left, find the number of ways to reach the bottom right square, where the possible moves are restricted to down and right

Dynamic programming solution:
initialize a m X n array of zeros, dp
set dp[1][1] to 1
fill in the grid, where dp[a][b] = dp[a][b-1] + dp[a-1][b]
answer is dp[m][n]
"""

def gridTraveler(m: int, n: int) -> int:
    if m < 0 or n < 0:
        return -1
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[1][1] = 1
    for x in range(1, m+1):
        for y in range(1, n+1):
            if x == y == 1:
                continue
            dp[x][y] = dp[x-1][y] + dp[x][y-1]
    return dp[m][n]


if __name__ == "__main__":
    print(gridTraveler(2,3))
    print(gridTraveler(3,3))
    print(gridTraveler(255, 255))
    print(gridTraveler(1016, 413))