# -*- coding: utf-8  -*-

import re
import pywikibot
from wikidata import Wikidata, GDN


Wikidata(
    site=pywikibot.Site("ca", "wikipedia"),
    refs={('p143', 'q199693'),}, # from CA Wikipedia
    template=u'Plantilla:Infotaula pel·lícula',
    #category=u'Категория:Фильмы без IMDb в Викиданных',
    #sleep=10,
    rules = {
        107: GDN.work,
        
        # From template:
        345: re.compile(ur'\|\s*imdb\s*=\s*(?:tt?|ID)?\s*(\d+)\s*[\|\}]'), # IMDb
    }
)

