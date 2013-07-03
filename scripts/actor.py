# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata, GDN

Wikidata(
    #template=u'Шаблон:Кинематографист',
    category=u'Категория:Кинематографисты без IMDb в Викиданных',
    #start=u'Андерс, Хельга',
    #sleep=10,
    rules={
        107: GDN.person,
        
        # From template:
        345: re.compile(ur'\|\s*imdb_id\s*=\s*(?:nm|ID)?\s*(\d+)\s*[\|\}\/\<]'), # IMDb
    }
)

