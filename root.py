import time

def power(value,exponent):
	ans = value
	while(exponent > 1):
		ans *= value
		exponent -= 1
	return ans

#Bisection method
def root(value, radical, tol = 1e-10):
	upper = max(value,1)
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

#Newton's method
def rootn(value, radical, tol = 1e-10):
	upper = max(value,1)
	lower = 0
	last = 0
	actual = ((upper+lower)/radical)
	while(abs(actual-last) > tol):
		try:
			last = actual
			#actual = actual - (power(actual,radical) - value)/(radical*power(actual,radical-1))
			actual = (1 - 1/radical)*actual + value/(radical*power(actual,radical-1))
		except KeyboardInterrupt:
			break
	return actual,abs(actual-last)

t0 = time.perf_counter()
v1,toll = root(5,2)
i1 = time.perf_counter()-t0

t0 = time.perf_counter()
v2,toll2 = rootn(5,2)
i2 = time.perf_counter()-t0

t0 = time.perf_counter()
v3 = 5**(1/2)
i3 = time.perf_counter()-t0

print('Bsc value:',v1,'Time:',i1)
print('Tolerance reached:', toll)
print('Nwt value:',v2,'Time:',i2)
print('Tolerance reached:', toll2)
print('Ref value:',v3,'Time:',i3)
v,_ = rootn(5,2, tol=1e-10)
print('Clc phi:',(1+v)/2)
print('Ref phi:',(1+5**(1/2))/2)