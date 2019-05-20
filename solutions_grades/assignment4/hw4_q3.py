import numpy as np
import pandas as pd


def common_complaint(fname: str):
    """
    Finds and returns the most common complaint as a tuple:
    (complaint_name, num)
    """
    data = pd.read_csv(fname, header=0, index_col=0)
    complaint_counts = data['Complaint Type'].value_counts()
    return complaint_counts.index[0], complaint_counts[0]


def parking_borough(fname: str) -> str:
    """
    Finds and returns the name of the NYC borough that has the
    most complaints of type 'Illegal Parking'.
    """
    data = pd.read_csv(fname, header=0, index_col=0)
    illegal_parks = data[data['Complaint Type'] == 'Illegal Parking']
    return illegal_parks.Borough.value_counts().index[0]

if __name__ == '__main__':
    fname = '311_service_requests.zip'
    d = common_complaint(fname)
    c = parking_borough(fname)