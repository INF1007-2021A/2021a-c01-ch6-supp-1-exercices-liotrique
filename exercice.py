#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	maximums = []
	for i in numbers:
		maximums.append(max(i))

	return maximums

def join_integers(numbers):
	somme = ""
	for number in numbers:
		somme += str(number)
	return int(somme)


def generate_prime_numbers(limit):
	premiers = []
	nombres = [nombre for nombre in range(2, limit +1)]

	while len(nombres) != 0:
		premiers.append(nombres[0])
		nombres = [i for i in nombres if i % nombres[0] != 0]

	return premiers



def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	list = []
	for num in range(1, num_combinations + 1):
		for string in strings:
			if excluded_multiples == None:
				list.append(string + str(num))
			elif num % excluded_multiples != 0:
				list.append(string + str(num))

	return list

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
