

class MarksHighError(Exception):
	pass


class MarksLowError(Exception):
	pass


class SubjectCountLowError(Exception):
	pass


class SubjectCountZeroError(Exception):
	pass


class MarksOfStudents:

	def __init__(self):
		self.subject_count = int(input("How many subjects do you have? "))
		self.marks_list = []
		if self.subject_count == 0:
			raise SubjectCountZeroError("subject count is zero")
		elif self.subject_count >= 4:
			for _ in range(self.subject_count):
				mark = int(input("Enter your marks "))
				if mark > 100:
					raise MarksHighError("marks are too high")
				elif mark < 0:
					raise MarksLowError("marks are too low")
				self.marks_list.append(mark)
			self.total_marks = "Your total mark is " + str(self.total_marks_list())
			self.percent_marks = "Your percent is " + str(self.percent_marks_list())
			self.grade_marks = "Your grade is " + str(self.grade_marks_list())
		else:
			raise SubjectCountLowError("subjects are too low to evaluate")

	def return_marks(self):
		return [self.total_marks, self.percent_marks, self.grade_marks]

	def total_marks_list(self):
		return sum(self.marks_list)

	def percent_marks_list(self):
		return self.total_marks_list() // self.subject_count

	def grade_marks_list(self):
		return self.grade(self.percent_marks_list())

	@staticmethod
	def grade(n: int):
		if 90 <= n <= 100:
			return "A1"
		elif 80 <= n <= 90:
			return "A2"
		elif 70 <= n <= 80:
			return "B1"
		elif 60 <= n <= 70:
			return "B2"
		elif 50 <= n <= 60:
			return "C1"
		elif 40 <= n <= 50:
			return "C2"
		elif 35 <= n <= 40:
			return "D"
		elif 20 <= n <= 35:
			return "E1"
		else:
			return "E2"




