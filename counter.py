""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
#from pickle import dump, load
import pickle

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""

	if exists(file_name) == True: #if we have a file already
		save_file = open(file_name, 'r')
		counter = pickle.load(save_file) #get the counter
		if reset == True: #reset the counter
			counter = 1
		else: #increment the counter
			if 'counter' in locals(): #if it's already there
				counter = counter + 1 # add one
			else: #if it's not already there
				counter = 1 # initialize


		save_file = open(file_name, 'w')
		pickle.dump(counter, save_file)
		save_file.close()
		return counter

	else:
		counter = 1
		save_file = open(file_name, 'w')
		pickle.dump(counter, save_file)
		save_file.close()
		return counter


	# if reset == True:


#			counter = 1
#	else:
#		if 'counter' in locals():
#			counter = counter + 1
#		else:
#			counter = 1











if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest

		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
