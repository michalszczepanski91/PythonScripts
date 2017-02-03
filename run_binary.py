#! /usr/bin/python
import os

cmd_body = './runMyProgram '
list_option = ['-s ','-a ','-h ']
# range to list_option.length
for i in range (0, 3):
	cmd = cmd_body + list_option[i]
# range to patameters.length
	for j in range (0, 5):
		cmd = cmd_body + list_option[i] + str(j)
		#os.system(cmd)
		print (cmd)
