from lxml import html
import urlparse
import sys

def parse_hyperlink(filename):
    with open(filename, 'r') as infile:
        data = infile.read().replace('\n', ' ')

    tree = html.fromstring(data)
    linklist = tree.xpath('./body//p//a')
    linklist.extend(tree.xpath("./body//table[@class='infobox vcard']//a"))
    urls = []

    print '%s\t' %(filename.split('/')[-1]),
    for link in linklist:
        if link.get('href'):
            name = link.get('href')
            if not (name.startswith('http') or name.startswith('.') or name.startswith('#')):
                if name in wiki_names:
                    print '%s' % (name),
    print ''
    

wiki_names = set([])
with open('../wiki_list', 'r') as infile:
    data = infile.readlines()
    for row in data:
        wiki_names.add(row.strip())
for wiki_name in wiki_names:
    parse_hyperlink('../wiki/' + wiki_name)
