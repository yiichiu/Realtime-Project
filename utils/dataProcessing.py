import sys
import os

"""
python dataProcessing wiki/ 20 dataser/out
"""

def main():

	path = sys.argv[1]

	fileNames = os.walk(path).next()[2]

	numberOfSet = int(sys.argv[2])

	outputName = sys.argv[3]

	fp = [open(outputName+".%d"%(i), "w") for i in range(numberOfSet)]

	for i in range(len(fileNames)):

		with open(path+fileNames[i]) as doc:

			content = []
			for line in doc:
				content.append(line.replace("\n", ""))

			#print "%d\t"%(i)+" ".join(content)

			fp[i % numberOfSet].write("%d\t"%(i)+" ".join(content)+"\n")


if __name__ == "__main__":
	main()






