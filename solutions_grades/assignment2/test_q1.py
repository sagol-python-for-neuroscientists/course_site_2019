from hw2_q1 import *


class TestBicycle:
    """
    Unit tests for the bicycle question. If no errors pop
    during the execution, and the summary printout doesn't
    contain any errors, your grade for the question will be perfect.
    """
    def test_existence(self):
        """ Asserts the class exists with the right name """
        assert Bicycle(gear=1, cadence=20)

    def test_change_speed_below_0(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(-1)
        assert bi.speed >= 0

    def test_change_speed_to_non_number(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to('a')
        assert (int(bi.speed) >= 0) and (int(bi.speed) <= 1000)

    def test_change_speed_to_higher_than_1000(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(1300)
        assert (bi.speed <= 1000)

    def test_cadence_remains_positive_zero(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(0)
        assert bi.cadence >=0

    def test_cadence_remains_positive_one(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(1)
        assert bi.cadence >= 0

    def test_gear_below_7(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(0)
        assert bi.gear >= 1
        bi.change_speed_to(1)
        assert bi.gear >= 1

    def test_gear_at_high_speeds(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(999)
        assert bi.gear <= 7

    def test_many_gear_changes(self):
        bi = Bicycle(gear=1, cadence=20)
        for speed in range(1000):
            bi.change_speed_to(speed)
        assert ((1 <= bi.gear <= 7) and (0 <= bi.speed <= 1000)), f"At a real speed of {speed},"\
                f"gear was {bi.gear} and bicycle speed was {bi.speed}."


if __name__ == '__main__':
    btests = TestBicycle()
    methods = ["existence", "change_speed_below_0", "change_speed_to_non_number",
               "change_speed_to_higher_than_1000", "cadence_remains_positive_zero",
               "cadence_remains_positive_one", "gear_below_7", "gear_at_high_speeds",
               "many_gear_changes"]

    errors = []

    for method in methods:
        try:
            getattr(btests, "test_" + method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")
    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")