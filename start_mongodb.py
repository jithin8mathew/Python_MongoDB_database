import os
from os.path import join
import itertools, sys

class setup_mongod:
	''' class contains functions to start mongodb '''

	def __init__(self,var):
		self.var= var

	def search_for_db(self):
		print("Search in progress ")
		spinner= itertools.cycle(["-","/","|","\\"])				# function to search the PC for mongod.exe
		for root, dirs, files in os.walk('C:\\Program Files\\'):
			sys.stdout.write(next(spinner))							
			sys.stdout.flush()
			sys.stdout.write('\b')
			if self.var in files:
				print ("found: %s" % join(root, self.var))
				os.chdir(root)										# change the location to the folder containing mongod.exe
				os.system(self.var) 
				break

start=setup_mongod("mongod.exe")				
start.search_for_db()