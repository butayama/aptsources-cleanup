#!/usr/bin/python3 -OEs
# -*- coding: utf-8

import os
import sys
import runpy

sys_path = sys.path
if os.altsep:
    sys_path = (p.replace(os.altsep, os.sep) for p in sys_path)
sys.path[:] = [p for p in sys_path if 'site-packages' not in p.split(os.sep)]

runpy.run_module('aptsources_cleanup', run_name='__main__')
