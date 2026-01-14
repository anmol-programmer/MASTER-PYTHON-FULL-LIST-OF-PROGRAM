def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

visit_count = counter()

print(visit_count())
print(visit_count())
print(visit_count())
