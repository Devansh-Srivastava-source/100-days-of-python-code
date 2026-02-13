#Example of class inheritence in python
class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, Exhale")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self): # This method overrides on the parent class method, thus modify it.
        super().breathe()
        print("Doing this under water")
    
    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()