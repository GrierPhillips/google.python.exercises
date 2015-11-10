"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def word_count_dict(filename):
	#will write dict of word, count for use by print_words and print_top.
	wordcount = {}
	input_file = open(filename, 'r')
	for line in input_file:
		words = line.split()
		for word in words:
			word = word.lower()
			if word in wordcount:
				wordcount[word] += 1
			else:
				wordcount[word] = 1
	input_file.close()
	return wordcount
	
def print_words(filename):
	word_count = word_count_dict(filename)
	words = sorted(word_count.keys())
	for word in words:
		print(word, word_count[word])

def get_count(word_count_tuple):
	#get_count returns the value of counts in word, count tuples.
	return word_count_tuple[1]
		
def print_top(filename):
	word_count = word_count_dict(filename)
	#word_count is a dict of word , count tuples. 
	#sort word_count by count descending. Use reverse = True and key = get_count.
	items = sorted(word_count.items(), key=get_count, reverse=True)
	#print top 20 words
	for item in items:
		print(item[0], item[1])		
	


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
