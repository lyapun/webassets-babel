# -*- coding: utf-8 -*-

__author__ = 'Taras Lyapun'
__email__ = 'taraslyapun@gmail.com'
__version__ = '0.1.3'

import os
import subprocess
import tempfile
from io import open

from webassets.filter import Filter
from webassets.exceptions import FilterError


class BabelFilter(Filter):
    """Turn ES6+ code into ES5 friendly code usign `Babel <https://babeljs.io/>`_.

    Babel is an external tool written for NodeJS.
    You can install it:
    ```
    npm install --global babel
    ```
    This filter assumes that the ``babel`` executable is in the path. Otherwise, you
    may define the ``BABEL_BIN`` setting.
    """
    name = 'babel'
    
    max_debug_level = None

    options = {
        'binary': 'BABEL_BIN',
    }

    def input(self, _in, out, **kwargs):
        input_filename = tempfile.mktemp() + "-babel.js"
        output_filename = tempfile.mktemp() + ".js"

        with open(input_filename, 'w') as f:
            f.write(_in.getvalue())

        proc = subprocess.Popen(
            self.get_executable_list(input_filename, output_filename),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            raise FilterError(
                'babel: subprocess had error: stderr=%s,'
                'stdout=%s, returncode=%s' .format(
                    stderr, stdout, proc.returncode))

        with open(output_filename, 'r') as f:
            out.write(f.read())

        os.unlink(input_filename)
        os.unlink(output_filename)

    def get_executable_list(self, input_filename, output_filename):
        return [self.binary or 'babel', input_filename, '-o', output_filename]
