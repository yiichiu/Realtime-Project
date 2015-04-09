from lxml import html
from nltk.tokenize import RegexpTokenizer

def parse_content(filename):
    tokenizer = RegexpTokenizer(r'\w+')

    with open(filename, 'r') as infile:
        data = infile.read().replace('\n', ' ')
    
    tree = html.fromstring(data)
    word_count = {}
    for ele in list(list(list(list(tree)[1])[3])[9])[10].itertext():
        if ele.strip() != '':
            for token in tokenizer.tokenize(ele.lower()):
                if token not in word_count:
                    word_count[token] = 0
                word_count[token] += 1
    for ele in word_count.keys():
        if word_count[ele] > 10:
            print ele, word_count[ele]

if __name__ == '__main__':
    parse_content('wiki/Google')


