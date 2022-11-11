"""
read_ensdf
Fox 11/2022
"""

import pyne
from pyne import ensdf
from icecream import ic

ic(pyne)

##################################

filename = '20F.ensdf'
x = ensdf.decays(filename)
print(x)

print('Done.')
