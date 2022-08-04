import pytest
@pytest.mark.parametrize("num,output",[(1,1),(2,4),(3,9)])
def test_cal_square1(num,output):
    assert num*num == output