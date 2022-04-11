import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# initial condition
y0 = [30,4]

#time points to solve over with the interval
t = np.linspace(1900,1920,num=1000)

# parameter values
a = 4
b = 0.2
m = 0.07
n = 0.3

# collect parameters as a list
params = [a, b, m, n]

# function that returns dy/dt
def model(variables,t,params):
    # hare populataion level
    x = variables[0]
    # lynx population level
    y = variables[1]
    #define parameters as respective listed values in the function
    a = params[0]
    b = params[1]
    m = params[2]
    n = params[3]
    # ODE's
    dxdt = a*x-b*x*y
    dydt = m*x*y-n*y
    return([dxdt,dydt])

# solve ODE
y = odeint(model,y0,t,args=(params,))

# define hares and lynx from output
hares = y[:,0]
lynx = y[:,1]

# plot output as phase-diagram
plt.plot(hares, lynx, '-', lw=1, color='purple')
plt.xlabel('amount of hares $r$')
plt.ylabel('amount of lynx $F$')
plt.title('phasespace')
plt.show()
#