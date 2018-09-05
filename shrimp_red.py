import random
import math
import numpy
class red:
	def __init__(self):
		self.X_1 = random.random()
		self.W_1 = [random.random()-0.5, random.random()-0.5]
		self.P_1 = numpy.array([[100000000,00000000],
							    [000000000,10000000]])
		self.wZ_12 = 0
		self.Q1=numpy.array([[5000000000,0000000000],
							 [0000000000,5000000000]])
		self.R1=10
		self.g1=1
		
	def step(self, x1, s1, u1, G1):
		self.x1 = x1
		self.s1 = s1
		self.u1 = u1
		self.G1 = G1
		self.X1 = self.X_1
		self.W1 = self.W_1
		self.P1 = self.P_1
		Z1 = numpy.array([ 1/(1+math.exp((-1)*self.s1[0])),
			   1/(1+math.exp((-1)*self.s1[1]))])
		e1 = self.x1-self.X1
		H1 = Z1
		K1 = self.P1@H1/(self.R1+H1.transpose()*self.P1@H1)
		self.W1=self.W1+self.g1*K1*e1
		self.P1=self.P1-K1@H1.transpose()*self.P1+self.Q1
		self.X_1=self.W1.transpose()@Z1+self.G1*self.u1
		self.W_1=self.W1
		self.P_1=self.P1
		self.wZ_12 = self.W1.transpose()@Z1
		return self.wZ_12