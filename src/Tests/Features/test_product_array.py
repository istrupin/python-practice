import pytest
from functools import partial
from pytest_bdd import scenario, scenarios, parsers, given, when, then
from Arrays import product_except_self

scenarios('product_array.feature')

# @scenarios('product_array.feature', 'Create product array')
# def test_product_array():
#     pass

@given(parsers.cfparse('An input array ["{nums:Number+}"]', extra_types=dict(Number=int)))
def numDict(nums):
    return {
        'nums' : nums,
        'result' : []
    }

@when(parsers.parse('I call "{method}"'))
def divide(numDict, method):
    prod = product_except_self.Solution()
    product_method = getattr(prod, method)
    numDict['result'] = product_method(numDict['nums'])

@then(parsers.cfparse('The class should return ["{res:Number+}"]', extra_types=dict(Number=int)))
def dt(numDict, res):
    assert numDict['result'] == res