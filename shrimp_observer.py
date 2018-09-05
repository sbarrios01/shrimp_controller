k1 =    .99
J  = 0.0002
Kt = 0.0145
b  = 0.0002

def observe (T,x1ref_k1,e1_k,x1_k):
	x2refk = J/Kt*(1/T*(-x1_k+x1ref_k1+k1*e1_k)+(b/J)*x1_k)
	return x2refk