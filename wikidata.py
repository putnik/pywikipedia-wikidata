# -*- coding: utf-8  -*-

import time, re

import pywikibot, catlib
import pagegenerators


class GDN(object):
    person = 'q215627'
    organization = 'q43229'
    event = 'q1656682'
    work = 'q386724'
    term = 'q1969448'
    place = 'q618123'
    disambig = 'q11651459'


class Wikidata(object):
    def __init__(self, site=None, template=None, category=None, start=None, pages=None,
                refs=None, rules={}, sleep=0, preload=60):
        if site:
            self._site = site
        else:
            self._site = pywikibot.Site("ru", "wikipedia")

        if refs:
            self._refs = refs
        else:
            self._refs = {('p143', 'q206855'),} # from Russian Wikipedia

        self._pagecount = 0
        self._editcount = 0
        self._rules = rules
        self._sleep = sleep

        if template:
            self._tpl = pywikibot.Page(self._site, template)
            gen = pagegenerators.ReferringPageGenerator(self._tpl,
                followRedirects=False,
                withTemplateInclusion=True,
                onlyTemplateInclusion=True)
            self._generator = pagegenerators.PreloadingGenerator(gen,
                pageNumber=preload)
            self._run_generator()
        elif category:
            self._cat = catlib.Category(self._site, category)
            gen = pagegenerators.CategorizedPageGenerator(self._cat,
                recurse=False,
                start=start)
            self._generator = pagegenerators.PreloadingGenerator(gen,
                pageNumber=preload)
            self._run_generator()
        elif pages:
            self._pages = pages
            self._run_pages()
        self._log('Done. Pages: %s, edits: %s.' % (self._pagecount, self._editcount), 1)

    def _edit_claim(self, data, pid, value, raw_value=False):
        if pid == 242:
            value = value.replace('_', ' ')
        self._editcount += 1
        self._log('%s. p%s = %s' % (self._editcount, pid, value), 92)
        time.sleep(self._sleep)
        data.editclaim('p' + str(pid), value,
            raw_value=raw_value,
            refs=self._refs,
            #comment='Bot: Transfer data from Russian Wikipedia, [[Property:P%s|p%s]]=[[%s]]' % (pid, pid, claims_rules[pid]),
            )

    def _run_generator(self):
        for page in self._generator:
            self._title(page.title())
            if page.namespace():
                self._error('Not an article')
                continue
            data = pywikibot.DataPage(page)
            if data.exists():
                claims = self._get_claims(data)
                for pid in self._rules:
                    self._check_claim(page, data, claims, pid, self._rules[pid])
            else:
                self._error('No data page')

    def _run_pages(self):
        for row in self._pages:
            self._title(row['name'])
            page = self._get_page_by_name(row['name'])
            data = pywikibot.DataPage(page)
            if data.exists():
                claims = self._get_claims(data)
                for pid in row['rules']:
                    self._check_claim(page, data, claims, pid, row['rules'][pid])
            else:
                self._error('No data page (%s)' % row['name'])

    def _get_page_by_name(self, pagename):
        page = pywikibot.Page(self._site, pagename)
        while page.isRedirectPage():
            page = page.getRedirectTarget()
        return page

    def _get_claims(self, data):
        item = data.get()
        claims = {}
        if 'claims' in item:
            for claim in item['claims']:
                if claim['m'][1] not in claims:
                    claims[claim['m'][1]] = []
                claims[claim['m'][1]].append(claim)
        return claims

    def _check_claim(self, page, data, claims, pid, rules):
        if pid not in claims:
            self._log('NO: %s' % pid)
            if not issubclass(type(rules), list):
                rules = [rules,]
            for rule in rules:
                if issubclass(type(rule), str):
                    self._edit_claim(data, pid, rule)
                else:
                    m = rule.search(page.get())
                    if m:
                        values = m.groups()
                        for v in values:
                            if v:
                                # TODO: Получение типа записи из Викиданных
                                # Media or Commons
                                if pid == 48 or pid == 373:
                                    # TODO: Проверка на сущестование файла/категории
                                    v = v.replace('_', ' ').strip()
                                    if not v:
                                        continue
                                    v = v[0].upper() + v[1:]
                                # IMDb
                                if pid == 345:
                                    v = u'{:0>7}'.format(int(v))
                                    if v == u'0000000':
                                        continue
                                    # Choose IMDb prefix using GND type
                                    if self._rules and 107 in self._rules:
                                        if self._rules[107] == GDN.person:
                                            v = u'nm' + v
                                        elif self._rules[107] == GDN.work:
                                            v = u'tt' + v
                                        else:
                                            self._error('Undefined IMDb type')
                                            continue
                                    else:
                                        #v = u'ch' + v
                                        self._error('Undefined IMDb type')
                                        continue
                                # TZ
                                if pid == 421:
                                    v = u'MSK' + v
                                # Link to page
                                if pid == 85 or pid == 132 or pid == 237 or  pid == 421:
                                    vpage = self._get_page_by_name(v)
                                    vdata = pywikibot.DataPage(vpage)
                                    if vdata.exists():
                                        self._log(v)
                                        v = str(vdata.get()['entity'])
                                    else:
                                        self._error('No data page for value (%s)' % v)
                                        continue
                                self._edit_claim(data, pid, v)

    def _log(self, msg, color=None):
        if color:
            print '\033[%sm%s\033[%sm' % (color, msg, 0)
        else:
            print msg

    def _title(self, msg):
        self._pagecount += 1
        self._log('%s. %s' % (self._pagecount, msg), 1)

    def _error(self, msg=None):
        self._log('ERROR: %s' % msg, 31)

