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

# %%
