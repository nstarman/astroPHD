# -*- coding: utf-8 -*-
# see LICENSE.rst

"""utilipy."""

__author__ = "Nathaniel Starkman"

__all__ = [
    "LogFile",
    "ObjDict",
    "wraps",
    "config",
]


##############################################################################
# IMPORTS

# Packages may add whatever they like to this file, but
# should keep this content at the top.
from ._astropy_init import *  # noqa


# PROJECT-SPECIFIC

# import commonly used functions
from .utils.logging import LogFile
from .utils.collections import ObjDict
from .utils.functools import wraps

# configuration
from . import config

# import top level packages
from . import (  # noqa
    astro,
    constants,
    # data,
    data_utils,
    decorators,
    extern,
    fitting,
    imports,
    ipython,
    math,
    plot,
    scripts,
    units,
    utils,
)
from . import astro  # noqa, separated b/c alias


#############################################################################
# HELP FUNCTION


def help() -> None:
    """`utilipy` help function.

    This function is a work in progress

    """
    print("This function is a work in progress")

    print("".join(["-"] * 79))
    ipython.help()

    return None


# /def


#############################################################################
# __ALL__

__all_top_imports__ = (
    "astro",
    "astro",
    "constants",
    # "data",
    "data_utils",
    "decorators",
    "extern",
    "fitting",
    "imports",
    "ipython",
    "math",
    "plot",
    "scripts",
    "units",
    "utils",
)

__all__ += list(__all_top_imports__)


#############################################################################
# END