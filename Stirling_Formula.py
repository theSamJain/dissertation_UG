import numpy as np
from scipy.integrate import quad
import pandas as pd
from numba import njit
import mpmath as Mp
import timeit

@njit
def stirling(n):
    # works till order of result is < 10^300
    stir_res = np.sqrt(2*np.pi)*n**(n + 0.5)/(np.exp(1)**(n))
    return stir_res
    # can be sped-up using mpmath

def factorial(n):
    # works only till order of result is < 10**100 (<70!)
    gamma_np1 = lambda x: x**(n)*np.exp(-x)
    fact_res = quad(gamma_np1, 0, np.inf)[0]
    return fact_res

def factorial2(n):
    # works for arbitrary precision
    fact2_res = Mp.fac(n)
    return fact2_res

if __name__ == '__main__':
    Mp.mp.dps = 5
    n_arr = [i for i in range(1, 11)] + [j for j in range(20, 110, 10)]
    stir_arr = []
    fact_arr = []
    fact2_arr = []
    err_arr = []
    for n in n_arr:
        stir = stirling(n)
        # fact = factorial(n)
        fact = factorial2(n)
        err = 1-stir/fact
        stir_arr.append(stir)
        fact_arr.append(fact)
        err_arr.append(err)
    dict = {"n": n_arr, 
            "n! (mpmath)": fact_arr, 
            "n! (Stirling)": stir_arr, 
            "Rel. error": err_arr
            }
    df = pd.DataFrame(dict)
    pd.set_option("display.precision", 5)
    print()
    print(df)
    print()