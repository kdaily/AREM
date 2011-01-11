#!/usr/bin/env python
# Time-stamp: <2010-09-01 17:03:47 Tao Liu>

"""Description

Setup script for MACS -- Model Based Analysis for ChIP-Seq data

Copyright (c) 2008,2009,2010 Tao Liu <taoliu@jimmy.harvard.edu>

This code is free software; you can redistribute it and/or modify it
under the terms of the Artistic License (see the file COPYING included
with the distribution).

@status:  beta
@version: $Revision$
@author:  Tao Liu
@contact: taoliu@jimmy.harvard.edu
"""

import os
import sys
from distutils.core import setup, Extension
try:
    import py2exe
except ImportError:
    pass
try:
    import py2app
except ImportError:
    pass

def main():
    if float(sys.version[:3])<2.6 or float(sys.version[:3])>=2.8:
        sys.stderr.write("CRITICAL: Python version must be 2.6 or 2.7!\n")
        sys.exit(1)

    setup(name="MACS",
          version="1.4.0beta",
          description="Model Based Analysis for ChIP-Seq data",
          author='Yong Zhang; Tao (Foo) Liu',
          author_email='zy@jimmy.harvard.edu; taoliu@jimmy.harvard.edu',
          url='http://liulab.dfci.harvard.edu/MACS/',
          package_dir={'MACS14' : 'lib'},
          packages=['MACS14', 'MACS14.IO'],
          scripts=['bin/macs14','bin/elandmulti2bed.py','bin/elandresult2bed.py','bin/elandexport2bed.py',
                   'bin/sam2bed.py'],
          console=['bin/macs14'],
          app    =['bin/macs14'],
          classifiers=[
              'Development Status :: 4 - experimental',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: Artistic License',
              'Operating System :: MacOS :: MacOS X',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Programming Language :: Python',
              ],
          )

if __name__ == '__main__':
    main()
