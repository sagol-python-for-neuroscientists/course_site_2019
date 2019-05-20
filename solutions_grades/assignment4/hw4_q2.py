import numpy as np
import pandas as pd


def largest_species(fname: str) -> pd.Series:
    """ Return largest column by year from the text file """

    data = pd.read_csv(fname, index_col=0, sep='\t', dtype=np.int64)
    return data.idxmax(axis=1)


def lynxes_when_hares(fname: str) -> pd.Series:
    """ Returns the number of lynxes when hares > fox """

    data = pd.read_csv(fname, index_col=0, sep='\t', dtype=np.int64)
    return data.loc[data['hare'] > data['fox'], 'lynx']


def mean_animals(fname: str) -> pd.DataFrame:
    """ Add a fourth column with the normalized mean number of animals in each year """
    data = pd.read_csv(fname, index_col=0, sep='\t', dtype=np.int64)
    # Could use the .assign() method as well
    data['mean_animals'] = data.sum(axis=1)
    data['mean_animals'] /= data['mean_animals'].max()
    return data


if __name__ == '__main__':
    fname = 'populations.txt'
    a = largest_species(fname)
    b = lynxes_when_hares(fname)
    d = mean_animals(fname)
