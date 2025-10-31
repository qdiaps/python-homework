class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        print(f"Створено новий об'єкт Animal: {self.name} ({self.species})")

    def make_sound(self):
        print(f"{self.name} ({self.species}) каже: {self.sound}!")

dog = Animal("Рекс", "Собака", 5, "Гав-гав")
cat = Animal("Мурчик", "Кіт", 3, "Няв")

dog.make_sound()
cat.make_sound()
