# -*- coding: utf-8 -*-

"""Docstring decorators."""

__author__ = "Nathaniel Starkman"


__all__ = [
    "format_doc",
    "set_docstring_for_import_func",
    "set_docstring_import_file_helper",
]


##############################################################################
# IMPORTS

# BUILT-IN

import ast
import typing as T


# PROJECT-SPECIFIC

from ..utils import functools
from ..data_utils import get_path_to_file


##############################################################################
# CODE
##############################################################################

##############################################################################
# Format Doc

# TODO figure out automodapi's :allowed-package-names: so don't
# need this jerry-rigged method

from astropy.utils.decorators import format_doc as _format_doc


def format_doc(
    docstring: T.Optional[str], *args: T.Any, **kwargs: T.Any
) -> T.Callable:
    """Astropy's Format Docstring Function.

    .. deprecated:: 1.0.0

    """
    return _format_doc(docstring, *args, **kwargs)


format_doc.__doc__ = _format_doc.__doc__
# /def

#####################################################################


def set_docstring_for_import_func(
    *path: str, package: T.Optional[str] = None, section: str = "Returns"
) -> str:
    """Set docstring for IPython import function, from import file's docstring.

    Takes a helper function for a module and adds the content of the modules'
    `section`. This currently only works on numpy-doc style docstrings.

    Parameters
    ----------
    *path: str
        path of import module
    package : str, optional, keyword only
        package for :func:`~utilipy.data_utils.get_path_to_file`
    section: str, optiona, keyword only
        numpy-doc style section name

    Notes
    -----
    This function might be moved

    """
    module = get_path_to_file(*path, package=package)

    # read docstring out of file
    with open(module, "r") as fd:
        module_doc = ast.get_docstring(ast.parse(fd.read()))

    # process docstring
    ind = module_doc.find(section)
    len_title = 2 * len(section)  # section & underline
    end_ind = ind + module_doc[ind + len_title :].find("---") + 2  # noqa

    doc = module_doc[ind:end_ind]  # get section (+ next header)

    # modify function with a basic decorator
    def decorator(func):
        @functools.wraps(func, docstring=func.__doc__ + "\n\n" + doc)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


# /def


##############################################################################
# END
