# ade25.assetmanager

## An asset manager for Plone projects

* `Source code @ GitHub <https://github.com/potzenheimer/ade25.assetmanager>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/ade25.assetmanager>`_
* `Documentation @ ReadTheDocs <http://ade25assetmanager.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/potzenheimer/ade25.assetmanager>`_

## How it works

This package provides a Plone addon as an installable Python egg package.

The generated Python package holds an example content type `ContentPage` which
provides a folderish version of the default **Page** document type.

The implementation is kept simple on purpose and asumes that the developer will
add further content manually.


## Installation

To install `ade25.assetmanager` you simply add ``ade25.assetmanager``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `ade25.assetmanager` using the Add-ons control panel.
