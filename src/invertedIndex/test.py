import sys
for line in sys.stdin:
	a = line.split('\t')
	for l in a:
		print l
