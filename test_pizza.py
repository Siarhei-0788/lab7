import pytest
from pizza_builder import PepperoniPizzaBuilder, PizzaDirector, PizzaBuilder, Pizza

# Тест для пиццы Пепперони
def test_pepperoni_pizza():
    builder = PepperoniPizzaBuilder()
    director = PizzaDirector(builder)
    pizza = director.construct_pizza()
    assert pizza.ingredients == ['pepperoni', 'peppers'], "Ingredients are not correct"
    assert pizza.sauce == 'tomato', "Sauce is not correct"
    assert pizza.cheese == 'provolone', "Cheese is not correct"
    assert pizza.baking_time == 15, "Baking time is not correct"
    assert str(pizza) == "Pizza with ingredients: pepperoni, peppers, sauce: tomato, cheese: provolone, baked for 15 minutes."

# Тест для проверки корректной работы конструктора пицц
def test_pizza_builder_constructs_correctly():
    class TestPizzaBuilder(PizzaBuilder):
        def __init__(self):
            self.pizza = Pizza()

        def add_ingredients(self):
            self.pizza.ingredients.append("test ingredient")

        def add_sauce(self):
            self.pizza.sauce = "test sauce"

        def add_cheese(self):
            self.pizza.cheese = "test cheese"

        def bake(self):
            self.pizza.baking_time = 20

        def get_pizza(self):
            return self.pizza

    builder = TestPizzaBuilder()
    director = PizzaDirector(builder)
    pizza = director.construct_pizza()
    assert pizza.ingredients == ['test ingredient'], "Ingredients are not correct"
    assert pizza.sauce == 'test sauce', "Sauce is not correct"
    assert pizza.cheese == 'test cheese', "Cheese is not correct"
    assert pizza.baking_time == 20, "Baking time is not correct"
    assert str(pizza) == "Pizza with ingredients: test ingredient, sauce: test sauce, cheese: test cheese, baked for 20 minutes."
