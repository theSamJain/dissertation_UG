import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from numba import njit

@njit
def CLT(d, n_exp):
    res = [np.mean(np.random.randint(low = 1, high = 7, size = d)) for i in range(n_exp)]
    return res

dices = [30]#list(range(2, 11, 2)) + [15, 20, 25, 30] + list(range(40, 100, 10))

for k in dices:
    n_exp = 10**6
    result = CLT(k, n_exp)

    plt.figure(k)
    mean_res, stdev_res = np.mean(result), np.std(result) # here stdev_res = sigma_pop/root(k)
    nbin = int(5*(n_exp**(1/6))/(3.5*stdev_res)) # Scott's Method    
    values, bins_arr, _ = plt.hist(np.array(result), edgecolor = "black", color = "white", bins = nbin)

    x = [np.mean([bins_arr[i], bins_arr[i+1]]) for i in range(len(bins_arr)-1)] # Bin Centers

    print("\nnbin = ", nbin)
    
    mean_pop = np.mean(np.arange(1, 7, 1))
    g_stdev = np.std(np.arange(1, 7, 1))/np.sqrt(k) # = stdev_res
    scale = n_exp*(bins_arr[1]-bins_arr[0])/(g_stdev*np.sqrt(2*np.pi))
    gaussian =  scale*np.exp(-((x-mean_pop*np.ones(len(x)))/g_stdev)**2/2)

    gauss =  lambda x: scale*np.exp(-((x-mean_pop)/g_stdev)**2/2)
    hist_area = sum(np.diff(bins_arr)*values)

    print("Standard Dev: ", stdev_res, g_stdev)
    print("Mean: ", mean_res, mean_pop)
    print("Area of Gaussian: ", quad(gauss, a = 1, b = 6)[0])
    print("Area of Histogram: ", hist_area)

    plt.plot(x, gaussian)
    plt.ylabel("Occurences")
    plt.title("Throwing {:} dice ${:}^{:}$ times".format(k, 10, int(np.log10(n_exp))))
    plt.savefig(r'A:\Projects & Internships\Dissertation\Results\CLT Graphs\{:}.png'.format(k))

    # plt.show()