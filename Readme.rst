# Ade25 Asset Manager
====================

Introduction
---------------

This package provides an installable python package that can be used to setup
a general storage and management facility for static assets inside a
Plone project.

* `Source code @ GitHub <https://github.com/ade25/ade25.assetmanager>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ade25/ade25.assetmanager>`_


Installation
---------------

To install `ade25.assetmanager` you simply add ``ade25.assetmanager``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `ade25.assetmanager` using the Add-ons control panel.


Configuration
----------------

The configuration is done by the package generic setup profile. In order to use this package you must first add a `AssetRepository` folder inside an
existing Plone site.

The package does not asume any site specific usecase though it was originally concieved for a showreel and project listing usecase. Therefore the asset management is delegated to a Dexterity behavior that enables asset manager views.