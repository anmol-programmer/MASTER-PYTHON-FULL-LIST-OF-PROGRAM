def flatten_list(nested):
    result = []
    for sublist in nested:
        result.extend(sublist)
    return result

print(flatten_list([[1, 2], [3, 4], [5]]))
