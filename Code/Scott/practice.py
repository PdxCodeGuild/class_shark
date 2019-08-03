class Dog:

    def __init__(self, name, breed, weight):
        self.name = name
        self.breed = breed
        self.weight = weight
    
    def bark(self):
        print(f"A {self.breed} dog named {self.name} just barked at me.")

d1 = Dog("Lassi", "Collie", 75 )
d2 = Dog("Spuds McKenzie", "Bull Terrier", 30) 
d3 = Dog("Brian", "lab", 50)

d1.bark()
d2.bark()
d3.bark()
