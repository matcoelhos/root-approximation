import time

def power(value,exponent):
	if(exponent > 0):
		return value*power(value,exponent-1)
	elif (exponent < 0):
		return(1/power(value,-1*(exponent)))
	else:
		return 1

def root(value, radical, tol = 1e-15):
	upper = value
	lower = 1
	actual = 0
	while(upper-lower > tol):
		actual = (upper+lower)/2
		p = power(actual,radical)
		if (p < value):
			lower = actual
		elif (p > value):
			upper = actual

	return actual

t0 = time.perf_counter()
v1 = root(5,2, tol=1e-16)
i1 = time.perf_counter()-t0

t0 = time.perf_counter()
v2 = 5**(1/2)
i2 = time.perf_counter()-t0

print('Clc value:',v1,'Time:',i1)
print('Ref value:',v2,'Time:',i2)
print('Calculated error:',abs(v2-v1))
print('Clc phi:',(1+v1)/2)
print('Ref phi:',(1+v2)/2)