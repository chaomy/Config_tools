#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chaomy
# @Date:   2017-08-16 20:14:53
# @Last Modified by:   chaomy
# @Last Modified time: 2017-08-16 20:26:00

import ase
import ase.io
from optparse import OptionParser


class transformat(object):

    def __init__(self):

        return

    def qe2vasp(self):
        atoms = ase.io.read('qe.out', 'espresso-out')
        ase.io.write(filename='poscar', images=atoms, format='vasp')
        return


if __name__ == '__main__':
    usage = "usage:%prog [options] arg1 [options] arg2"
    parser = OptionParser(usage=usage)

    parser.add_option('-t', '--mtype', action='store',
                      type='string', dest='mtype')

    parser.add_option('-p', "--params", action="store",
                      type='string', dest="fargs")

    (options, args) = parser.parse_args()
    drv = transformat()

    dispatcher = {'qe2vasp': drv.qe2vasp}

    if options.fargs is not None:
        dispatcher[options.mtype.lower()](options.fargs)
    else:
        dispatcher[options.mtype.lower()]()
