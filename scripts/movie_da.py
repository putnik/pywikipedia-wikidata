# -*- coding: utf-8  -*-

import re
import pywikibot
from wikidata import Wikidata, GDN


Wikidata(
    site=pywikibot.Site("da", "wikipedia"),
    refs={('p143', 'q181163'),}, # from DA Wikipedia
    template=u'Skabelon:Infoboks film',
    #category=u'Категория:Фильмы без IMDb в Викиданных',
    #sleep=10,
    rules = {
        107: GDN.work,
        
        # From template:
        345: re.compile(ur'\|\s*imdb\s*=\s*(?:tt?|ID)?\s*(\d+)\s*[\|\}]'), # IMDb
    }
)

