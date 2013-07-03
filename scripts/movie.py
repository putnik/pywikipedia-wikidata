# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata, GDN

Wikidata(
    #template=u'Шаблон:Фильм',
    category=u'Категория:Фильмы без IMDb в Викиданных',
    #sleep=10,
    rules = {
        107: GDN.work,
        
        # From template:
        345: re.compile(ur'\|\s*imdb_id\s*=\s*(?:tt?|ID)?\s*(\d+)\s*[\|\}]'), # IMDb
    }
)

