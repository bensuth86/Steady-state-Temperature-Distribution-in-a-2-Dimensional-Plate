import numpy as np
import math
import copy

                                    # %INPUTS%
L = 10
W = 20

xmax = float(1/L)
ymax = float(1/W)

increm = input("Enter increments along x -axis:")
increm = float(increm)
dx = float(xmax/increm)
dy = dx

# convergence criteria
e = float(5/10000)

# %Setup initial grid%

x = np.arange(0, xmax + dx, dx)
y = np.arange(0, ymax + dy, dy)

t_ini = np.full((len(y), len(x)), 20.000)

LHE = []
for elem in y:
    LHE.append(float((20 + 180 * math.sin(20 * math.pi * elem))))
    
##print("\n", x)
##print("\n", y)

(t_ini[0:,0]) = LHE
np.around(t_ini, decimals=3)

                                    # % PROCESSING %
# Jacobi method formula
def Jacobie(j,i):
    t_nplusone[j,i] = (t_n[j,i-1]+t_n[j,i+1]+t_n[j-1,i]+t_n[j+1,i])/4
    return t_nplusone[j,i]


# temperature array before nth iteration
t_n = t_ini

# Initial Error array
E = t_ini+1 - t_n


##print ("\n",t_n)
k = 0

# # temperature array after nth iteration
t_nplusone = copy.deepcopy(t_n)



# while loop iterates until difference between arrays for nth and n-1th iterations is less than convergence criteria, e
while np.amax(E[0:,1:]) > e:
    
    for j in np.arange(1, len(y)-1):
        for i in np.arange(1, len(x)-1):
            Jacobie(j,i)
    # error array after previous iteration
    print ("\n", t_nplusone)

    E = t_nplusone - t_n
    error = float(np.amax(E))
    
    t_n = copy.deepcopy(t_nplusone)
    k += 1  # iteration count
    print ("\n %.3f" % error)
##    print ("\n", k)

##print ("\n\n",t_nplusone)

print ("\n Solution converged in %s iterations" % k)
    

