#
from main import Light

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import time

step = 11 #input("Please insert the number for each STEP, here -->>   ")
first = 1  #input("Please insert the number for First step, here -->>   ")
final = 2500  #input("Please insert the number of Final step, here -->>   ")

total = int( (final - first) / step )


Lambda_vals = []
R_baseLambda = []
T_baseLambda = []

lambda0 = 1600

for d in range( total + 1):
    
    Landa_val = first + ( step*(d) )
    
    Lambda_vals.append(Landa_val)
    
    ReflectanceRT = Light(landa0= lambda0, landa= Landa_val)
    
    R_Lambda, T_Lambda = ReflectanceRT.run(landa = Landa_val)
    
    R_baseLambda.append(R_Lambda)
    
    T_baseLambda.append(T_Lambda)



print("\n len(R_baseLambda) -->>  ", len(R_baseLambda))
print( "\n len(T_baseLambda)-->>  ", len(T_baseLambda))
time.sleep(2)
print("\n An Example of numbers inside R_baseLambda) -->>  ", (R_baseLambda[111]))
print("\n An Example of numbers inside T_baseLambda) -->>  ", (T_baseLambda[121]), "\n\n")
time.sleep(3)
print("\n\n Please wait,, while we are setting up the plot !\n\n")



plt.figure(figsize=(10, 5))
plt.plot( Lambda_vals, R_baseLambda)
plt.plot( Lambda_vals, T_baseLambda )
plt.xlabel('reflectBaseR')
plt.ylabel('Lambda_Vals')
plt.title('Plot R based on Lambda')
nameHelper = Light.nameHelper
plt.savefig(f'output/Fig_reflectBaseR_START{first}_ends{final}_id{nameHelper}.png')
plt.legend()
plt.show()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.5f'))
fig.set_figheight(5)
fig.set_figwidth(15)
plt.plot( Lambda_vals, R_baseLambda)
plt.plot( Lambda_vals, T_baseLambda  )
plt.xlabel('reflectBaseT')
plt.ylabel('Lambda_Vals')
plt.title('Plot T based on Lambda')
nameHelper = Light.nameHelper
plt.savefig(f'output/Fig_reflectBaseT_START{first}_ends{final}_id{nameHelper}.png')
plt.show()
