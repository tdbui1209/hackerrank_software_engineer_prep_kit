def binarySearch(nums: list[int], target: int) -> int:
    result = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            return result
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
