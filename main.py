class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.name, "видає звук", self.sound)
animal1 = Animal("Кіт", "Мяу")
animal1.make_sound()

animal2 = Animal("Собака", "Гав")
animal2.make_sound()
