import math  
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

    def R(lambda0):
   o = 0
    n1 = 2.5
    l1 = lambda0 / (4 * n1)
    h = n1 * l1 * math.cos(o)

    mu0 = 4 * math.pi * pow(10, -7)
    epsilon0 = 8.85 * pow(10, -12)
    gamma1 = math.sqrt(epsilon0 / mu0) * n1 * math.cos(o)
    gamma0 = math.sqrt(epsilon0 / mu0)

step=0.011
first=800
final=2500
num=int((final - first)/step)

for d in np.arange(1,num+2):
       Landa_val= first+(step*(d-1))

    k = (2 * math.pi) / lambda0
    i = 1
    M11 = math.cos(k * h)
    M12 = (i * math.sin(k * h)) / gamma1
    M21 = i * gamma1 * math.sin(k * h)
    M22 = math.cos(k * h)

  r = pow(abs(((M11 * gamma0) + (M12 * gamma0 * gamma1) - M21 - M22) / ((M11 * gamma0) + (M12 * gamma0 * gamma1) + M21 + M22)), 2)

return r

lambda_values = []
reflectance_values = []

for lambda_val in lambda_values:
    reflectance_values.append(R(lambda_val))

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.17f'))
fig.set_figheight(5)
fig.set_figwidth(15)
plt.plot(lambda_values, reflectance_values)

plt.show() 
