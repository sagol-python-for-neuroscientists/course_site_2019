from hw3_q3 import *
import numpy as np
import pathlib


class TestBasicNumpy:
    fname = 'data.npy'
    data = np.load(fname)

    def test_load_data(self):
        assert np.all(self.data == load_data(self.fname))

    def test_find_in_range(self):
        cur_data = np.load(pathlib.Path('tests_data/find_in_range.npy'))
        assert np.all(cur_data == find_in_range(self.data))

    def test_first_after_val(self):
        cur_data = np.load(pathlib.Path('tests_data/first_after_val.npy'))
        assert np.all(cur_data == first_after_val(self.data))
