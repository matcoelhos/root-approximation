import time

def power(value,exponent):
	if(exponent > 0):
		return value*power(value,exponent-1)
	elif (exponent < 0):
		return(1/power(value,-1*(exponent)))
	else:
		return 1

def root(value, radical, tol):
	upper = value
	lower = 0
	actual = 0
	while(abs(upper-lower) > tol):
		try:
			actual = ((upper+lower)/2)
			p = power(actual,radical)
			if (p < value):
				lower = actual
			elif (p > value):
				upper = actual
			else:
				return actual,abs(upper-lower)
		except KeyboardInterrupt:
			break

	return actual,abs(upper-lower)

t0 = time.perf_counter()
v1,toll = root(2,2, tol=5e-10)
i1 = time.perf_counter()-t0

t0 = time.perf_counter()
v2 = 2**(1/2)
i2 = time.perf_counter()-t0

print('Clc value:',v1,'Time:',i1)
print('Tolerance reached:', toll)
print('Ref value:',v2,'Time:',i2)
print('Calculated error:',abs(v2-v1))
v,_ = root(5,2, tol=1e-15)
print('Clc phi:',(1+v)/2)
print('Ref phi:',(1+5**(1/2))/2)