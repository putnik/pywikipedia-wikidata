# -*- coding: utf-8  -*-

import re
import pywikibot
from wikidata import Wikidata, GDN


Wikidata(
    site=pywikibot.Site("el", "wikipedia"),
    refs={('p143', 'q11918'),}, # from Greek Wikipedia
    template=u'Πρότυπο:Πληροφορίες ταινίας',
    #category=u'Категория:Фильмы без IMDb в Викиданных',
    #sleep=10,
    rules = {
        107: GDN.work,
        
        # From template:
        345: re.compile(ur'\|\s*imdb_id(?:_2)?\s*=\s*(?:tt?|ID)?\s*(\d+)\s*[\|\}]'), # IMDb
    }
)

