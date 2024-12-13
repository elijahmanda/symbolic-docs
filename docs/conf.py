# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

from pygments.lexers import get_lexer_by_name
from symbolic_lexer import SymbolicLexer


def setup(app):
    app.add_lexer('symbolic', SymbolicLexer)


project = 'Symbolic'
copyright = '2024, Elijah Manda'
author = 'Elijah Manda'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # For generating API docs from docstrings
    'sphinx.ext.napoleon',  # For NumPy/Google-style docstrings
    'recommonmark',         # For Markdown support
    'sphinx_rtd_theme',
    'symbolic_domain'
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
