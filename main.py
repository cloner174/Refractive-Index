#cloner174
#cloner174.org@gmail.com
##
from math import *


# γ -->>  Gamma
# ε -->>  Epsilon
# θ -->>  Theta
# λ -->>  Lambda
# μ -->>  Mu

class Light:
    
    def __init__(self, Lambda_0: float):
        
        self.Lambda_0: Lambda_0
        self.n_1 = 2.5
        self.Theta_1 = 0
        self.Epsilon_0 = (8.85)*((10)**(-12))
        self.Mu = ( 4 )*( pi )*( ( 10 )**( -7 ) ) 
    
    
    def k(self):
        
        face_ = 2 * pi
        _down = self.Lambda_0
        
        return face_/_down
    
    def 
    
    def h(self):
        
        h_firstCoef = self.n_1
        h_secondCoef = 