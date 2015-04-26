#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_webassets_babel
----------------------------------

Tests for `webassets_babel` module.
"""
from __future__ import unicode_literals
from io import StringIO
from mock import patch
import unittest

from webassets_babel import BabelFilter


class BabelFilterTestCase(unittest.TestCase):

    @patch.object(BabelFilter, 'get_executable_list',
                  lambda self, input, output: ['cp', input, output])
    def test_should_process_input(self):
        _input = StringIO()
        _input.write('Test.')
        _output = StringIO()
        babel = BabelFilter()
        babel.input(_input, _output)
        self.assertEqual(_output.getvalue(), 'Test.')

    def test_get_executable_list(self):
        babel = BabelFilter()
        self.assertEqual(babel.get_executable_list('input', 'output'),
                         ['babel', 'input', '-o', 'output'])

if __name__ == '__main__':
    unittest.main()
