##Think Python chapter 9 exercises - import a dictionary of words (words.txt, in this repository),
##and define functions to do statistical analysis on the dictionary.

from __future__ import division

fin = open('words.txt')

word_list = []

for lines in fin:
	words = lines.split()
	for word in words:
		word_list.append(word)

def has_no_e(word):
	return 'e' not in word

def avoids(word, forbidden_string):
	counter = 0
	for letter in forbidden_string:
		if letter in word:
			counter += 1
	return counter > 0

def uses_only(word, test_string):
	counter = 0
	for letter in test_string:
		if letter not in word:
			counter += 1
	return counter <= 0

def uses_all(word, test_string):
	counter = 0
	for letter in test_string:
		if letter in word:
			counter += 1
	return counter == len(test_string)

def is_abecedarian(word):
	previous = ''
	for letter in word:
		if letter < previous:
			return False
		else:
			previous = letter
	return True

abecedarian_words = []

for word in word_list:
	if is_abecedarian(word):
		abecedarian_words.append(word)

