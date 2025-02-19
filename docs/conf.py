# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Kanka'
copyright = 'Owlchester SNC'
author = 'Owlchester SNC'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

source_suffix = [
    ".md",
]

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    'analytics_id': 'G-Q3YPF8N1J0',
    'analytics_anonymize_ip': True,
    'logo_only': True,
    'navigation_depth': 5,
}
html_logo = 'img/kanka-white.png'
html_favicon = "img/favicon.ico"

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
