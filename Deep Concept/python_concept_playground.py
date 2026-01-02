# ==============================
# Python Concepts Playground
# ==============================
import copy

def mutability_demo():
    print("\n--- Mutability Demo ---")
    lst1 = [1, 2, 3]
    lst2 = lst1
    lst2.append(4)
    print("List1:", lst1)
    print("List2:", lst2)
    print("ID List1:", id(lst1))
    print("ID List2:", id(lst2))

    s1 = "hello"
    s2 = s1
    s2 += " world"
    print("\nString demo:")
    print("S1:", s1)
    print("S2:", s2)
    print("ID S1:", id(s1))
    print("ID S2:", id(s2))

def identity_vs_equality_demo():
    print("\n--- Identity vs Equality Demo ---")
    a = 256
    b = 256
    print("256 == 256:", a == b, "| 256 is 256:", a is b)

    x = 257
    y = 257
    print("257 == 257:", x == y, "| 257 is 257:", x is y)

    l1 = [1, 2]
    l2 = [1, 2]
    print("[1,2] == [1,2]:", l1 == l2, "| [1,2] is [1,2]:", l1 is l2)

def copy_vs_reference_demo():
    print("\n--- Copy vs Reference Demo ---")
    orig = [1, 2, 3]
    ref = orig
    slice_copy = orig[:]
    deep_copy = copy.copy(orig)

    ref.append(4)
    slice_copy.append(5)
    deep_copy.append(6)

    print("Original:", orig)
    print("Reference:", ref)
    print("Slice Copy:", slice_copy)
    print("Shallow Copy:", deep_copy)

def truthy_falsy_demo():
    print("\n--- Truthy / Falsy Demo ---")
    user_input = input("Enter something: ")
    if user_input:
        print("Truthy input")
    else:
        print("Falsy input")

def mutable_default_arg_bug_demo():
    print("\n--- Mutable Default Argument Bug Demo ---")

    def buggy_add(item, lst=[]):
        lst.append(item)
        return lst

    def safe_add(item, lst=None):
        if lst is None:
            lst = []
        lst.append(item)
        return lst

    print("Buggy version:")
    print(buggy_add(1))
    print(buggy_add(2))

    print("Safe version:")
    print(safe_add(1))
    print(safe_add(2))

def main():
    while True:
        print("\n===== Python Concepts Playground =====")
        print("1. Mutability Demo")
        print("2. Identity vs Equality Demo")
        print("3. Copy vs Reference Demo")
        print("4. Truthy / Falsy Demo")
        print("5. Mutable Default Argument Bug Demo")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            mutability_demo()
        elif choice == '2':
            identity_vs_equality_demo()
        elif choice == '3':
            copy_vs_reference_demo()
        elif choice == '4':
            truthy_falsy_demo()
        elif choice == '5':
            mutable_default_arg_bug_demo()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
