# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# If your extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'Activate Your UHC Card'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare'

# Full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------
# Title shown in the browser tab and top of HTML pages
html_title = "Activate Your UHC Card at activate.uhc.com – Step-by-Step Guide"

# Optional shorter title used in the navigation bar or elsewhere
html_short_title = "UHC Card Activation"

# Favicon (put favicon.ico in the root directory or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment to enable)
# html_theme = 'sphinx_rtd_theme'

# Hide the "View page source" link on pages
html_show_sourcelink = False

# Allow raw HTML blocks within .rst files for enhanced customization
html_allow_unsafe = True

# Theme-specific customization options
html_theme_options = {
    'show_powered_by': False,  # Remove "Powered by Sphinx" footer
}

# Paths to custom templates and static files
templates_path = ['_templates']
# Uncomment below if you have custom static assets like CSS or images
# html_static_path = ['_static']

# Files and folders to ignore when building documentation
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
