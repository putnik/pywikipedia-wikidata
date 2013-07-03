# -*- coding: utf-8  -*-

import re
import pywikibot
from wikidata import Wikidata, GDN


Wikidata(
    template=u'Шаблон:Данные о субъекте Российской Федерации',
    #category=u'Категория:Фильмы без IMDb в Викиданных',
    #sleep=10,
    rules = {
        107: GDN.place,
        17: 'q159', # Country = Russia
        
        # From template:
        421: re.compile(ur'\|\s*MSKS\s*=\s*([\+\-]?\d+)\s*[\|\}]'), # MSK+N
    }
)

