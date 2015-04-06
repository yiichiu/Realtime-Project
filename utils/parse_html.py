from lxml import html

def parse_content(filename):
    with open(filename, 'r') as infile:
        data = infile.read().replace('\n', ' ')
    
    tree = html.fromstring(data)
    for ele in list(list(list(list(tree)[1])[3])[9])[10].itertext():
        if ele.strip() != '':
            print ele.encode('utf-8')

if __name__ == '__main__':
    parse_content('../wiki/YouTube')


