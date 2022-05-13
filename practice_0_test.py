import practice_0


def test_answer():
    assert practice_0.func(3) == 4


def test_square_list():
    assert practice_0.square_list == [1,9,25,49,81]


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_sum(self):
        assert practice_0.sum_of_args(2,4,6) == 12
