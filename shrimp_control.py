import numpy
from numpy.linalg import inv
I = numpy.array([[1,0],
				 [0,1]])
Pr1 = numpy.array([[2.5,2.5],
				   [2.5,2.5]])
G1 = numpy.array([[0.1],
				  [1.0]])

def control (Fi,rs):
	hi=G1.transpose()*Pr1*(Fi-rs)
	Ji=1/2*(G1.transpose())@Pr1@G1
	u=-inv((I+Ji))@hi;
	return u;
	