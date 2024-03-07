import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def R( lambda0 ):
    
    o = 0
    n1 = 2.5
    l1 = lambda0 / ( 4 * n1 )
    h = n1 * l1 * math.cos(o)
    
    mu0 = 4 * math.pi * pow(10, -7)
    epsilon0 = 8.85 * pow(10, -12)
    
    gamma0 = math.sqrt( epsilon0 / mu0 )
    gamma1 = math.sqrt( epsilon0 / mu0 ) * n1 * math.cos(o)
    
    k = ( 2 * math.pi ) / lambda0
    i = 1
    M11 = math.cos( k * h)
    M12 = ( i * math.sin( k * h ) ) / gamma1
    M21 = i * gamma1 * math.sin( k * h )
    M22 = math.cos( k * h )
    
    r = pow( abs( ( (M11 * gamma0) + (M12 * gamma0 * gamma1) - (M21) - (M22) ) /( (M11 * gamma0) + (M12 * gamma0 * gamma1 ) + M21 + M22 ) ), 2 )
    
    return r


step = 0.011 #input("Please insert the Total number of STEPS, here -->>   ")
first = 800  #input("Please insert the number for First step, here -->>   ")
final = 2500  #input("Please insert the number of Final step, here -->>   ")

num = int( (final - first) / step )
lambda_values = []
for d in range(num+1):                # for all steps +1 !  
    
    Landa_val = first + ( step*(d) )
    
    lambda_values.append( Landa_val )



reflectance_values = []

for lambda_val in lambda_values:
    reflectance_values.append(R(lambda_val))


fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.17f'))
fig.set_figheight(5)
fig.set_figwidth(15)
plt.plot(lambda_values, reflectance_values)

plt.show()
