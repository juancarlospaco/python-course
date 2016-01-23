#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from subprocess import getoutput


def walkdir_to_filelist(where, target, omit):
    """Perform full walk of where, gather full path of all files."""
    print("Scan {},searching {},ignoring {}".format(where, target, omit))
    return tuple([os.path.join(r, f)
                  for r, d, fs in os.walk(where, followlinks=True)
                  for f in fs if not f.startswith('.') and
                  not f.endswith(omit) and
                  f.endswith(target)])  # only target files,no hidden files


for exercise in walkdir_to_filelist(os.getcwd(), ".py", ".pyc"):
    print("\n" + "#" * 99)
    print(exercise)
    print(getoutput("python3 '{}'".format(exercise)))
