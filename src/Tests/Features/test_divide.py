import pytest
from functools import partial
from pytest_bdd import scenario, scenarios, parsers, given, when, then
from divide import divide_two


# @scenario('divide.feature', 'Divide Two positive numbers')
# def test_divide_positive():
#     pass

# @scenario('divide.feature', 'Divide Two negative numbers')
# def test_divide_negative():
#     pass

# @scenario('divide.feature', 'Divide positive by negative')
# def test_divide_pos_neg():
#     pass

# @scenario('divide.feature','Divide negative by positive')
# def test_divide_neg_pos():
#     pass

EXTRA_TYPES = {
    'Number' : int
}

CONVERTERS = {
    'dividend' : int,
    'divisor' : int,
    'result' : int
}

# scenarios('divide.feature')
scenarios('divide.feature', example_converters = CONVERTERS)
parse_num = partial(parsers.cfparse, extra_types = EXTRA_TYPES)

@given(parse_num('Dividend of "{dividend:Number}" and Divisor of "{divisor:Number}"'))
@given('Dividend of "<dividend>" and Divisor of "<divisor>"')
def div(dividend, divisor):
    return {
        'dividend' : dividend,
        'divisor' : divisor,
        'result' : 0
    }

@when("I divide them")
def divide(div):
    dt = divide_two.Solution()
    div['result'] = dt.divide(div['dividend'], div['divisor'])

@then(parse_num('Quotient should be accurate "{result:Number}"'))
@then('Quotient should be accurate "<result>"')
def dt(div, result):
    assert div['result'] == result