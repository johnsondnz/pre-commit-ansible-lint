#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# maintainer (@johnsondnz)
"""
validation of jinja2 templates
"""
import argparse
import sys

from jinja2 import Environment
from jinja2 import exceptions
from jinja2 import TemplateNotFound

from hooks.classes.jinja2 import AbsolutePathLoader
from hooks.functions.common_functions import message_logging

DOCUMENTATION = """
pytest for validation of jinja2 templates.
"""

REQUIREMENTS = """
pip3 install jinja2 --user
"""


def _run_test(
    filename,
    env=Environment(
        loader=AbsolutePathLoader(),
        extensions=[
            "jinja2.ext.i18n",
            "jinja2.ext.do",
            "jinja2.ext.loopcontrols",
        ],
    ),
):
    """
    Inital entrypoint from __main__:
    params:
        filename: path to file that is checked
    Comments: Prints results to stdout as part of test run.
    """
    error = False
    try:
        env.get_template(filename)

    except TemplateNotFound:
        message_logging(
            filename=filename,
            message_title="File not found",
            message="Unable to open file",
        )
        error = True

    except exceptions.TemplateSyntaxError as ex:
        message_logging(
            filename=ex.filename,
            message_title="Syntax Fail",
            message=f"Syntax check failed: {ex.message} at line {ex.lineno}",
        )
        error = True

    except IndexError:
        message_logging(
            filename=filename,
            message_title="Usage",
            message="j2lint.py filename [filename ...]",
        )
        error = True

    except (IOError, Exception) as e:
        print(
            f"Something went wrong opening the file: {filename} - {e.__class__.__name__}, {e}",
        )
        error = True

    return error


def main(argv=None) -> bool:
    """
    Returns: bool as sys.exit code.  True = 1, False = 0.  Zero is good.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)
    error = False

    for filename in args.filenames:
        error = _run_test(filename) if error is not True else error

    try:
        return error

    except Exception:
        return True


if __name__ == "__main__":
    sys.exit(main())
