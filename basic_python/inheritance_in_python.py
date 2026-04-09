class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        super().display()
        print("Breed:", self.breed)


d = Dog("Buddy", "Labrador")
d.display()