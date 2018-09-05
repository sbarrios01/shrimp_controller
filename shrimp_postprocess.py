class post:
	def __init__(self):	
		self.max = 5588
	
	def postprocess (self,u):
		Pulsesperturn = (u/12)*5500
		if (Pulsesperturn > self.max):
			self.max = Pulsesperturn
		elif (Pulsesperturn < -self.max):
			 self.max = -Pulsesperturn
		return int(Pulsesperturn*(127/self.max))