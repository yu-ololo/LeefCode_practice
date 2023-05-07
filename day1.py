# %% 二分探索
nums = [-1, 0, 3, 5, 9, 12]
target = 9
left = -1
right = len(nums)
# std::lower_bound()
while right - left > 1:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid
    else:
        right = mid

# %% bad version
m = 5
bad = 4


def isBadVersion(version):
    return version >= bad


def firstBadVersion(n):
    left = -1
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid
    return right


print(firstBadVersion(m))
# %%
n = 2021


def numSquares(n):
    n = int(n)
    dp = [0] * (n + 1)
    print(dp)
    for i in range(1, n + 1):
        dp[i] = i
        for j in range(1, i):
            if j * j > i:
                break
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        print(dp)
    return dp[n]


print(numSquares(n))
