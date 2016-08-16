import argparse
import lbl
import re

def tokenize(filename):	
	file = open(filename).read()
	sentences = re.split('!?.\n', file)
	return [s.split(" ") for s in sentences]

def train(filename):	
	sentences = tokenize(filename)
	lm = lbl.LBL(sentences)
	
def evaluate(filename, net):
	sentences = tokenize(filename)
	lm = lbl.LBL()
	lm.load(net)
	lm.perplexity(sentences)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()	
	parser.add_argument('--train', default=None, metavar="FILE",
						help='Train text file')
	parser.add_argument('--ppl', default=None, metavar="FILE",
						help='Computes PPL of net on text file (if we train, do that after training)')
	parser.add_argument('--net', default=None, metavar="FILE",
						help='Net file to load')
						
	args = parser.parse_args()
	
	if args.train:
		train(args.train)

	if args.ppl and args.net:
		evaluate(args.ppl, args.net)