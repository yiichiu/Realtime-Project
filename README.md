# Realtime and Big Data Analysis final project
Build a search engine with semantic results

##Data Source: Wikipedia
[wikipedia dump](https://dumps.wikimedia.org/enwikinews/20150426/)
* 2015-04-26 11:30:56 done All pages, current versions only.

##For Testing purpose, we are using a smaller dataset
[wikipdeia dump strategywiki](https://dumps.wikimedia.org/strategywiki/20150424/)
* 2015-04-24 13:31:37 done All pages, current versions only.

#Reformat input files into N partitions
Before partitioning, you might need to install the following argparse first
```bash
yum install python-argparse
```

##Command:
```bash
sh reformat_all.sh numberOfMapper

```
#Run indexer on hadoop cluster
Before running, you might need to install the following package
nltk

##Command:
```
sh runHadoop.sh src/invertedIndexBuilder
```
#Run the online query file

##command
```
spark-submit --master local[4] online_query.py 

```

#Result
##Smaller dataset (~200MB)
* Query: Batman
  * 
```
First  Pass:
  [3104, 3107, 3109, 3106, 3105, 3110, 2781, 6308, 3158, 4740]
  3104 Batman (1989 film)
  3107 Batman & Robin (film)
  3109 Batman: Year One
  3106 Batman Returns
  3105 Batman (1966 film)
  3110 Talk:Batman
  2781 Blackadder
  6308 Daily Planet
  3158 Barry Goldwater
  4740 Cyborgs in fiction

Key terms:
  set(['catwoman', 'series', 'one', 'states', 'year', 'burton', 'film', 'category', 'joker', 'united', 'accessdate', 'barry', 'goldwater', 'gotham', 'ya', 'batman', 'cyborg', 'date', 'news', 'penguin', 'blackadder', 'name', 'comics', 'work', 'daily', 'planet', '2008', 'warner', 'robin', 'first'])

Second pass:
  [3104, 3106, 2763, 2781, 7100, 4497, 3622, 6105, 3314, 5835]
  3104 Batman (1989 film)
  3106 Batman Returns
  2763 British National Party
  2781 Blackadder
  7100 EastEnders
  4497 Cleveland Browns
  3622 Columbia River
  6105 Don't ask, don't tell
  3314 Ballarat
  5835 David Letterman
```
##Larger dataset (~600MB)


# MapReduce Jobs
## Data Processing
  We preprocess the xml data by assigning each page a document id and splitting them into approximately 20 partitions. 

## Term frequency

###Mapper
* Input: raw xml page
* Output: 
  * key: term
  * value: document id

###Reduce
* Input:
  * key: term
  * value: document id
* Output:
  * key: term
  * value: a dictionary that maps document id to term frequency

## Inverted Document Frequencies

###Mapper
* Input: raw xml page
* Output: 
  * key: term
  * value: document id

###Reduce
* Input:
  * key: term
  * value: document id
* Output:
  * key: term
  * value: inverted document frequency

## Document Store

###Mapper
* Input: raw xml page
* Output: 
  * key: document id
  * value: a tuple containing document title, url, and text

###Reduce
* Input:
  * key: document id
  * value: a tuple containing document title, url, and text
* Output:
  * key: document id
  * value: a tuple containing document title, url, and text

#Difficulties
* Dumbo
  * At first, we tried to use wikipedia with html format and split our dataset inside dumbo, but we can't install any package that we need to parse the data (for example, lxml package)
  * We were able to run some Hadoop job that doesn't require any external package, but that was only for some simple map reduce program from the previous assignments.
  * We tried to email the IT guy but didn't get any response, so we give up using dumbo.

* AWS
  * We also tried to use Amazon Cloud Service to deploy our program, but because of the short amount of time we have left and the tedious environment setup process, we decided to try it only if we have time after testing our program locally.

* Data source / data size
  * We have changed our data source many times from html to xml format for some conveniency reasons.
  * The size of the whole wikipedia data set is around 50GB. So it's very hard for us to even split the data into smaller chunks for map reduce jobs. ( We later heard that it's possible to process it with compressed format).

* Stopwords
  * In our second pass, we use the key terms from the corpus of the top ten document of the first pass, but there are many wikipedia specific stopwords that interfere our result. For example, "rf", "web", "title", "cite", "title".... and some numbers.
  * But we can't just eliminate those words because they might have significant meanings in some cases.
