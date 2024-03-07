#
from main import Light


step = 0.011 #input("Please insert the Total number of STEPS, here -->>   ")
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
    
    ReflectanceR, ReflectanceT = ReflectanceRT.main()
    
    lambda_values.append(Landa_val)
    
    reflectance_valuesR.append(ReflectanceR[1])
    reflectance_valuesT.append(ReflectanceT[1])
    
    
    
    