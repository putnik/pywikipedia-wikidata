# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata

Wikidata(template=u'Шаблон:НП-США', rules = {
    107: 'q618123', # GDN = geo
    17: 'q30', # Country = USA
    
    # From template:
    #36: re.compile(ur'\|\s*FSCtrNm\s*=\s*(?:\[\[)?(.*?)\s*[\|\}\]]'), # столица
    373: re.compile(ur'\|\s*категория в Commons\s*=\s*([^\|\[\]]*?)\s*[\|\}]'), # Commons
    #281: re.compile(ur'\|\s*почтовый индекс\s*=\s*(\d+)\s*(?:[\|\}]|<ref)'), # Post index
    #281: re.compile(ur'\|\s*почтовые индексы\s*=\s*(\d+)(?:\s*[^\d](?:<br\s?\/?>)?\s*(\d+))*\s*(?:[\|\}]|<ref)'), # Post index

    #163: re.compile(ur'\|\s*FlagLnk\s*=\s*(.*?)\s*[\|\}]'),
    #237: re.compile(ur'\|\s*CoALnk\s*=\s*(.*?)\s*[\|\}]'),
    #48: re.compile(ur'\|\s*Аудио\s*=\s*(.+?)\s*[\|\]\}]'),
    #41: re.compile(ur'\|\s*флаг\s*=\s*([^\|\[\]]*?)\s*[\|\]]'),
    #94: re.compile(ur'\|\s*герб\s*=\s*(.*)\s*[\|\]]'),

    #85: re.compile(ur'\|\s*Название гимна\s*=\s*(?:\{\{s\|)?«?(?:\'\')?(?:\[\[)?(.*?)\s*[\|\}\]]'), # гимн
})

