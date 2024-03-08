#
from main import Light

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter



step = 0.011 #input("Please insert the number for each STEP, here -->>   ")
first = 800  #input("Please insert the number for First step, here -->>   ")
final = 2500  #input("Please insert the number of Final step, here -->>   ")

total = int( (final - first) / step )

lambda_values = []
reflectance_values = []
reflectance_valuesR = []
reflectance_valuesT = []

lambda0 = 1600

for d in range( total + 1):
    
    Landa_val = first + ( step*(d) )
    
    ReflectanceRT = Light(landa0= lambda0, landa= Landa_val)
    
    ReflectanceR, ReflectanceT = ReflectanceRT.run()
    
    lambda_values.append(Landa_val)
    
    reflectance_valuesR.append(ReflectanceR)
    reflectance_valuesT.append(ReflectanceT)
    

print(len(reflectance_valuesR))
print(len(reflectance_valuesT))
print(len(lambda_values))

#lambda_values.pop()

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.17f'))
fig.set_figheight(5)
fig.set_figwidth(15)
plt.plot(lambda_values, reflectance_valuesR)
plt.show()

fig, ax = plt.subplots()
plt.plot(lambda_values, reflectance_valuesT)
plt.show()
