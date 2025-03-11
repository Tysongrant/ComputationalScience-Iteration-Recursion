# By L van Veen, Ontario Tech U, 2023.
# Starter code for Steffenson iteration for assignment 2.
#Edited and Completed by Tyson Grant - 100875284 - Ontario Tech, 2023.
# Collaborators: Adam Kolodziejzak - 100874535


import numpy as np

def steff(f,fp,x,epse,epsr,itmx):
# Steffensen iteration for f(x)=0.
#   Input: function handles f and f', floats inital guess x, tolerance for error (epse) and residual (epsr), integer max nur of iterations itmx. 
#   Output: approximate solution x, estimate of error, residual.
    
    #steff_data= []

    for i in range(itmx):                             # Loop over iterations.
        y1 = x                                        # Initializes y1 to x
        
        r = f(y1)                                     # Find f
        df = fp(y1)                                   # Find derivative of f
        dy = -r/df                                    # Updates Newton step
        y2 = y1+dy                                    # adds the Newton step to y1 

        r = f(y2)                                     # find f
        df = fp(y2)                                   # find derivative of f at y2
        dy = -r/df                                    # Updates Newton step
        y3 = y2+dy                                    # adds Newton step to previous step

        x = y1 - (((y2-y1)**2)/(y3-2*y2+y1))          # Evaluates function and sets to x

        err = abs(x-y1)                               # Residual is absolute value of function
        res = abs(r)                                  # Estimate the error

        #steff_data.append([i, x, err, res]) -- used for plotting

        print("Error: ", err)
        print("Residual: ", res, "\n")

        if abs(f(x)) < epse and abs(f(x)) < epsr:     # Checks for convergence based on two criteria
            print("Convergence!")
            break

    if err < epse and res < epsr:                     # print warning message
        print("No Convergence")
    
    return x,err,res                                  # Return floats: approximate intersection of x, approximate error err and residual res.
