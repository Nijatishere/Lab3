
x = 0.1
epilon=0.01

term = x 
sum_P = term

n = 2  
sign = -1 

while abs(term) >= epsilon:
    term = sign * (x ** n) / n  
    sum_P += term  
    sign *= -1 
    n += 1  

print(sum_P)
