from abc import ABC, abstractmethod

# Product: Пицца
class Pizza:
    def __init__(self):
        self.ingredients = []  # Ингредиенты пиццы
        self.sauce = None  # Соус для пиццы
        self.cheese = None  # Сыр для пиццы
        self.baking_time = 0  # Время выпекания

    def __str__(self):
        return f"Pizza with ingredients: {', '.join(self.ingredients)}, sauce: {self.sauce}, cheese: {self.cheese}, baked for {self.baking_time} minutes."

# Builder: Интерфейс для создания частей пиццы
class PizzaBuilder(ABC):
    @abstractmethod
    def add_ingredients(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass
    
    @abstractmethod
    def bake(self):
        pass
    
    @abstractmethod
    def get_pizza(self):
        pass

# Concrete Builder: Пицца Маргарита
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()  # Новый объект пиццы
    
    def add_ingredients(self):
        self.pizza.ingredients.append("tomato")  # Добавление помидоров
        self.pizza.ingredients.append("basil")  # Добавление базилика
    
    def add_sauce(self):
        self.pizza.sauce = "tomato"  # Добавление томатного соуса
    
    def add_cheese(self):
        self.pizza.cheese = "mozzarella"  # Добавление моцареллы
    
    def bake(self):
        self.pizza.baking_time = 10  # Время выпекания 10 минут
    
    def get_pizza(self):
        return self.pizza  # Возвращение объекта пиццы

# Concrete Builder: Гавайская пицца
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()  # Новый объект пиццы
    
    def add_ingredients(self):
        self.pizza.ingredients.append("ham")  # Добавление ветчины
        self.pizza.ingredients.append("pineapple")  # Добавление ананасов
    
    def add_sauce(self):
        self.pizza.sauce = "tomato"  # Добавление томатного соуса
    
    def add_cheese(self):
        self.pizza.cheese = "cheddar"  # Добавление сыра чеддер
    
    def bake(self):
        self.pizza.baking_time = 12  # Время выпекания 12 минут
    
    def get_pizza(self):
        return self.pizza  # Возвращение объекта пиццы

# Concrete Builder: Пицца Пепперони
class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()  # Новый объект пиццы
    
    def add_ingredients(self):
        self.pizza.ingredients.append("pepperoni")  # Добавление пепперони
        self.pizza.ingredients.append("peppers")  # Добавление перца
    
    def add_sauce(self):
        self.pizza.sauce = "tomato"  # Добавление томатного соуса
    
    def add_cheese(self):
        self.pizza.cheese = "provolone"  # Добавление проволоне
    
    def bake(self):
        self.pizza.baking_time = 15  # Время выпекания 15 минут
    
    def get_pizza(self):
        return self.pizza  # Возвращение объекта пиццы

# Director: Управляет процессом приготовления пиццы
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder  # Установка билдера

    def construct_pizza(self):
        self.builder.add_ingredients()  # Добавление ингредиентов
        self.builder.add_sauce()  # Добавление соуса
        self.builder.add_cheese()  # Добавление сыра
        self.builder.bake()  # Выпекание
        return self.builder.get_pizza()  # Возвращение готовой пиццы

# Использование классов
if __name__ == "__main__":
    # Приготовление пиццы Маргарита
    margherita_builder = MargheritaPizzaBuilder()
    director = PizzaDirector(margherita_builder)
    margherita_pizza = director.construct_pizza()
    print(margherita_pizza)

    # Приготовление Гавайской пиццы
    hawaiian_builder = HawaiianPizzaBuilder()
    director = PizzaDirector(hawaiian_builder)
    hawaiian_pizza = director.construct_pizza()
    print(hawaiian_pizza)

    # Приготовление пиццы Пепперони
    pepperoni_builder = PepperoniPizzaBuilder()
    director = PizzaDirector(pepperoni_builder)
    pepperoni_pizza = director.construct_pizza()
    print(pepperoni_pizza)
