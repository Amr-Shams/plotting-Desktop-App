
class input_Equation(object):
	"""docstring for input"""
	def __init__(self, arg):
		super(input_Equation, self).__init__()
		self.string = arg
		self.rep={'^':'**','cos':'np.cos','sin':'np.sin','sqrt':'np.sqrt','exp':'np.exp',}
	def trans(self):
		# now validate the input
		for value,key in self.rep.items():
			self.string=self.string.replace(value,key)
		if "x" not in self.string:
			self.string=f"{self.string}+0*x"
	def evaulate(self,x):
		return eval(self.string)