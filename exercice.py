#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
def ellipsoide( x = 1, y = 1, z = 1, masse_volumique = 1):

    volume = 4/3 * x * y * z
    masse = masse_volumique * volume

    return (volume, masse)


# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(ellipsoide())

    pass
