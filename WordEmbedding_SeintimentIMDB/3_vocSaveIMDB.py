# -*- coding: utf-8 -*-
def save_list(lines, filename):
	# convert lines to a single blob of text
	data = '\n'.join(lines)
	# open file
	file = open(filename, 'w')
	# write text
	file.write(data)
	# close file
	file.close()
 # save tokens to a vocabulary file
save_list(tokens, 'vocab.txt')
#++++++++++++++++++++++++++++++++++++
