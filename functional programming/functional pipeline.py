# Functional Pipeline: Filter Even Numbers and Square Them
numbers = [1, 2, 3, 4, 5, 6]

result = list(map(
    lambda x: x * x,
    filter(lambda x: x % 2 == 0, numbers)
))

print(result)
