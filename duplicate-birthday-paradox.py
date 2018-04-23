## Birthday paradox exercise (10.8) from Think Python, p. 101
## If there are 23 students in your class, what are the chances that two of you have the same birthday?
## Generate 10,000 random classrooms with random birthdays for the students, and check for duplicates.

from __future__ import division
import random

def has_duplicates(x):
	t = sorted(x)
	duplicates = 0
	for i,_ in enumerate(t):
		if x[i] == x[i-1]:
			duplicates+=1
	return duplicates > 0

sample_set = []
sample_classes_to_generate = 10000
class_size = 23

#generate the random classrooms
for i in range(sample_classes_to_generate):
	sample_set.append([random.randint(1,365) for i in range(class_size)])

#duplicate birthdays in the classrooms?
duplicate_birthday_classrooms = 0
for i in sample_set:
	if has_duplicates(i) == True:
		duplicate_birthday_classrooms+=1

probability_of_duplicate_birthdays = (duplicate_birthday_classrooms/sample_classes_to_generate) * 100

print(str(probability_of_duplicate_birthdays)+'% percent chance of duplicate birthdays.')
