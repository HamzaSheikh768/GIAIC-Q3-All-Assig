# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class 
# during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, type):
        self.type = type
    
    def start(self):
        print(f"{self.type} engine started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    
    def start_engine(self):
        self.engine.start()

#____________________________ Example usage
engine = Engine("V6")
car = Car("Toyota", engine)
car.start_engine()