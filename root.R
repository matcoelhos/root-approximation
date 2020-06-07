power <- function(value,exponent)
{
  if(exponent > 0){
    return(value*power(value,exponent-1))
  }
  else if(exponent < 0){
    return(1/power(value,-1*(exponent)))
  }
  else{
    return(1)
  }
}

root <- function(value, radical, tol)
{
  upper = value
  lower = 0
  actual = 0
	while((upper-lower) > tol)
  {
			actual = ((upper+lower)/2)
			p = power(actual,radical)
			if (p < value){
				lower = actual
			}
			else if (p > value){
				upper = actual
			}
			else{
				break
			}
	}
	return(c(actual,abs(upper-lower)))
}

ans = root(5,2, tol=5e-10)
v2 = 5**(1/2)

print('Clc value:')
print(ans[1])
print('Tolerance reached:')
print(ans[2])
print('Ref value:')
print(v2)
print('Error: ')
print(abs(ans[1]-v2))

ans2 = root(5,2, tol=1e-15)
print('Clc phi:')
print((1+ans2[1])/2)
print('Ref phi:')
print((1+5**(1/2))/2)