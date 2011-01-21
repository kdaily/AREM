#!/usr/bin/env python
# Time-stamp: <2011-01-20 18:21:42 Jake Biesinger>

"""Description:

Copyright (c) 2008,2009,2010 Yong Zhang, Tao Liu <taoliu@jimmy.harvard.edu>

This code is free software; you can redistribute it and/or modify it
under the terms of the Artistic License (see the file COPYING included
with the distribution).

@status: beta
@version: $Revision$
@originalauthor:  Yong Zhang, Tao Liu
@originalcontact: taoliu@jimmy.harvard.edu

Modifications to probabilistically align reads to regions with highest
enrichment performed by Jacob Biesinger. Repackaged as "AREM" in accordance
with copyright restrictions.

@author: Biesinger, W Jacob B
@contact: jake.biesinger@gmail.com

Changes to this file since original release of MACS 1.4 (summer wishes):
  December/January 2011
    * Updated names (AREM, not MACS14)
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

    setup(name="AREM",
          version="AREM 1.0 Initial Release based on MACS 1.4 (summer wishes)",
          description="Aligning Reads by Expectation-Maximization.\nBased on MACS (Model Based Analysis for ChIP-Seq data)",
          author='Jake Biesinger; Yong Zhang; Tao (Foo) Liu',
          author_email='jake.biesinger@gmail.com; zy@jimmy.harvard.edu; taoliu@jimmy.harvard.edu',
          url='http://http://cbcl.ics.uci.edu/CompBioLab/index.php/AREM  http://liulab.dfci.harvard.edu/MACS/',
          package_dir={'AREM' : 'lib'},
          packages=['AREM', 'AREM.IO'],
          scripts=['bin/arem','bin/elandmulti2bed.py','bin/elandresult2bed.py','bin/elandexport2bed.py',
                   'bin/sam2bed.py'],
          console=['bin/arem'],
          app    =['bin/arem'],
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
