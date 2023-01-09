import re
from error import Error
from func import input_Equation
class Valid(object):
	"""docstring for valid"""
	def __init__(self, arg,x):
		super(Valid, self).__init__()
		self.string = arg
		self.validwords = ['x','cosin','sin','exp','sqrt','+','/','^','*','-']
		self.valid=True
		self.value=x
	def check(self,val):
		# now check if the argumnet has the values specifed
		pattren=r'[a-zA-Z_]+'
		#loop through and check the word is in the list
		for word in re.findall(pattren,self.string):
			if word not in self.validwords:
				return False
		try:
			val.evaluate(self.value)
		except:
			return False
		return True
v=Valid("3x^2+5",10)
inp=input_Equation("3x^2+5")
inp.trans()
if v.check(inp):
	print("Nice")
else:
	e=Error()
	print(e.pop1(v.string))
	# there are some const function that doesn't have an x
