#grade_calculator

class Book(object):
	
	cat = {"homework" : .75 ,
		   "exam" : .25,
		   }
	
	def __init__(self):
		self.homework = []
		self.exam = []
	
	def add_exam(self, earned, possible, extra_credit = False):
		if extra_credit == False:
			if earned > possible:
				raise ValueError
		self.exam.append((earned, possible))
		
	def add_homework(self, earned, possible, extra_credit = False):
		if extra_credit == False:
			if earned > possible:
				raise ValueError
		self.homework.append((earned, possible))
	
	def calculate_grade(self):
		raise NotImplementedError
		
	
