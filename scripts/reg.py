# -*- coding: utf-8  -*-

import time, re

import pywikibot
import pagegenerators


site = pywikibot.Site("ru", "wikipedia")
tpl = pywikibot.Page(site, u'Шаблон:Данные о субъекте Российской Федерации')

gen = pagegenerators.ReferringPageGenerator(tpl,
                            followRedirects=False,
                            withTemplateInclusion=True,
                            onlyTemplateInclusion=True)
generator = pagegenerators.PreloadingGenerator(gen, pageNumber=10)


claims_rules = {
    107: 'q618123', # GDN = geo
    17: 'q159', # Country = Russia
    
    # From template:
    36: re.compile(ur'\|\s*FSCtrNm\s*=\s*(?:\[\[)?(.*?)\s*[\|\}\]]'), # столица
    373: re.compile(ur'\|\s*Викисклад\s*=\s*Category:(.*?)\s*[\|\}]'), # Commons

    163: re.compile(ur'\|\s*FlagLnk\s*=\s*(.*?)\s*[\|\}]'),
    237: re.compile(ur'\|\s*CoALnk\s*=\s*(.*?)\s*[\|\}]'),
    41: re.compile(ur'\|\s*FSFlag\s*=\s*\[\[(?:[Фф]айл|[Ff]ile|[Ии]зображение|[Ii]mage):(.+?)\s*[\|\]]'),
    94: re.compile(ur'\|\s*FSCoA\s*=\s*\[\[(?:[Фф]айл|[Ff]ile|[Ии]зображение|[Ii]mage):(.+?)\s*[\|\]]'),

    85: re.compile(ur'\|\s*FSAnthem\s*=\s*(?:\{\{s\|)?«?(?:\'\')?(?:\[\[)?(.*?)\s*[\|\}\]]'), # столица

#    242: re.compile(ur'\|\s*FSMapName\s*=\s*(.*?)\s*[\|\}]'), # Map image
}


def editclaim(pid, value):
    print 'p%s = %s' % (pid, value)
    data.editclaim('p' + str(pid), value,
        raw_value=False,
        refs={('p143', 'q206855'),}, # from Russian Wikipedia
        #comment='Bot: Transfer data from Russian Wikipedia, [[Property:P%s|p%s]]=[[%s]]' % (pid, pid, claims_rules[pid]),
        )
    time.sleep(15)


for page in generator:
    print page
    if page.namespace():
        print 'ERROR: NOT AN ARTICLE'
        continue
    data = pywikibot.DataPage(page)
    if data.exists():
        item = data.get()
        
        claims = {}
        if 'claims' in item:
            for claim in item['claims']:
                if claim['m'][1] not in claims:
                    claims[claim['m'][1]] = []
                claims[claim['m'][1]].append(claim)
        
        for pid in claims_rules:
            if pid not in claims:
                rules = claims_rules[pid]
                if not issubclass(type(rules), list):
                    rules = [rules,]
                for rule in rules:
                    if issubclass(type(rule), str):
                        editclaim(pid, rule)
                    else:
                        m = rule.search(page.get())
                        if m:
                            values = m.groups()
                            for v in values:
                                if v:
                                    if pid == 242:
                                        v = 'Map of Russia - %s Krai (2008-03).svg' % v
                                    v = v.replace('_', ' ')
                                    if pid == 36 or pid == 163 or pid == 237 or pid == 85:
                                        vpage = pywikibot.Page(site, v)
                                        while vpage.isRedirectPage():
                                            vpage = vpage.getRedirectTarget()
                                        vdata = pywikibot.DataPage(vpage)
                                        if vdata.exists():
                                            print v
                                            editclaim(pid, str(vdata.get()['entity']))
                                        else:
                                            print 'ERROR: NO DATA PAGE FOR VALUE (%s)' % v
                                    else:
                                        editclaim(pid, v)
    else:
        print 'ERROR: NO DATA PAGE'

