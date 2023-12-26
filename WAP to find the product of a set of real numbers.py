#5.WAP to find the product of a set of real numbers.

import random

rans_dict = {k: None for k in list(set([random.randint(1, 100000) for i in range(100000)]))}

for key, value in rans_dict.items():
    for i in range(2, int(key ** 0.5) + 2):
        if key % i == 0 and key // i in rans_dict:
            rans_dict[key] = (i, key // i)

print(rans_dict[232])
