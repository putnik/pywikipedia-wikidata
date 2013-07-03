# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata


Wikidata(pages=[
    { 'name': u'Алтайский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Камчатский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Хабаровский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Краснодарский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Красноярский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Пермский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Приморский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Ставропольский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
    { 'name': u'Забайкальский край', 'rules': { 242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]') } },
])

