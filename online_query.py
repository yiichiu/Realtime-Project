import re
import sys
import nltk
from pyspark import SparkContext

sc = SparkContext(appName="Query")
tf = sc.textFile("realtime/tf_file")
tf_pairs = tf.map(lambda x: (x.split("\t")[0], x.split("\t")[1]))

idf = sc.textFile("realtime/idf_file")
idf_pairs = idf.map(lambda x: (x.split("\t")[0], float(x.split("\t")[1])))

fileContent = sc.textFile("realtime/content_file")
content_pairs = fileContent.map(lambda x: (int(x.split("\t")[0]), eval(x.split("\t")[1])))
docID_to_content = dict(content_pairs.map(lambda (k,v): (k, v['title'])).collect())

def get_document_id(phrase_to_search):
    words_to_search = set(phrase_to_search.split(' '))
    num_of_words = len(words_to_search)
    
    def parse_dict(key, string):
        elements = string.split(',')
        elements[0] = elements[0].split('{')[1]
        elements[-1] = elements[-1].split('}')[0]
        result = []
        for element in elements:
            docID, tf = map(int, element.strip().split(': '))
            result.append((docID, [(key, tf)]))
        #result = map((lambda x: tuple(map(int, x.strip().split(': ')))), elements)
        return result
    
    word_idf = dict(idf_pairs.filter(lambda (k,v): k in words_to_search).collect())
    
    def get_score(word_tf_list):
        total_score = 0
        for word, tf in word_tf_list:
            total_score += tf*word_idf[word]
        return total_score
    
    
    related = tf_pairs.filter(lambda (k,v): k in words_to_search)
    all_docs = related.flatMap(lambda (k,v): parse_dict(k, v)).reduceByKey(lambda a, b: a + b).filter(lambda (k,v): len(v) >= max(num_of_words-1,1)).map(lambda (k,v): (k, get_score(v))).collect()
    top_docs = [k for (k,v) in reversed(sorted(all_docs, key=lambda x:x[1])[max(-10, -len(all_docs)):])]
    top_docs_set = set(top_docs)

    top_docs_content = content_pairs.filter(lambda (k, v): k in top_docs_set)
    top_docs_text = top_docs_content.map(lambda (k,v): v['text']).flatMap(lambda x: x.lower().split(' ')).map(lambda x: (x,1)).reduceByKey(lambda a, b: a+b)
    top_words = set([x for (x,y) in sorted(top_docs_text.join(idf_pairs).map(lambda (k,v): (k, v[0]*v[1])).collect(), key=lambda x: x[1])[-30:]])
    
    semantic_idf = dict(idf_pairs.filter(lambda (k,v): k in top_words).collect())
    def get_semantic_score(word_tf_list):
        total_score = 0
        for word, tf in word_tf_list:
            total_score += tf*semantic_idf[word]
        return total_score
    
    semantic_related = tf_pairs.filter(lambda (k, v): k in top_words)
    new_all_docs = semantic_related.flatMap(lambda (k,v): parse_dict(k, v)).reduceByKey(lambda a, b: a + b).map(lambda (k,v): (k, get_semantic_score(v))).collect()
    top_new_all_docs = [k for (k,v) in reversed(sorted(new_all_docs, key=lambda x:x[1])[max(-10, -len(new_all_docs)):])]
    return top_docs, top_words, top_new_all_docs

phrase_to_search = str(raw_input("Please enter your query (EXIT to stop): "))
#phrase_to_search = 'batman joker'
while phrase_to_search != 'EXIT':
    top_docs, top_words, semantic_top_docs = get_document_id(phrase_to_search)
    print top_docs
    for top_doc in top_docs:
        print top_doc, docID_to_content[top_doc]
    print top_words
    print semantic_top_docs
    for top_doc in semantic_top_docs:
        print top_doc, docID_to_content[top_doc]
    phrase_to_search = str(raw_input("Please enter your query (EXIT to stop): "))

