
#import sys
#sys.path.append("../src")
# TODO make it with pip install -e
from math_demo import add, add_with_bug, calculate_tax_bagged, calculate_tax


def test_addition():
    assert add(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    # assert add_with_bug(7, 6) == 13
    print("Test ADDITION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print("Test BUGGED ADDITION PASSED")
    # finally we found data that make test reliable
    # assert add_with_bug(7, 6) == 13
    
def test_addition_dublicate():
    assert add(6, 7) == 6 + 7
    print("Test DUPLICATE ADDITION PASSED")

def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j # violation of dublicating
            assert add(i, j) == -i + j
            assert add(i, j) == -i - j
            assert add(i, j) == i - j
    print("Test OVERKILL ADDITION PASSED")

def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    print("Test CLUSTER PASSED")

def test_addition_commutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("Test COMMUTATIVITY PASSED")

def test_tax_calculator_pesticide_with_bug():
    assert calculate_tax_bagged(1000) == 150
    assert calculate_tax_bagged(100) == 15
    assert calculate_tax_bagged(10) == 1.5
    assert calculate_tax_bagged(1) == 0.15
    assert calculate_tax_bagged(234) == 35.1 
    print("Test TAX CALCULATOR PASSED")
    # assert calculate_tax_bagged(2.34) == 0.35 # 0.351

def test_tax_calculator_pesticide():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1 
    print("Test TAX CALCULATOR PASSED")
    # assert calculate_tax(2.34) == 0.35 # 0.351

def test_negative_income():
    try:
        calculate_tax(-100)
        print("Test NEGATIVE INCOME FAILED")
    except ValueError as e:
        print("Test NEGATIVE INCOME PASSED")


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_dublicate()
    test_addition_clusters()
    test_addition_commutative()
    test_tax_calculator_pesticide()
    test_tax_calculator_pesticide_with_bug()
    test_negative_income()
    # test_addition_overkill()