from fizzbuzz import fizzbuzz


def test_fizzbuzz_type():
    def check_type_and_possible_value(n, r):
        if type(r) is str:
            assert r in ["Fizz Buzz", "Fizz", "Buzz"]
        else:
            assert n == r

    for i in range(100):
        check_type_and_possible_value(i, fizzbuzz(i))


def test_fizzbuzz():
    assert fizzbuzz(0) == "Fizz Buzz"
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(11) == 11
    assert fizzbuzz(15) == "Fizz Buzz"
