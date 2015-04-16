python utils/invertedIndexerMapper.py $1 | sort | python utils/invertedIndexerCombiner.py | python utils/invertedIndexerReducer.py
