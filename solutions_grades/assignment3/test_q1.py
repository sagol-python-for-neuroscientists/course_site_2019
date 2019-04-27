from hw3_q1 import *


class TestQ1:
    """ A couple of tests for question 1 """

    def test_uniques(self):
        fi = FolderIterator()
        assert isinstance(fi.uniques, list)

    def test_duplicates(self):
        fi = FolderIterator()
        assert isinstance(fi.duplicates, dict)

    def test_find_unique_vals(self):
        fi = FolderIterator()
        fi.iter_folder()
        vals_to_find = ['d', 'j', 'q', 'o', 'b', 't', 'f', 'v', 'c', 'l', 'a', 'z', 'r', 'y', 'e', 'w', 'h', 'g']
        for item in fi.uniques:
            for val in vals_to_find:
                if val in item:
                    vals_to_find.remove(val)
                    break
        assert vals_to_find == []

    def test_unique_keys(self):
        fi = FolderIterator()
        fi.iter_folder()
        keys = ['S2.2lL',
             'AQ.n5x',
             'rH.rbh',
             'iz.9P3',
             'jG.Roh',
             'kZ.kJo',
             'RZ.9zx',
             'DC.bQx',
             'YO.doV',
             'GZ.pVN',
             '9f.zif',
             'mU.4yL',
             'pd.k0I',
             'Rx.Pe7',
             'rj.PRj',
             '8D.blN',
             'jG.d2t',
             'kI.wOE']
        for key in fi.duplicates:
            for key_to_find in keys:
                if key_to_find in key:
                    break
            else:
                assert False

        assert True

