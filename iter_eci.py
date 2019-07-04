import numpy as  np
import copy 
c=np.array([[1.,1.,1.,1.],[0.,1.,0.,0.],[0.,0.,1.,1.],[0.,0.,0.,1.]])
def eci(c)
	c.astype(np.float64)
	a=c.sum(1)
	b = c.sum(0)
	a0 = copy.deepcopy(a)
	b0 = copy.deepcopy(b)
	for _ in range(100):
		a1 = copy.deepcopy(a)
		for i in range(len(a)):
			a1[i] = 1.0*sum([b[j] for j in range(len(a)) if c[i,j]])/a0[i]
		b1 = copy.deepcopy(b)
		for j in range(len(b)):
			b1[j] =  1.0*sum([a[i] for i in range(len(b)) if c[i,j]])/b0[j]
		print(a1,b1)
		a=a1
		b=b1
	return a,b
