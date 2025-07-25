# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime


project = 'Trivox Docs'
author = 'Santiago Rincon <rincorpes@gmail.com>'
copyright = f"{datetime.datetime.now().year} Santiago Rincón"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme = 'furo'

html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": "#00e0ff",                 # cyan from triangle
        "color-brand-content": "#a259ff",                 # purple from eye
        "color-background-primary": "#0f0f0f",            # dark black
        "color-background-hover": "#1a1a1a",
        "color-background-hover--transparent": "#1a1a1a",
        "color-highlight-on-target": "#332e66",           # accent for headings or links
        "color-foreground-primary": "#ffffff",            # base text
    },
    "light_css_variables": {
        "color-brand-primary": "#00bfe6",                 # muted cyan for light mode
        "color-brand-content": "#7c4dff",                 # keep slight purple tint
        "color-background-primary": "#ffffff",
        "color-background-hover": "#f2f2f2",
        "color-background-hover--transparent": "#f9f9f9",
        "color-highlight-on-target": "#d6c8ff",           # soft violet highlight
        "color-foreground-primary": "#0f0f0f",            # dark text
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/trivox-io/evolving-ideas",
            "html": "",
            "class": "fa-brands fa-github",
        },
        {
            "name": "Discord",
            "url": "https://discord.gg/ER9Sryjd",
            "html": "",
            "class": "fa-brands fa-discord",
        },
    ],
}

html_static_path = ['_static']
