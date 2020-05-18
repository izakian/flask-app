from random_number_generator import RandomNumber

def test_InRange():
    rand_val=RandomNumber(1, 10).generate()
    assert rand_val >= 1 and rand_val <= 10

