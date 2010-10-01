#!/usr/bin/python
import re
import urllib2
import random

p_tropic_head = re.compile('<TD width="')
p_tropic_tail = re.compile('<\/TD><\/TR>')
p_tropic_get = re.compile('>([^<]+)<\/')

p_adj_head = re.compile('<span class="style58">')
p_adj_get = re.compile('>([^<]+)<\/')
p_adj_skip = re.compile('nbsp')

tropic_cache = []
tropicurl = ('http://www.hko.gov.hk/prtver/html'
             '/docs/informtc/sound/tc_pronunciation2008e.shtml')

adj_cache = []
adjurl = 'http://www.keepandshare.com/doc/12894/adjective-list?p=y'


def get():
    if len(tropic_cache) == 0:
        build_cache()
    return '%s %s' % (random.choice(adj_cache), random.choice(tropic_cache))


def build_cache():
    f = urllib2.urlopen(tropicurl)
    for line in f.readlines():
        if p_tropic_head.search(line) and not p_tropic_tail.search(line):
            m = p_tropic_get.search(line)
            try:
                m = m.group(1)
                tropic_cache.append(m.lstrip().rstrip('* ').capitalize())
            except:
                pass
    f.close()

    f = urllib2.urlopen(adjurl)
    for line in f.readlines():
        if p_adj_head.search(line):
            m = p_adj_get.search(line)
            try:
                m = m.group(1)
                if not p_adj_skip.search(m):
                    adj_cache.append(m.lstrip().rstrip('. ').capitalize())
            except:
                pass
    f.close()


for x in xrange(0, 10):
    print get()
