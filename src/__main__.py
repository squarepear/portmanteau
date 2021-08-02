"""
Jeffrey Harmon
Portmanteau.py
Aug. 1, 2021
"""

import getopt, inspect, os, sys

from process import process


def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hf:", [ "help", "file=" ])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)

	filename = None
	words = None

	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-f", "--file"):
			filename = a

	words = args

	if filename != None and os.path.isfile(filename):
		file = open(filename, "r")

		for word in file.readlines():
			if word.strip() != "":
				words.append(word.strip().lower())

		file.close()

	print(process(words))


def usage():
	print(inspect.cleandoc("""
		Portmanteau.py

		USAGE:
		   portmanteau [OPTIONS] [WORDS]

		OPTIONS:
		   -h, --help       	Prints this message
		   -f, --file <FILE>	File to import list of words

		ARGS:
		   [WORDS]... Words to combine.
	"""))


if __name__ == "__main__":
	main()
