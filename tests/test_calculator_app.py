from src.stamp_duty_calculator.calculator_app import calculator


def test_calculator_returns_0():
    assert calculator(100000) == 0
