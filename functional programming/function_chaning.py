nums = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, nums))
)

print(result)

