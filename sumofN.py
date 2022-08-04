import pytest
def SumofNnumbers(num):
    if num < 0:
        print("Enter a natural number")
    else:
        sum = 0
        while (num > 0):
            sum += num
            num -= 1
        return sum

@pytest.mark.parametrize("num,output",[(1,1),(2,3),(5,15)])
def test_cal_SumofNnumbers(num,output):
    assert SumofNnumbers(num) == output