import numpy as np


def average_conc(data, start=0, stop=None):
    """Returns average concentration of particles/mL over the data. Specify 'start' and 'stop' kwargs for a subset"""
    if stop is None:
        stop = len(data)

    counts_per_litre = {}
    for x in range(16):
        counts_per_litre[data.columns[1+x]] = np.sum(data[data.columns[1+x]][start:stop]/data['SFR(ml/s)'][start:stop])/len(data['Bin00'][start:stop])*1000
    return counts_per_litre

def mass_conc(bin_data, data):
    """Returns the mass concentration of particles in g/ml"""
    mass_per_litre = {}
    for item in bin_data.index.values:
        mass_per_litre[item] = round(average_conc(data)[item] * bin_data['Vol of a particle in bin (um3) (calculated by software)'].loc[
            item] * bin_data['Density of a particle in bin (g/ml)'].loc[item] * 10E-13, 12)
    return mass_per_litre
