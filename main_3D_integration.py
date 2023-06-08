import numpy as np
from Simpson_3D import simpson3D as simp3d
from Monte_Carlo import montecarlo3d as mc3d
import matplotlib.pyplot as plt

if __name__ =='__main__':
    func = lambda x, y, z: np.exp(x+y+z)
    a = 0; b = 1; 
    c = 0; d = 1; 
    e = 0; f = 1; 

    result_simp = []
    result_mc = []

    n = np.array([3, 9, 11, 19, 23, 25, 27, 29, 35, 41, 43, 45, 47, 51, 53, 69])
    for j in n:
        xx = np.linspace(a, b, j)
        yy = np.linspace(c, d, j)
        zz = np.linspace(e, f, j)
        result_simp.append(simp3d(xx, yy, zz, func))
        result_mc.append(mc3d(xx, yy, zz, func, j**3)) # Since 3D-simpson was also being sampled at n**3 points

    analytic = (np.exp(1)-1)**3
    analytical = np.full((len(n), 1), analytic)
    res_s = analytic - result_simp
    res_m = analytic - result_mc

    plt.plot(n**3, analytical, label = "Analytic Result", color = "black", zorder = -1)
    plt.plot(n**3, result_simp, marker = '.', label = "Error in Composite Simpson 3D")
    plt.plot(n**3, result_mc, marker = '.', label = "Error in Monte Carlo")    
    plt.xscale("log")
    plt.xlabel("Number of points at which function is sampled $(n^3)$")
    plt.ylabel("$f(x, y, z)$")
    # plt.title("Error Plot")
    plt.legend()
    plt.show()