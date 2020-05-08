#
# Tests for external libraries
#

import math
import scipy.stats

#
# Create confiance interval for the proportion
#
z = abs(scipy.stats.norm(0, 1).ppf(0.05 / 2))
#
# conservator confiance interval
#
#n = 2398
#e = z / math.sqrt(4 * n)
#print(e)

def get_n(e):
    n = (z / e)**2 / 4
    return n

print(get_n(0.03))