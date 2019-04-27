from hw3_q2 import *


class TestQ2:
    """ Tests for Q2 """
    name = 'lorem_morse.txt'

    def test_file_exists(self):
        with open(self.name) as f:
            f.read()
        assert True

    def test_file_valid(self):
        with open(self.name) as f:
            data = f.read()
        assert data.count('-') == 2748
        assert data.count('.') == 4175
        assert data.count('\n') == 453

    def test_individual_lines(self):
        with open(self.name) as f:
            data = f.readlines()
        assert len(data) == 454
        assert data[-1] == '.-....--.-.-..-....-.-.-'
        assert data[3].startswith('.....-')

