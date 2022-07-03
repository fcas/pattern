#### PATTERN | VECTOR | WORDLIST ###################################################################
# Copyright (c) 2010 University of Antwerp, Belgium
# Author: Tom De Smedt <tom@organisms.be>
# License: BSD (see LICENSE.txt for details).
# http://www.clips.ua.ac.be/pages/pattern

####################################################################################################

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from builtins import str, bytes, dict, int
from builtins import map, zip, filter
from builtins import object, range

import os
from io import open

try:
    MODULE = os.path.dirname(os.path.realpath(__file__))
except:
    MODULE = ""


class Wordlist(object):

    def __init__(self, name, data=[]):
        """ Lazy read-only list of words.
        """
        self._name = name
        self._data = data

    def _load(self):
        if not self._data:
            with open(os.path.join(MODULE, self._name + ".txt")) as f:
                self._data = f.read().split("\n")

    def __repr__(self):
        self._load()
        return repr(self._data)

    def __iter__(self):
        self._load()
        return iter(self._data)

    def __len__(self):
        self._load()
        return len(self._data)

    def __contains__(self, w):
        self._load()
        return w in self._data

    def __add__(self, iterable):
        self._load()
        return Wordlist(None, data=sorted(self._data + list(iterable)))

    def __getitem__(self, i):
        self._load()
        return self._data[i]

    def __setitem__(self, i, v):
        self._load()
        self._data[i] = v

    def insert(self, i, v):
        self._load()
        self._data.insert(i, v)

    def append(self, v):
        self._load()
        self._data.append(v)

    def extend(self, v):
        self._load()
        self._data.extend(v)

STOPWORDS = Wordlist("stopwords") # Russian stop words
