# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata, GDN

Wikidata(
    #template=u'Шаблон:Commonscat-inline',
    category=u'Категория:Википедия:Ссылка на Викисклад непосредственно в статье',
    #start=u'Гоцзыцзянь',
    #sleep=10,
    rules={
        # From template:
        373: re.compile(ur'\|\s*(?:[Cc]ommons|[Кк]атегория в [Cc]ommons|[Вв]икисклад|[Кк]атегория на [Вв]икискладе)\s*\=\s*(?:[Cc]ategory:\s*)?([^\|\}]+?)\s*[\|\}\<]'), # Commons
    }
)

