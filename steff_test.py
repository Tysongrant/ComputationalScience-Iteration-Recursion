from steff import steff
import numpy as np

def f(x):
    return 148.413-np.exp(-x**2-2.0*x+4.0)

def fp(x):
    return (2.0*x+2.0) * np.exp(-x**2-2.0*x+4.0)

def test_steff():
    x = -0.99
    epse = 1e-10
    epsr = 1e-10
    itmx = 5
    x, err, res = steff(f,fp,x,epse,epsr,itmx)
    
    assert abs(x+0.9989646134522571) < 1e-10

x, err, res = steff(f, fp, -0.99, 1E-10, 1E-10, 5)

print(x)
