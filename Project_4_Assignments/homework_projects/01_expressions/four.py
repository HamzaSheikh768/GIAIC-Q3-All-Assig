import math  # math module ko import kar rahe hain, jisme sqrt function hai

def main():
    # User se AB aur AC ka length lena
    ab = float(input("Enter the length of AB: "))  # AB side
    ac = float(input("Enter the length of AC: "))  # AC side

    # Pythagorean theorem ke according BC ka length calculate karna
    bc = math.sqrt(ab**2 + ac**2)
    
    # Hypotenuse ka result print karna
    print("The length of BC (the hypotenuse) is: " + str(bc))

# Function ko call karna
if __name__ == '__main__':
    main()
