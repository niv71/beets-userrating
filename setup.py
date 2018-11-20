from setuptools import setup

setup (
    name                 = 'beets-userrating',
    author               = 'Michael Wawrzyniak',
    author_email         = 'mwawrzyniak@cmstactical.net',
    description          = "A plugin for managing user's per-track ratings in the music geek's media organizer",
    install_requires     = ['beets >= 1.4.3'],
    license              = 'GPLv3',
    namespace_packages   = ['beetsplug'],
    packages             = ['beetsplug'],
    platforms            = 'ALL',
    url                  = 'https://github.com/niv71/beets-userrating',
    version              = '0.0.2',
)
