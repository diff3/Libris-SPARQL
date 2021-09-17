#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
from SPARQLWrapper import SPARQLWrapper, JSON
import queries as q

"""
Example SPARQL from Libris with Python3
https://libris.kb.se/sparql

Written by Magnus Pettersson @2021
"""

sparql = SPARQLWrapper("https://libris.kb.se/sparql")
sparql.setReturnFormat(JSON)

# switch between 0-16 as in queries file.
sparql.setQuery(q.query[2])

result = sparql.query().convert()
pprint.pprint(result)
