from HTMLParser import HTMLParser
import urlparse
import sys


class MyHTMLParser(HTMLParser):
    is_link = False
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.is_link = True
            #print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        if tag == 'a':
            self.is_link = False
            #print "Encountered an end tag :", tag
    def handle_data(self, data):
        if self.is_link == True and data.strip() != '':
            print "Encountered some data  :", data


with open('../wiki/Google', 'r') as infile:
    data = infile.read().replace('\n', ' ')

parser = MyHTMLParser()
parser.feed(data)
print parser

