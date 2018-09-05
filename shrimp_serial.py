import serial
from binascii import hexlify

class shrimp2serial:
	def __init__(self):
		self.uart = serial.Serial("COM6",57600,timeout=0.5)
				#Initialize
		self.uart.write(bytes([2]))
		buffer = 0
		buffer = self.uart.read(1)
		#print ("Serial read: "+str(hexlify(buffer)))
	
	def write (self, value):
		self.uart.write(bytes([4]))
		self.uart.write(value.to_bytes(1,'big',signed=True))
		self.uart.write(bytes([0]))
		buffer = 0
		buffer = self.uart.read(1)
		#print ("Serial read: "+str(hexlify(buffer)))#0x04
		
	def read (self):
		self.uart.write(bytes([5]))
		buffer = self.uart.read(1)
		#print ("Serial read: "+str(hexlify(buffer)))#0x05
		buffer = self.uart.read(1)
		#print ("Serial read: "+str(hexlify(buffer)))#velocitypython
		velocity = int.from_bytes(buffer,'big',signed=True)
		buffer = self.uart.read(1)
		#print ("Serial read: "+str(hexlify(buffer)))#Steering angle
		return velocity
	def close (self):
		self.uart.write(bytes([3]))
		buffer = self.uart.read(1)
		self.uart.close()
		