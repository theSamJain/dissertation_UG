import numpy as np
import Simpson_2D as simp2D
import Monte_Carlo as mc
import matplotlib.pyplot as plt

if __name__ =='__main__':

    func = lambda x, y: np.exp(x+y)
    a = 0; b = 1; 
    c = 0; d = 1; 
    result_simp = []
    result_mc = []

    n = np.array([3**i for i in range(2, 8)])
    for j in n:
        xx = np.linspace(a, b, j)
        yy = np.linspace(c, d, j)
        result_simp.append(simp2D.simpson2D(xx, yy, func))
        result_mc.append(mc.montecarlo(xx, yy, func, j**2)) # Since 2D-simpson was also being sampled at n**2 points

    analytic = (np.exp(1)-1)**2
    analytical = np.full((len(n), 1), analytic)
    res_s = analytic - result_simp
    res_m = analytic - result_mc

    # plt.plot(n**2, np.full((len(n), 1), analytic), label = "Analytic Result", color = "black", zorder = -1)
    plt.scatter(n**2, res_s, label = "Error in Composite Simpson 2D")
    plt.scatter(n**2, res_m, label = "Error in Monte Carlo")    
    plt.xscale("log")
    plt.xlabel("Number of points at which function is sampled $(n^2)$")
    plt.ylabel("$f(x, y)$")
    plt.title("Error Plot")
    plt.legend()
    plt.show()