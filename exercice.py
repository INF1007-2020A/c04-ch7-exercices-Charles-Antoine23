#!/usr/bin/env python
# -*- coding: utf-8 -*-




# TODO: Importez vos modules ici
from math import pi
import sys
sys.path.insert(1, "C:\Users\Charles-\Documents\Polytechnique\INF1007\c04-ch6-exercices-Charles-Antoine23")
from exercice2 import frequence

# TODO: Définissez vos fonction ici
def ellipsoide( x = 1, y = 1, z = 1, masse_volumique = 1):

    volume = 4 / 3 * pi * x * y * z
    masse = masse_volumique * volume

    return volume, masse


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(ellipsoide())
    print(lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[1])("Ceci est une phrase")

    pass
