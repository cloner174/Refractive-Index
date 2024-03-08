#
#                   #       #                         In the name of God                     #      # #

#cloner174
#cloner174.org@gmail.com
##


#Assuming Just One Layer is involved! -> we call it layer A
# γ -->>  Gamma
# ε -->>  Epsilon
# θ -->>  Theta
# λ -->>  Lambda
# μ -->>  Mu


from math import *
import numpy as np



class Light:
    
    def __init__(self, landa0: float, landa: float, i_: int = None):
        
        self.landa0 = landa0
        self.landa = landa
        self.n1 = 2.5
        self.TeTa_i = 0
        self.Epsilon0 = (8.85)*((10)**(-12))
        self.Mu = ( 4 )*( pi )*( ( 10 )**( -7 ) )
        
        if i_:
            self.i = i_
        else:
            self.i = 1
    
    
    def L(self):
        
        head_ = self.landa0
        _tail = ( 4 )*( self.n1 )
        
        return head_ / _tail
    
    
    def k(self):
        
        face_ = 2 * pi
        _down = self.landa
        
        return face_/_down
    
    
    def h(self):
        
        h_firstCoef = self.n1
        h_secondCoef = self.L()
        h_thirdCoef = cos( self.TeTa_i )
        
        return ( ( h_firstCoef )*( h_secondCoef )*( h_thirdCoef ) ) 
    
    
    def gama0( self ):
        
        head_ = self.Epsilon0
        _tail = self.Mu
        
        return sqrt( ( ( head_ )/( _tail ) ) )
    
    
    def gamma1(self):
        
        gamma1_firstCoef = self.gama0()
        gamma1_secondCoef = self.n1
        gamma1_thirdCoef = cos( self.TeTa_i )
        
        return ( ( gamma1_firstCoef )*(gamma1_secondCoef)*(gamma1_thirdCoef) )
    
    
    
    def M(self):
        
        m11 = cos( (self.k())*(self.h()) )
        m12 = ( (self.i)*( sin( (self.k())*(self.h())) ) )/( self.gamma1() )
        m21 = (self.i)*(self.gamma1())*( sin((self.k())*(self.h())) )
        m22 = cos( (self.k())*(self.h()) )
        
        TransPose_Matrix = [
            [m11, m12],
            [m21, m22]
        ]
        
        
        return np.matrix(TransPose_Matrix)
    
    
    def r(self):
        
        m = self.M()
        
        head_1 = m[0,0] * self.gama0()
        head_2 = m[0,1] * self.gama0() * self.gamma1()
        head_3 = - ( m[1,0] )
        head_4 = - ( m[1,1] * self.gamma1() )
        
        _tail1 = m[0,0] * self.gama0()
        _tail2 = m[0,1] * self.gama0() * self.gamma1()
        _tail3 = m[1,0]
        _tail4 =  m[1,1] * self.gamma1()
        
        head_ = head_1 + head_2 + head_3 + head_4
        _tail = _tail1 + _tail2 + _tail3 + _tail4
        
        return (head_ / _tail)
    
    
    def t(self):
        
        m = self.M()
        
        head_ = 2 * self.gama0()
        
        _tail1 = m[0,0] * self.gama0()
        _tail2 = m[0,1] * self.gama0() * self.gamma1()
        _tail3 = m[1,0]
        _tail4 =  m[1,1] * self.gamma1()     
        
        _tail = _tail1 + _tail2 + _tail3 + _tail4
        
        return (head_ / _tail)
    
    
    nameHelper = np.random.randint(1000)
    
    def run(self, return_tuple_shape: bool = False):
        
        R = self.r()
        T = self.t()
            
        R_abseloutValuePowerUp_2 = (abs( R ))**(2)
        T_abseloutValuePowerUp_2 = (abs( T ))**(2)
        
        if return_tuple_shape == True:
            
            R_of_Landa = ( self.landa, R_abseloutValuePowerUp_2 )
            T_of_Landa = ( self.landa, T_abseloutValuePowerUp_2)
            
            return R_of_Landa, T_of_Landa
        
        else:
            
            return R_abseloutValuePowerUp_2, T_abseloutValuePowerUp_2
        
        
    
#End-!-
