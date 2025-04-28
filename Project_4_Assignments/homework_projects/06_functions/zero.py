def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
