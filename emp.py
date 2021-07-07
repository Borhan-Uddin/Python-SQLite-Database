
class emp():

	def __init__(self, first_name,last_name,salary):
	    self.first_name = first_name
	    self.last_name = last_name
	    self.salary = salary


	def get_email(self):

		return "{}{}@gmail.com".format(self.first_name,self.last_name)

	def get_salary(self):

		return self.salary