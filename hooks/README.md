# Hooks

This directory contains Python scripts that run during the build process, in the order specified in [mkdocs.yml](../mkdocs.yml).

See the [Events](https://www.mkdocs.org/dev-guide/plugins/#events) section of the MkDocs Developer Guide for a diagram and details about the `on_` functions.

[bib2md.py](bib2md.py) and [people.py](people.py) are responsible for the auto-generated content on the site, including cross references.
