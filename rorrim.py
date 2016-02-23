# -*- coding: utf-8 -*-
import os
import readline
from colors import *

c = raw_input("chinese: ")

with open("phone.cin", "r") as ins:
    for line in ins:
        if c == line[-4:].strip():
            print line.strip()



