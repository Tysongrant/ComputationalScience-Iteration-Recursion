# Author: L. van Veen, UOIT 2023. Starter script for assignment 2, Q2.
import numpy as np
import matplotlib.pyplot as plt
from steff import steff
from newton import newton

# Question 2
def f(x):
    return np.exp((-x**2)+x) - 0.5*x - 1.0836
def fp(x):
    return np.exp((-x**2)+x)*((-2*x)+1)-0.5

# Find reasonable values for residual and error tolerance and the number of iterations:
tol_err = 1E-10
tol_res = 1E-10
itmax = 15

# initial point
x0 = 1.0

# First try Newton iteration:
print("Calling Newton function...")
x,err,res = newton(f,fp,x0,itmax,tol_err,tol_res)
print("Covergence Value: ", x)

print("\n")

# That converges slowly, now try steffenson
print("Calling Steffensen function...")
x,err,res = steff(f, fp, x0, tol_err, tol_res, itmax)
print("Covergence Value: ", x)


'''

CODE TO PLOT GRAPHS, PROFESSOR SAID TO COMMENT IT OUT/DELETE IT SO THE 4TH RETURN VARIABLE IN FUNCTIONS 
WOULD NOT CAUSE A PROBLEM IN AUTOGRADING SYSTEM

I created dictionary in Steff and Newton functions, then appended the values needed to creates the graphs,
returned these dictionaries as an array using np.asarray( ...) and then used them to plot as seen below.

Dictionaries were called 'steff_data' and 'newton_data'

plt.semilogy(newton_data[:,0], newton_data[:,2], marker="x",label='Newton', color='r')
plt.semilogy(steff_data[:,0], steff_data[:,2], marker='x', label='Steff', color='b')
plt.legend()
plt.title("Error vs Num. of Iter.")
plt.xlabel("Number of Iterations")
plt.ylabel("Error")
plt.grid(True)
plt.show()

plt.semilogy(newton_data[:,0], newton_data[:,3], marker="x",label='Newton', color='r')
plt.semilogy(steff_data[:,0], steff_data[:,3], marker='x', label='Steff', color='b')
plt.legend()
plt.title("Residual vs Num. of Iter.")
plt.xlabel("Number of Iterations")
plt.ylabel("Residual")
plt.grid(True)
plt.show()
'''



