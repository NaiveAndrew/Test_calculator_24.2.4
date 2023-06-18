import pytest

from app.calculator import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_success(self):
        assert self.calc.division(self, 12, 3) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_success(self):
        assert self.calc.adding(self, 6, 7) == 13

    def teardown(self):
        print("Выполнение метода Teardown")