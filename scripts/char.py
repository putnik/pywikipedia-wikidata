# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata, GDN

Wikidata(
    #template=u'Шаблон:Карточка персонажа',
    category=u'Категория:Персонажи без IMDb в Викиданных',
    #start=u'Андерс, Хельга',
    #sleep=10,
    rules={
        #107: GDN.person,
        
        # From template:
        345: re.compile(ur'\|\s*imdb\s*=\s*(?:ch|ID)?\s*(\d+)\s*[\|\}\/\<]'), # IMDb
    }
)

