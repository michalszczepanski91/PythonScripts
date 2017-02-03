#! /usr/bin/python
import os

# call for program
cmd_body = './runMyProgram '
# possible option
# -n normal
# -f fast
# -h help
list_option = ['-n ','-f ','-h ']

#print list_option.length
for idx, option in enumerate(list_option):
	# range to patameters.length
	for j in range (0, 5):
		cmd = cmd_body + option +str(j)
#		os.system(cmd)
		print (cmd)
