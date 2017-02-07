#! /usr/bin/python

import commands, os, os.path, sys, string, glob

def returnVector(vector, pathAndNameFiles, searched_string):
   """Function returns vector which is preceded by string third argument.
   """
   TXT = open(pathAndNameFiles, 'r')
   lines = TXT.readlines()
   lines = [ x.strip() for x in lines ]
   vector_temp = []
   for idx, line in enumerate(lines):
      if (line == searched_string):
         vector_temp = [ float(x) for x in lines[idx+1].split()]
         vector.extend(vector_temp)
#        vector.append(vector_temp)  #this give [[value]]
   return;


# call for program
if len(sys.argv) < 2:
	print "******************** ERROR **************************"
	print "arguments:"
	print "give a full path to files"
	print "..."
	sys.exit(0)
	
os.system('clear')
	
# GLOBAL DEF:
# if you want to push it to txt file
save_to_txtFile = True
#save_to_txtFile = None
INPUTpathAndNameFile = sys.argv[1]
OUTPUTpathAndNameFile = INPUTpathAndNameFile + '_output.txt'
searched_string = 't'
Vector_Found = []

# main
returnVector(Vector_Found, INPUTpathAndNameFile, searched_string);

print Vector_Found

if save_to_txtFile:
   output_file = open(OUTPUTpathAndNameFile, "w")
   output_file.write("%s\n" % Vector_Found)
   output_file.close()
	
sys.exit(0)
