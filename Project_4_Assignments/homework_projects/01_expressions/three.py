# Conversion factor for feet to inches
INCHES_IN_FOOT = 12  # There are 12 inches in 1 foot.

def main():
    # User se feet input lena
    feet = float(input("Enter number of feet: "))
    
    # Feet ko inches me convert karna
    inches = feet * INCHES_IN_FOOT
    
    # Output result print karna
    print("That is", inches, "inches!")

# Function ko call karna
if __name__ == '__main__':
    main()
