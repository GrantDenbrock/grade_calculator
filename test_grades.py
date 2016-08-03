import grade_calculator as gc

def test_adding_exam():
	grades = gc.Book()
	grades.add_exam(1,20)
	assert grades.exam == [(1,20)]
	
def test_adding_homework():
	grades = gc.Book()
	grades.add_homework(1,20)
	assert grades.homework == [(1,20)]
	
	
	
def test_adding_homework_ec():
	grades = gc.Book()
	try:
		grades.add_homework(20,5)
		assert False
	except ValueError:
		assert True
	grades.add_homework(20,5,extra_credit=True)
	assert grades.homework == [(20,5)]
	
def test_adding_exam_ec():
	grades = gc.Book()
	grades.add_exam(20, 5, extra_credit=True)
	assert grades.exam == [(20,5)]
	


def test_creation():
	grade = gc.Book()
	assert grade.homework == []
	assert grade.exam == []
	
def test_calculate_grade():
	grade = gc.Book()
	assert grade.calculate_grade() == .50
