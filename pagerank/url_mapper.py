from lxml import html
import urlparse

def parse_hyperlink(filename):
    wiki_names = set([])
    with open('../wiki_list', 'r') as infile:
        data = infile.readlines()
        for row in data:
            wiki_names.add(row.strip())

    with open(filename, 'r') as infile:
        data = infile.read().replace('\n', ' ')

    tree = html.fromstring(data)
    linklist = tree.xpath('./body//p//a')
    linklist.extend(tree.xpath("./body//table[@class='infobox vcard']//a"))
    urls = []

    for link in linklist:
        if link.get('href'):
            name = link.get('href')
            if not (name.startswith('http') or name.startswith('.') or name.startswith('#')):
                if name in wiki_names:
                    print '%s\t%s' % ( name, filename.split('/')[-1] )
    

parse_hyperlink('../wiki/Google')
