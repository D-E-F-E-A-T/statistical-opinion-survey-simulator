# import used modules
from soss.confianceinterval import ProportionConservator

# get sample size for proportion with 0.95 
# of confiability and an max error of 0.02
size = ProportionConservator.get_sample_size(0.95, 0.02)
# show information
print(size)