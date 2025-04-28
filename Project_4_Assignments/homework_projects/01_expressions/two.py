# Speed of light in meters per second
C = 299792458  

def main():
    # User se mass input lena (kg)
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Energy calculate karna using Einstein's formula
    energy_in_joules = mass_in_kg * (C ** 2)

    # Output dikhana
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")

# Required to call the main function
if __name__ == '__main__':
    main()
