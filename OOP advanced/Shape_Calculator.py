import math

class Shape:
    def area(self, *args):
        pass

    def perimeter(self, *args):
        pass

    def volume(self, *args):
        pass

class Rectangle(Shape):
    def area(self, l, w):
        return l * w

    def perimeter(self, l, w):
        return 2 * (l + w)

class Square(Shape):
    def area(self, s):
        return s * s

    def perimeter(self, s):
        return 4 * s

class Circle(Shape):
    def area(self, r):
        return math.pi * r * r

    def perimeter(self, r):
        return 2 * math.pi * r

class Triangle(Shape):
    def area(self, b, h):
        return 0.5 * b * h

    def perimeter(self, a, b, c):
        return a + b + c

class Cube(Shape):
    def area(self, a):
        return 6 * a * a

    def volume(self, a):
        return a ** 3

class Cuboid(Shape):
    def area(self, l, w, h):
        return 2 * (l*w + w*h + h*l)

    def volume(self, l, w, h):
        return l * w * h

class Sphere(Shape):
    def area(self, r):
        return 4 * math.pi * r * r

    def volume(self, r):
        return (4/3) * math.pi * r ** 3

class Cylinder(Shape):
    def area(self, r, h):
        return 2 * math.pi * r * (r + h)

    def volume(self, r, h):
        return math.pi * r * r * h

print("""
Choose Operation:
1. Area
2. Perimeter
3. Volume
""")

op = int(input("Enter choice: "))

print("""
Choose Shape:
1. Rectangle
2. Square
3. Circle
4. Triangle
5. Cube
6. Cuboid
7. Sphere
8. Cylinder
""")

shape = int(input("Enter shape number: "))

match op:

    case 1:
        match shape:
            case 1:
                l = float(input("Length: "))
                w = float(input("Width: "))
                print("Area =", Rectangle().area(l, w))

            case 2:
                s = float(input("Side: "))
                print("Area =", Square().area(s))

            case 3:
                r = float(input("Radius: "))
                print("Area =", Circle().area(r))

            case 4:
                b = float(input("Base: "))
                h = float(input("Height: "))
                print("Area =", Triangle().area(b, h))

            case 5:
                a = float(input("Side: "))
                print("Surface Area =", Cube().area(a))

            case 6:
                l = float(input("Length: "))
                w = float(input("Width: "))
                h = float(input("Height: "))
                print("Surface Area =", Cuboid().area(l, w, h))

            case 7:
                r = float(input("Radius: "))
                print("Surface Area =", Sphere().area(r))

            case 8:
                r = float(input("Radius: "))
                h = float(input("Height: "))
                print("Surface Area =", Cylinder().area(r, h))

    case 2:
        match shape:
            case 1:
                l = float(input("Length: "))
                w = float(input("Width: "))
                print("Perimeter =", Rectangle().perimeter(l, w))

            case 2:
                s = float(input("Side: "))
                print("Perimeter =", Square().perimeter(s))

            case 3:
                r = float(input("Radius: "))
                print("Perimeter =", Circle().perimeter(r))

            case 4:
                a = float(input("Side 1: "))
                b = float(input("Side 2: "))
                c = float(input("Side 3: "))
                print("Perimeter =", Triangle().perimeter(a, b, c))

            case _:
                print("Perimeter not applicable")

    case 3:
        match shape:
            case 5:
                a = float(input("Side: "))
                print("Volume =", Cube().volume(a))

            case 6:
                l = float(input("Length: "))
                w = float(input("Width: "))
                h = float(input("Height: "))
                print("Volume =", Cuboid().volume(l, w, h))

            case 7:
                r = float(input("Radius: "))
                print("Volume =", Sphere().volume(r))

            case 8:
                r = float(input("Radius: "))
                h = float(input("Height: "))
                print("Volume =", Cylinder().volume(r, h))

            case _:
                print("Volume not applicable")

    case _:
        print("Invalid operation")
