#
from main import Light


A = Light()


step = 0.011 #input("Please insert the Total number of STEPS, here -->>   ")
first = 800  #input("Please insert the number for First step, here -->>   ")
final = 2500  #input("Please insert the number of Final step, here -->>   ")

total = int( (final - first) / step )

lambda_values = []
reflectance_values = []

for i in range( first, final, step):
    
    