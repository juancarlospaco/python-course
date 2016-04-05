#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from subprocess import call


def walkdir_to_filelist(where, target, omit):
    """Perform full walk of where, gather full path of all files."""
    print("Scan {},searching {},ignoring {}".format(where, target, omit))
    return tuple([os.path.join(r, f)
                  for r, d, fs in os.walk(where, followlinks=True)
                  for f in fs if not f.startswith(('.', 'pyqt_')) and
                  not f.endswith(omit) and
                  f.endswith(target)])  # only target files,no hidden files


for exercise in walkdir_to_filelist(os.getcwd(), ".py", ".pyc"):
    print("\n" + "#" * 99)
    print(exercise)
    return_code = call("python3 '{}'".format(exercise), shell=True)
    print(exercise, "FAIL" if return_code else "PASS")


exit(return_code)
