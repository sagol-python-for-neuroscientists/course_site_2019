"""
__author__ = Hagai Har-Gil
HW2 Question 1 Solution
"""
class Bicycle:
    """ A basic implementation of a Bicycle """
    def __init__(self, gear=1, cadence=0):
        self.gear = gear  # can only be 1-7
        self.cadence = cadence
        self.speed = gear * cadence

    def __str__(self):
        return f"Current bicycle status:\nGear: {self.gear}\n"\
            f"Cadence: {self.cadence}\n"\
            f"Speed: {self.speed}"

    def change_gear(self, direction: str):
        """
        Change the bicycle's gear.
        direction: str - 'up' or 'down'
        """
        if direction is 'up':  # one way
            self.gear = min(self.gear + 1, 7)

        elif direction is 'down':  # another way
            if self.gear > 1:
                self.gear -= 1
            else:
                print('Already at minimal gear')

        else:
            print("Gear change can only be 'up' or 'down'.")

        self.speed = self.gear * self.cadence

    def change_cadence_by(self, num):
        """ Increase or decrease the pedals' cadence """

        if isinstance(num, (str, float)):
            self.cadence += num
        else:
            print('Cadence must change by an integer or floating point number.')

    def change_speed_to(self, num):
        """ Change the speed to num by changing gear and cadence """
        if isinstance(num, (int, float)):
            if not 0 <= num <= 1000:
                print("New speed must be between 0 and 1000 KPH.")
                return

            self.speed = num

        # Primitive logic to change cadence and gear follows
        if self.speed < 10:
            self.gear = 1
        elif self.speed > 800:
            self.gear = 7
        else:
            self.gear = 4

        self.change_cadence_by(self.speed / self.gear)

##################################
"---------------------------------"
##################################

# A more advanced implementation, perhaps making the advantages of OOP clearer
from enum import Enum

class GearChange(Enum):
    UP = 1
    DOWN = -1


class Bicycle_Advanced:
    """
    A more advanced implementation of bicycle, enforcing the parameters in a stricter manner
    speed must be positive, gear must in the range [1, 7] and cadence in the range [0, 200]
    Not all "tricks" here must be used together, but the idea is to show more advanced capabilities
    and modelling ideas. While it's about 10 lines of code (LOC) longer, it's certainly more robust.
    """

    def __init__(self, gear=1, cadence=0):

        # Initializations
        self._gear_table = [1, 2, 3, 4, 5, 6, 7]
        self._verify_inputs(gear, cadence)

        # Gear
        self.gear = gear  # can only be 1-7
        self._cur_gear_index = gear - 1

        self.cadence = cadence
        self.speed = self.gear * self.cadence

    def __str__(self):
        return f"Current bicycle status:\nGear: {self.gear}\n"\
            f"Cadence: {self.cadence}\n"\
            f"Speed: {self.speed}"

    def _verify_inputs(self, gear, cadence):
        """ Internal method """
        if gear not in self._gear_table:
            raise ValueError("Gear must be an integer between 1 and 7 inclusive.")

        if not 0 <= cadence <= 500:
            raise ValueError("Cadence must be between 0 and 500 rotations per minute.")

    def _change_gear_to(self, gear):
        """
        Internal method to change the gear.
        The assertion helps since this method should never fail,
        as it is a private method, but it's good to assert
        its success anyway.
        """
        assert gear  in self._gear_table
        self.gear = gear
        self._cur_gear_index = gear - 1

    def change_gear(self, direction):
        """
        Change the bicycle's gear.
        direction: Enumeration - UP (+1) or DOWN (-1)
        """
        try:
            next_gear = self._gear_table[self._cur_gear_index + direction.value]
        except IndexError:
            print("Edge of bicycle's gear reached.")
        else:
            self._change_gear_to(next_gear)

    def change_cadence_by(self, num):
        """ Increase or decrease the pedals' cadence """

        try:
            new_cadence = self.cadence + num
        except TypeError:
            print('Cadence must change by an integer or floating point number.')
            return

        if not ((0 <= new_cadence <= 500) and (new_cadence * self.gear <= 1000)):
            print(f'New cadence value too extreme. My current cadence is {self.cadence}.')
        else:
            self.cadence = new_cadence
            self.speed = self.gear * self.cadence

    def change_speed_to(self, num):
        """ Change the speed by changing pedal cadence and gear """

        if not 0 <= num <= 1000:
            print("New speed must be between 0 and 1000 KPH.")
            return

        # Change cadence incrementally until we find a suitable value
        step_size = 50
        max_allowed_cadence_change = int(500 + step_size - self.cadence)
        add_to_cadence = range(0, max_allowed_cadence_change, step_size)
        for value in add_to_cadence:
            self.change_cadence_by(value)
            if min(self._gear_table) <= num / self.cadence <= max(self._gear_table):
                self._change_gear_to(int(num / self.cadence))
                self.cadence = num / self.gear
                self.speed = self.gear * self.cadence
                break
        else:
            print(f"Problem in finding suitable parameters for speed {num}.")


if __name__ == '__main__':
    print("My old bikes:\n------------")
    bike = Bicycle(cadence=10)
    bike.change_cadence_by(10)
    bike.change_gear('down')
    bike.change_gear('up')
    print(bike.speed)

    bike.change_speed_to(874)
    print(f"Cadence: {bike.cadence}, gear: {bike.gear}")

    print("\nMy shiny new BMX:\n----------------")
    bmx = Bicycle_Advanced(gear=2, cadence=25)
    bmx.change_gear(GearChange.UP)
    bmx.change_cadence_by(100)
    bmx.change_speed_to(500)
    print(f"Cadence: {bmx.cadence}, gear: {bmx.gear}, speed: {bmx.speed}")
    bmx.change_cadence_by(-120)
    bmx.change_speed_to(500)
    print(f"Cadence: {bmx.cadence}, gear: {bmx.gear}, speed: {bmx.speed}")