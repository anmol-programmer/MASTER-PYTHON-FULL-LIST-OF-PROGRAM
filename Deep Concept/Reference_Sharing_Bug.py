list1 = [10, 20, 30]
list2 = list1    # reference sharing

list2.append(40)

print("list1:", list1)
print("list2:", list2)
