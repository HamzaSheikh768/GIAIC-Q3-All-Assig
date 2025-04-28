def main():
    # Triangle ke 3 sides ka input lena (float taake decimal values bhi accept hoon)
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Perimeter calculate karna
    perimeter = side1 + side2 + side3

    # Output print karna
    print(f"The perimeter of the triangle is {perimeter}")


# Function ko execute karne ke liye ye line zaroori hai
if __name__ == '__main__':
    main()
