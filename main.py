class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self):
        print(f"{self.name} ест.")


class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color="Brown"):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def __init__(self, name, age, is_venomous=False):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        print(f"{self.name} шипит.")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

    # Создаем объекты разных типов животных


sparrow = Bird("Воробей", 2)
tiger = Mammal("Тигр", 5)
snake = Reptile("Змея", 3, is_venomous=True)

# Список животных
animals = [sparrow, tiger, snake]

# Вызываем функцию для демонстрации полиморфизма
animal_sound(animals)

import pickle

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []  # Список для хранения животных
        self.employees = []  # Список для хранения сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк {self.name}.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} добавлен в сотрудники зоопарка {self.name}.")

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f"- {animal.name}, возраст: {animal.age}")

    def show_employees(self):
        print(f"Сотрудники зоопарка {self.name}:")
        for employee in self.employees:
            print(f"- {employee.name}, должность: {employee.__class__.__name__}")

 # Метод для сохранения данных в файл
    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Данные зоопарка {self.name} сохранены в файл {filename}.")

# Метод для загрузки данных из файла
    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'rb') as f:
                zoo = pickle.load(f)
            print(f"Данные зоопарка {zoo.name} загружены из файла {filename}.")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return None

# Создаем зоопарк
zoo = Zoo("Городской зоопарк")

# Добавляем животных
zoo.add_animal(sparrow)
zoo.add_animal(tiger)
zoo.add_animal(snake)

# Выводим список животных
zoo.show_animals()

class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# Создаем зоопарк
zoo = Zoo("Городской зоопарк")

# Создаем сотрудников
keeper = ZooKeeper("Василий")
vet = Veterinarian("Екатерина")

# Добавляем сотрудников в зоопарк
zoo.add_employee(keeper)
zoo.add_employee(vet)

# Выводим список сотрудников
zoo.show_employees()

# Сохраняем данные зоопарка в файл
zoo.save_data("zoo_data.pkl")

# Загрузка данных из файла
loaded_zoo = Zoo.load_data("zoo_data.pkl")
if loaded_zoo:
    loaded_zoo.show_animals()
    loaded_zoo.show_employees()








