# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a 
# class method with cls to manage and display the count.

class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

#____________________________ Example usage
c1 = Counter()
c2 = Counter()
print(f"Number of objects created: {Counter.get_count()}")