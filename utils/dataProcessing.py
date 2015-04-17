import sys
import os


def main():

	path = sys.argv[1]

	fileNames = os.walk(path).next()[2]

	part = int(sys.argv[2])
	numberOfSets = 10	

	for i in range(len(fileNames)):

		if i % numberOfSets == part: 

			with open(path+fileNames[i]) as doc:

				content = []
				for line in doc:
					content.append(line.replace("\n", ""))

				print "%d\t"%(i)+" ".join(content)



if __name__ == "__main__":
	main()

