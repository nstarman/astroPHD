# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   : matplotlib_imports
# AUTHOR  : Nathaniel Starkman
# PROJECT : astroPHD
#
# ----------------------------------------------------------------------------

# Docstring and Metadata
r"""Base set of imports for matplotlib.

Routine Listings
----------------
Matplotlib: imports

    - pyplot->plt
    - matplotlib->mpl, .cm, .colors
    - mpl_toolkits.mplot3d.Axes3D

astroPHD: imports

    - ipython.plot.configure_matplotlib

References
----------
Matplotlib reference [1]_.

.. [1] John D. Hunter. Matplotlib: A 2D Graphics Environment, Computing in
    Science & Engineering, 9, 90-95 (2007), DOI:10.1109/MCSE.2007.55
    http://scitation.aip.org/content/aip/journal/cise/9/3/10.1109/MCSE.2007.55

"""

__author__ = "Nathaniel Starkman"


##############################################################################
# HELPER FUNCTIONS

from astroPHD.config import __config__
from astroPHD.decorators.docstring import (
    _set_docstring_import_file_helper,
    _import_file_docstring_helper,
)


##############################################################################
# IMPORTS

# +---------------------------------------------------------------------------+
# Plotting

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm, colors

from mpl_toolkits.mplot3d import Axes3D  # 3D plotting

# +--------------------------------------------------------------------------+
# IPython Magic

try:

    _HAS_IPYTHON = False

    get_ipython()

    if get_ipython() is None:  # double checking
        raise NameError

except NameError:

    pass

else:

    _HAS_IPYTHON = True

    from astroPHD.ipython.plot import configure_matplotlib


##############################################################################
# Running Imported Functions

if _HAS_IPYTHON:

    configure_matplotlib(backend="inline", figure_format="retina")


##############################################################################
# Printing Information


@_set_docstring_import_file_helper("Matplotlib", __doc__)  # doc from __doc__
def matplotlib_imports_help():
    """Help for Matplotlib base imports."""
    doc = _import_file_docstring_helper(matplotlib_imports_help.__doc__)
    print(doc)


# /def


if __config__.getboolean("verbosity", "verbose-imports"):
    matplotlib_imports_help()


##############################################################################
# END