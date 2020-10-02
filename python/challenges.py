class Pet:
    type = 'Bondable'

    def __init__(self, name, age, says="I don't speak"):
        self.name = name
        self.age = age
        self.says = says

    def get_name(self):
        return f'The pets name is {self.name}'

    def speak(self):
        return f'{self.says}'


class Dog(Pet):
    type = 'Social'


class Cat(Pet):
    def __init__(self, name, age, says, color):
        super().__init__(name, age, says)
        self.color = color
    type = 'Anti-social'


class Fish(Pet):
    type = 'Social'


odie = Dog('Odie', 5, 'Woof')
print(odie.__dict__)
print(odie.type)
print(odie.speak())

garfield = Cat('Garfield', 6, 'Meow', 'White')
print(garfield.__dict__)
print(garfield.type)
print(garfield.speak())

nemo = Fish('Nemo', 2)

print(nemo.__dict__)
print(nemo.type)
print(nemo.speak())
