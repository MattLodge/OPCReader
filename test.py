from OPCReader import parse
from OPCReader.statistics import average_conc, mass_conc

meta, bin_data, data = parse(r'./Doc/3 micron testing 30min.csv')


print(average_conc(data, 50, 100))

print(mass_conc(bin_data, data))

exit()

