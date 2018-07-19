import pickle
from pymongo import MongoClient
import os

class Company_name:
	
	""" __doc__  about the code goes here"""

	employee_count=0 							# class variable
	sec_global=None
	os.system("start cmd /k python start_mongodb.py")
	global client 								# global varible
	client = MongoClient('localhost', 27017)	# Establish connection with MongoDb localhost port 27017 using MongoClient

	def __init__(self, name, age, gender, interest, experience, sepcializaion, salary):
		self.name= name                         
		self.age= age
		self.gender= gender
		self.interest= interest
		self.experience= experience				# _int_ method
		self.sepcializaion= sepcializaion
		self.salary= salary

		Company_name.employee_count+=1

	def database(self):
		global db 
		global collection
		db = client.employee_info               # database name (use pymongo_test)
		collection = db.major_section	        # collection or tables (db.createCollection("collection name"))
		post_data={								# dictionary of data (of employees)
			"Name": self.name,
			"Age": self.age,
			"gender": self.gender,
			"interest": self.interest,
			"experience": self.experience,
			"sepcializaion": self.sepcializaion,
			"salary": self.salary
		}
		result = collection.insert(post_data)	# inserting the data using mongoDB insert() method
	
	def display_mongo_database(self):
		dsip= collection.find()					# display the mongoDB entry
		for x in dsip:
			print(x)
		
	def pickle_backup(self):					# funcition to demonstrate pickle dump
		emp_dict={"Name":self.name, "age":self.age, "gender":self.gender, "interest":self.interest," experience":self.experience,
		"sepcializaion":self.sepcializaion, "salary":self.salary}
		sec_store=open("Path\\to\\your\\desired_directory\\file_name.data","wb+")
		pickle.dump(emp_dict, sec_store)
		sec_store.close()

	def pickle_display(self):					# function to demonstrate pickle 
		read_pick=open("Path\\to\\your\\desired_directory\\file_name.data","rb+")
		avar=pickle.load(read_pick)
		print(avar)

	def display(self):
		print("Name:", self.name, "\n Age:", self.age, "\n Gender :", self.gender, "\n interest :", self.interest, \
			"\n experience :",self.experience, "\n sepcializaion :",self.sepcializaion, "\n Salary :", self.salary )
		return self

	@classmethod								# code to demonstrate class method
	def print_name(cls, name):
		cls.name=name
		print(cls.name)
		return (cls.name)

	def class_info(self):
		print(Company_name.__doc__)
		print("This is the name of class",Company_name.__name__)
		print(Company_name.__module__)
		print(Company_name.__bases__)
		print(Company_name.__dict__)
		print(Company_name.__class__)

	def __del__(self):							# code to __del__ method
		print("Deleted")


em=Company_name("XYZ",26,"male","data science", "2 yrs", "Bioinformatics","15K ")		#############################
em.display()																			##### accept user input######
em.class_info()																			######### instead ###########
print(getattr(em,'salary'))						# get attribute function 
em.pickle_backup()
em.pickle_display()
em.database()
em.display_mongo_database()
new_meth= Company_name.print_name(input("Enter name:"))
