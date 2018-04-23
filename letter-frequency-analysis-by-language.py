## uses word.txt and italiano.txt from this repo
## What are the percentage frequencies of the letters in the alphabet in different languages?

from __future__ import division
import string


def process_file(filename):
	hist = {}
	fp = open(filename)
	for line in fp:
		process_line(line, hist)
	return hist

def process_line(line, hist):
	line = line.replace('-','')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = None

def letter_count(word, counter):
	for letter in word:
		counter[letter] = counter.get(letter,0)+1

def letter_frequency(hist):
	counter = {}
	for word in hist:
		letter_count(word, counter)
	return counter

def letter_sum(hist):
	total = 0
	for _,v in hist.iteritems():
		total += v
	return total


def letter_printer(letter, hist, total):
	percent = (hist[letter]/total)*100
	print(letter.upper() + " makes up " + str(percent)	+ " percent of letter occurences.")


def language_frequency(language_file, lang_name):
	'''generate a word list for a language, count letters, make hist of frequency,
	and print the frequencies of the letters.
	language_file is text file, lang_name is string with the name of the language'''

	word_list = process_file(language_file)
	letter_hist = letter_frequency(word_list)
	letter_total = letter_sum(letter_hist)

	print(lang_name + " letter frequencies.")

	for letter in letter_hist:
		letter_printer(letter, letter_hist, letter_total)

language_frequency('words.txt', 'English')
language_frequency('italiano.txt','Italian')
