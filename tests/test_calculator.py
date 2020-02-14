import sys
sys.path.append("../calculator/")
import calculator

def test_add(*args):
    assert calculator.add(0,1) == 1
    assert calculator.add(-1,6) == 5
    assert calculator.add(6,8) == 14
    assert calculator.add(1,5,9,6) == 21
def test_multiply(*args):
    assert calculator.multiply (2,6) == 12
    assert calculator.multiply (3,10) == 30
    assert calculator.multiply (4,5) == 20
    assert calculator.multiply (2,1,3,5,10) == 300

if __name__ == "__main__":
    pass