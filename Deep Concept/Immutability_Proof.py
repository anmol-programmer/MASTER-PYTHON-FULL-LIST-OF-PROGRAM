text = "python"

print("Before modification:")
print("Value:", text)
print("ID:", id(text))

text = text + "123"

print("\nAfter modification:")
print("Value:", text)
print("ID:", id(text))
