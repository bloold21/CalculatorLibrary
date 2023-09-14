import calculator
import os


class TestCalCulator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(selfs):
        assert 100 == calculator.multiply(10, 10)

