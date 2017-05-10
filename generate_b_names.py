
from generatorkata import *

with open("phone_data_10000.txt") as f:
    cg = map(clean_phone_in_line, b_names_generator(f.readlines()))
    for bname, number in cg:
        print("{},{}".format(bname, number))

