def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(1,3,4,5,6))
print(sum_numbers(1, 2, 3))          # Output: 6
print(sum_numbers(10, 20, 30, 40))   # Output: 100
print(sum_numbers())                # Output: 0
