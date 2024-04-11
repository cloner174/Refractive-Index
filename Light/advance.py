#
#                   #       #                         In the name of God                     #      # #

#cloner174
#cloner174.org@gmail.com
##
import numpy as np
import matplotlib.pyplot as plt

class TwoLayerObject:
    
    def __init__(self, n0, nt, na, nb, landa0):
        self.n0 = n0  # Refractive index of air/initial medium
        self.nt = nt  # Refractive index of substrate
        self.na = na  # Refractive index of Layer A
        self.nb = nb  # Refractive index of Layer B
        self.landa0 = landa0  # Central wavelength
        self.c = 3e17  # Speed of light in nm/s
        self.La = landa0 / (4 * na)  # Length of Layer A
        self.Lb = landa0 / (4 * nb)  # Length of Layer B
    
    
    def calculate_M(self, landa):
        k0 = (2 * np.pi) / landa
        ka = k0 * self.na
        kb = k0 * self.nb
        # Matrix for layer A to B transition
        Mab = np.array([
            [0.5 * (1 + self.na / self.nb) * np.exp(-1j * ka * self.La), 0.5 * (1 - self.na / self.nb) * np.exp(1j * ka * self.La)],
            [0.5 * (1 - self.na / self.nb) * np.exp(-1j * ka * self.La), 0.5 * (1 + self.na / self.nb) * np.exp(1j * ka * self.La)]
        ])
        # Matrix for layer B to A transition
        Mba = np.array([
            [0.5 * (1 + self.nb / self.na) * np.exp(-1j * kb * self.Lb), 0.5 * (1 - self.nb / self.na) * np.exp(1j * kb * self.Lb)],
            [0.5 * (1 - self.nb / self.na) * np.exp(-1j * kb * self.Lb), 0.5 * (1 + self.nb / self.na) * np.exp(1j * kb * self.Lb)]
        ])
        # Combined matrix
        H1 = np.matmul(Mab, Mba)
        H2 = np.linalg.matrix_power(H1, 24)  # assuming 24 layers like in MATLAB code
        trans = 1 / H2[0, 0]
        ref = H2[1, 0] / H2[0, 0]
        return abs(ref)**2, abs(trans)**2
    
    
    def show_plot(self, first=1, final=1000, step=1.1):
        landa_vals = np.arange(first, final + step, step)
        R = []
        T = []
        for landa in landa_vals:
            r, t = self.calculate_M(landa)
            R.append(r)
            T.append(t)
        W = ((2 * np.pi * self.c) / landa_vals) / ((2 * np.pi * self.c) / self.landa0)
        plt.figure(figsize=(10, 5))
        plt.plot(W, T, label='Transmission')
        plt.plot(W, R, label='Reflection')
        plt.xlabel('Normalized Frequency (W)')
        plt.ylabel(' Coefficients (T) (R) ')
        plt.title('Reflection and Transmission Coefficients vs. Normalized Frequency')
        plt.legend()
        plt.show()

#end#