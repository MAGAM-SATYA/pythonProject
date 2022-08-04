import PYTEST1

def test_calSquare1():
    result= PYTEST1.cal_square(6)
    assert result== 36

@pytest.mark.satya
def test_calSquare2():
    result= PYTEST1.cal_square(7)
    assert result== 49