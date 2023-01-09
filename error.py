class Error(object):
	"""docstring for Error"""
	def __init__(self):
		super(Error, self).__init__()
	def pop1(self,word):
		return (f"'{word}' is not correct\n re-enter the function again like the example\n a*x^n+...+C")
	def pop2(self):
		return f"min x should be less than max x"
