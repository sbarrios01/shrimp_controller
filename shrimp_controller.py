import math
import time
import random
import numpy
from shrimp_red import red
import shrimp_observer
from shrimp_postprocess import post
import shrimp_control

class shrimp_motorcontrol:
	def __init__(self):
		#serial = shrimp2serial()
		#self.referenceData = list (math.floor(math.cos(((2*math.pi)/127)*i)*127) for i in range (0,255))
		#self.inputData = list (math.floor((math.cos(((2*math.pi)/127)*i)*(1.0+(random.random()-0.5)/10))*127) for i in range (0,255))
		self.referenceData=[]
		self.inputData=[]
		self.outputData=[]
		self.x1=[]
		self.x2=[]
		self.red_x1 = red()
		self.red_x2 = red()
		self.G1 = 0.1
		self.G2 = 2
		self.wZ_12_1 = []
		self.wZ_12_2 = []
		self.T = 0.00001#Cambiar por el periodo
		self.x2refk1 = []
		self.u = [numpy.array([[-146.38890568,-1463.88905683],
							   [ 264.19661551, 2641.96615514]])]
		self.postP = post()
		self.postP.max=1200000
		self.i = 0
		

#for i in range (0,255):
#	print (referenceData[i], end=' ', flush=True)
	#x1.append((inputData[i]*2*math.pi)/5504)
	#x2.append(((inputData[i]/5588)*12)/8.71)
#print("---------------------")
#for s in range (0,1):
#	for i in range (0,255):
	def step(self,input,reference):
		self.inputData.append(input)
		self.referenceData.append(reference)
		self.x1.append((self.inputData[self.i]*2*math.pi)/5504)
		self.x2.append(((self.inputData[self.i]/5588)*12)/8.71)
		self.wZ_12_1.append(self.red_x1.step(self.x1[self.i],[self.x1[self.i],self.x2[self.i]],self.x2[self.i],self.G1))
		self.wZ_12_2.append(self.red_x2.step(self.x2[self.i],[self.x1[self.i],self.x2[self.i]],self.u[self.i][0,0],self.G2))
		self.x2refk1.append(shrimp_observer.observe(self.T,self.referenceData[self.i],self.wZ_12_1[self.i]-self.referenceData[self.i],self.wZ_12_1[self.i]))#Add delays
		self.u.append(shrimp_control.control(numpy.array([[self.wZ_12_1[self.i]],[self.wZ_12_2[self.i]]]),numpy.array([[self.referenceData[self.i]],[self.x2refk1[self.i]]])))
		self.outputData.append(self.postP.postprocess(self.u[self.i+1][1,1]))
		self.i = self.i+1
		return self.outputData[self.i-1]
		#outputData.append((inputData[self.i]*2)-((referenceData[self.i])))
		#serial.write(outputData[self.i])
		#print (u[self.i+1], end=' ', flush=True)
		#print (self.outputData[self.i], end=' ', flush=True)
		
		#time.sleep(1/10)
#serial.close()
		