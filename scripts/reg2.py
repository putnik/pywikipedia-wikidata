# -*- coding: utf-8  -*-

import re
from wikidata import Wikidata

Wikidata(template=u'Шаблон:Данные о субъекте Российской Федерации', rules = {
    48: re.compile(ur'\|\s*Аудио\s*=\s*([^\|]*)\s*[\|\]\}]'),
})

