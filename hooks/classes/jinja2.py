#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# maintainer (@johnsondnz)
"""
class used by jinja2_lint module
"""
import os.path

from ansible_collections.ansible.utils.plugins.filter.ipaddr import ipaddr
from jinja2 import BaseLoader
from jinja2 import TemplateNotFound

# -- Section taken from https://github.com/drm/jinja2-lint/blob/master/j2lint.py --#


class AbsolutePathLoader(BaseLoader):
    """
    Loads Absolute Path
    """

    def get_source(self, environment, template):
        """
        Include some custom ansible filters
        Raise error if template is not found
        """

        # Include some custom ansible fitlers
        environment.filters["ipaddr"] = ipaddr
        environment.filters["type_debug"] = lambda o: o.__class__.__name__

        if not os.path.exists(template):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(template)
        with open(template) as file:
            source = file.read()
        return source, template, lambda: mtime == os.path.getmtime(template)


# -- end of borrowed code -- #
