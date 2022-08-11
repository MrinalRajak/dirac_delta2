
# Integrating the dirac delta function2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2)
def d(x):
    return (n/(np.sqrt(np.pi)))*(np.exp(-(n**2*(x-np.pi)**2)))*f(x)

n=int(input("Enter the value of n: "))
a=np.pi-50
b=np.pi+50
x=np.arange(a,b,0.1)
R=[]
for i in range(10):
    R.append(quad(lambda x:d(x),a,b)[0])
    i+=1

print(R)
print("function: ",f(np.pi))
plt.plot(x,d(x))
plt.xlabel("x-value")
plt.ylabel("delta-value")
plt.grid(True)
plt.show()

