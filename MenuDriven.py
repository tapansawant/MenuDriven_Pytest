def Area_Rectangle(a, b):
    return a * b


def Perimeter_Rect(a, b):
    return 2 * (a + b)


def Area_Square(a):
    return a * a


if __name__ == "__main__":
    l = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    side = int(input("Enter side of square:"))

    while True:
        print("\nPress ")
        print("1 to find area of rectangle")
        print("2 to find perimeter of rectangle ")
        print("2 to find area of square ")
        print("4 to Exit")

        ch = int(input("Enter your Choice "))
        if ch == 1:
            print(Area_Rectangle(l, b))
        elif ch == 2:
            print(Perimeter_Rect(l, b))
        elif ch == 3:
            print(Area_Square(side))
        elif ch == 4:
            break
