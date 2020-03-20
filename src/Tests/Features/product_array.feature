Feature: Product_Array
    Return array with product of input array except self

Scenario: Create product array
    Given An input array ["1,3,7,4"]
    When I call "productExceptSelf"
    Then The class should return ["84,28,12,21"]

Scenario: Create product array faster
    Given An input array ["1,3,7,4"]
    When I call "productExceptSelf_constant_space"
    Then The class should return ["84,28,12,21"]