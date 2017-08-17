#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chaomy
# @Date:   2017-08-16 20:14:53
# @Last Modified by:   chaomy
# @Last Modified time: 2017-08-16 20:18:06

import ase
from optparse import OptionParser


class transformat(object):

    def __init__(self):

        return

    def qe2poscar(self):
        atoms = ase.io.read('qe.out', 'espresso-out')
        ase.io.write(filename='poscar', images=atoms, format='vasp')
        return


if __name__ == '__main__':
    usage = "usage:%prog [options] arg1 [options] arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--mtype",
                      action="store",
                      type="string",
                      dest="mtype", help="",
                      default="prp_r")
    (options, args) = parser.parse_args()
    drv = transformat()
    drv.qe2poscar()
