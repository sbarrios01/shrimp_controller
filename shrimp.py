import math
import time
import random
from shrimp_controller import shrimp_motorcontrol
from shrimp_serial import shrimp2serial
random.seed()
referenceData = list (math.floor(math.cos(((2*math.pi)/127)*i)*127) for i in range (0,255))
inputDataF = list (math.floor((math.cos(((2*math.pi)/127)*i)*(1.0+(random.random()-0.5)/10))*127) for i in range (0,255))
inputDataR = list (math.floor((math.cos(((2*math.pi)/127)*i)*(1.0+(random.random()-0.5)/10))*127) for i in range (0,255))
inputDataL = list (math.floor((math.cos(((2*math.pi)/127)*i)*(1.0+(random.random()-0.5)/10))*127) for i in range (0,255))
inputDataB = list (math.floor((math.cos(((2*math.pi)/127)*i)*(1.0+(random.random()-0.5)/10))*127) for i in range (0,255))
motorF = shrimp_motorcontrol()
motorR = shrimp_motorcontrol()
motorL = shrimp_motorcontrol()
motorB = shrimp_motorcontrol()
serial = shrimp2serial()

for i in range (0,255):
	print (referenceData[i], end=' || ', flush=True)
	print (motorF.step(serial.read(),referenceData[i]), end=' ', flush=True)
	print (motorR.step(inputDataR[i],referenceData[i]), end=' ', flush=True)
	print (motorL.step(inputDataL[i],referenceData[i]), end=' ', flush=True)
	print (motorB.step(inputDataB[i],referenceData[i]))
	serial.write(motorF.outputData[motorF.i-1])
	time.sleep(1/10)
serial.close()