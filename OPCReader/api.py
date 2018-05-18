import pandas as pd
import datetime
from os.path import exists


def parse(filename):
    """Parses the specified CSV file from the OPC, returns Pandas Dataframes containing system info, bin settings, and the data"""
    if exists(filename):
        return _read_meta(filename),_read_bin_settings(filename), _read_data(filename)
    else:
        raise IOError('File could not be found')


def _read_meta(filename):
    """Read the first 6 rows of the datafile, this contains the system information"""
    data = pd.read_csv(filename,header=None, nrows=6, sep=",|:", engine="python", index_col=0).T
    return data


def _read_bin_settings(filename):
    """Reads the system bin settings"""
    data = pd.read_csv(filename, header=7, nrows=9, index_col=0).T
    return data


def _read_data(filename):
    """Read the data contained in the CSV"""
    data = pd.read_csv(filename, header=18)
    data['OADateTime'] = data['OADateTime'].apply(_ole_to_epoch)
    return data


def _ole_to_epoch(x):
    """Convert OAtime to datetime"""
    OLE_TIME_ZERO = datetime.datetime(1899, 12, 30, 0, 0, 0)
    time = OLE_TIME_ZERO + datetime.timedelta(days=float(x))
    return time
