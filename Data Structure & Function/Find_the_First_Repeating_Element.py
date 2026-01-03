def first_repeating(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return None   

print(first_repeating([10, 5, 3, 4, 3, 5, 6]))
