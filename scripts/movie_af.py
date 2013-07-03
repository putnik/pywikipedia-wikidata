# -*- coding: utf-8  -*-

import re
import pywikibot
from wikidata import Wikidata, GDN


Wikidata(
    site=pywikibot.Site("af", "wikipedia"),
    refs={('p143', 'q766705'),}, # from Ukrain Wikipedia
    template=u'Sjabloon:Inligtingskas rolprent',
    #category=u'Категория:Фильмы без IMDb в Викиданных',
    #sleep=10,
    rules = {
        107: GDN.work,
        
        # From template:
        345: re.compile(ur'\|\s*imdb_id\s*=\s*(?:tt?|ID)?\s*(\d+)\s*[\|\}]'), # IMDb
    }
)

