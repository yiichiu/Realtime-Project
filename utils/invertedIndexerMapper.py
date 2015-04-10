from lxml import html
from nltk.tokenize import RegexpTokenizer
import sys
def parse_content(filename):
    tokenizer = RegexpTokenizer(r'\w+')

    with open(filename, 'r') as infile:
        data = infile.read().replace('\n', ' ')
    
    tree = html.fromstring(data)
    for ele in list(list(list(list(tree)[1])[3])[9])[10].itertext():
        if ele.strip() != '':
            for token in tokenizer.tokenize(ele.lower()):
              print '%s\t%s' % (token.encode('utf-8'), sys.argv[1])

if __name__ == '__main__':
    fileName = sys.argv[1]
    parse_content('wiki/%s' % fileName) 


