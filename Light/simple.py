#                   #       #                         In the name of God                     #      # #
#
#cloner174
#cloner174.org@gmail.com
#
#Assuming Just One Layer is involved! -> we call it layer A
# γ -->>  Gamma
# ε -->>  Epsilon
# θ -->>  Theta
# λ -->>  Lambda
# μ -->>  Mu
#
import numpy as np
import matplotlib.pyplot as plt


class OneLayerObject :
    
    def __init__(self, teta_i = 30 , landa0 = 1500, n1 = 2.5) :
        self.teta_i = teta_i
        self.landa0 = landa0
        self.n1 = n1             # # Refractive index of Layer A
        self.L1 = landa0 / (4 * n1)  # Length of Layer A
        self.epsilon0 = (8.85)*((10)**(-12))
        self.Mu0 = ( 4 )*( np.pi )*( ( 10 )**( -7 ) )
    
    
    def _h(self) :
        self.h = self.n1 * self.L1 * np.cos(self.teta_i)
    
    def _gamma0(self) :
        self.gamma0 = np.square( (self.epsilon0 / self.Mu0) )
    
    def _gamma1(self) :
        self.gamma1 = self.gamma0 * self.n1 * np.cos(self.teta_i)
    
    def _M(self, landa) :
        k0 = 2*np.pi / landa
        self.M = np.array( [[ np.cos(k0 * self.h), - np.sin(k0 * self.h)],
                            [np.sin(k0 * self.h),np.cos(k0 * self.h)]])
    
    def _r(self) :
        
        _head = ( self.M[0,0] * self.gamma0 ) + ( self.M[0, 1] * self.gamma0 * self.gamma1 ) - ( self.M[1, 0] )  - ( self.M[1, 1] * self.gamma1 )
        tail_ = ( self.M[0,0] * self.gamma0 ) + ( self.M[0, 1] * self.gamma0 * self.gamma1 ) + ( self.M[1, 0] )  + ( self.M[1, 1] * self.gamma1 )
        
        self.r = _head / tail_
    
    def _t(self) :
        _head = 2 * self.gamma0
        tail_ = ( self.M[0,0] * self.gamma0 ) + ( self.M[0,1] * self.gamma0 * self.gamma1 ) + ( self.M[1, 0] )  + ( self.M[1, 1] * self.gamma1 )
        
        self.t = _head / tail_
    
    def show_plot(self, 
                  first : int = 1, 
                  final : int = 1000, 
                  step : float = 0.5 ,
                  figure_size : tuple = (20, 15),
                  show_Transmission : bool = False, 
                  show_Reflection : bool = True):
        
        self._h()
        self._gamma0()
        self._gamma1()      
        landa_vals = np.arange(first, final + step, step)
        R = []
        T = []
        for landa in landa_vals:
            self._M(landa = landa)
            self._r()
            self._t()
            r = abs(self.r) 
            t = abs(self.t)
            r = r**2
            t = t**2  
            R.append(r)
            T.append(t)
        
        if show_Transmission :
            
            plt.figure( figsize = figure_size )
            plt.plot(landa_vals, T, label='Transmission')
            plt.xlabel(' Landa Values Range ')
            plt.ylabel(' Coefficient (T) ')
            plt.title(' Transmission Coefficient vs. Frequency')
            plt.legend()
            plt.show()
            return
        
        elif show_Reflection :
            
            plt.figure( figsize = figure_size )
            plt.plot(landa_vals, R, label='Reflection')
            plt.xlabel(' Landa Values Range ')
            plt.ylabel(' Coefficient (R) ')
            plt.title(' Reflection Coefficient vs. Frequency')
            plt.legend()
            plt.show()
            return
        
        elif show_Transmission and show_Reflection :
            
            plt.figure( figsize = figure_size )
            plt.plot(landa_vals, T, label='Transmission')
            plt.plot(landa_vals, R, label='Reflection')
            plt.xlabel(' Landa Values Range ')
            plt.ylabel(' Coefficients (T) (R) ')
            plt.title('Reflection and Transmission Coefficients vs. Normalized Frequency')
            plt.legend()
            plt.show()
            return
        
        elif show_Transmission == False and show_Reflection == False:
            print(" What should I Do now ? ")
            self.R = R
            self.T = T
            print( " You can Use <name of class>.R or <name of class>.T to get access to their values !")
            return

#end#