import numpy as np
import matplotlib
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

# define plot with 2 subplots
f,(ax1,ax2) = plt.subplots(2)

#ax1 subplot, show every row in the first column of y matrix
preyline, = ax1.plot(t,y[:,0], color="r")
#ax2 subplot, show every row in second column of y matrix
predline, = ax2.plot(t,y[:,1], color="b")

#label axis
ax1.set_ylabel("hare population")
ax2.set_ylabel("lynx population")
ax2.set_xlabel("Time")
#show subplots
plt.show()

