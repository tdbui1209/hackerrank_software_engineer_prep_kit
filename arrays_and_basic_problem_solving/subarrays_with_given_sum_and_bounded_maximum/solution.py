def countSubarraysWithSumAndMaxAtMost(nums: list[int], k: int, M: int) -> int:
    n = len(nums)
    count = 0
    i = 0

    while i < n:
        if nums[i] > M:
            i += 1
            continue
        
        prefix = {0: 1}
        s = 0

        while i < n and nums[i] <= M:
            s += nums[i]
            count += prefix.get(s - k, 0)
            prefix[s] = prefix.get(s, 0) + 1
            i += 1

    return count
