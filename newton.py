# Newton iteration for finding the root of a function. L. van Veen, Ontario Tech U, 2024.
import numpy as np

# Inputs: function handles f and fp (derivative of f), initial guess x0, max nr. of iterations kMax, tolrance for error (epsX) and residual (epsF).
def newton(f,fp,x0,kMax,epsX,epsF):
    x = x0                                         # Convergence flag set to "no convergence" by default.
    conv = 0
    #newton_data = []
    for i in range(kMax):                          # Loop over iterations.
        r = f(x)                                   # Evaluate f...
        df = fp(x)                                 # Evaluate derivative of f
        dx = -r/df                                 # Newton update step
        
        err = abs(dx)                              # Estimate of the error and the residual.
        res = abs(r)

        #newton_data.append([i, x, err, res])      # Used for plotting
        
        print('Iteration %d, err=%e, res=%e' % (i,err,res))
        if err < epsX and res < epsF:              # Check for convergence.
            conv = 1
            print("It Converges")
            break

        x += dx                                    # Update the solution.
        
    if conv == 0:
        print('No convergence!')

    return x,err,res                                # You may want to return the convergence flag, too!
