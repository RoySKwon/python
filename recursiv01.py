# recursiv01

import re


def recursiv_fuction(i):
    if i == 100:
        return;

    print("call Recursiv Fuction","count: ",i);
    recursiv_fuction(i+1);

recursiv_fuction(1);
