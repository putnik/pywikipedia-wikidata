# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata

Wikidata(template=u'Шаблон:Достопримечательность', rules = {
    107: 'q618123', # GDN = geo
    373: re.compile(ur'\|\s*Commons\s*=\s*([^\|\[\]]*?)\s*[\|\}<]'), # Commons
})

