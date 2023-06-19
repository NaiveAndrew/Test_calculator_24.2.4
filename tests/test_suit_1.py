# импортируем класс Calculator из модуля app.calculator:
import pytest

# импортируем класс Calculator из модуля app.calculator
from app.calculator import Calculator

# создаем класс TestCalc для тестирования методов калькулятора:
class TestCalc:

    # определяем метод setup, который будет выполняться перед каждым тестом:
    def setup(self):
        self.calc = Calculator

    # определяем метод test_multiply_success, который будет проверять корректность умножения
    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 3) == 9

    # определяем метод test_division_success, который будет проверять корректность деления
    def test_division_success(self):
        assert self.calc.division(self, 12, 3) == 4

    # определяем метод test_subtraction_success, который будет проверять корректность вычитания
    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    # определяем метод test_adding_success, который будет проверять корректность сложения
    def test_adding_success(self):
        assert self.calc.adding(self, 6, 7) == 13

    # определяем метод teardown, который будет выполняться после каждого теста
    def teardown(self):
        print("Выполнение метода Teardown")
