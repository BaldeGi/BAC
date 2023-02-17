import random
import time
  
import matplotlib.pyplot as plt
import numpy as np


def paire_max(a): #Approche par force brute
    """
    Calcule la somme maximale d'une paire d'entiers de `a`
    pre: `a` est un tableau (list) d'entiers
    pre: len(`a`) >= 2
    post: retourne la somme maximale obtenue Ã  partir d'une
        paire d'entiers de `a`
    """
    somme_maximale=-1000000000000000
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            somme_courante = a[i] + a[j]
            if somme_courante > somme_maximale:
                somme_maximale = somme_courante
    return somme_maximale



def paire_max_efficace(a):
    """
    Calcule la somme maximale d'une paire d'entiers de `a`
    pre: `a` est un tableau (list) d'entiers
    pre: len(`a`) >= 2
    post: retourne la somme maximale obtenue Ã  partir d'une
        paire d'entiers de `a`
    """
    l=list(a)
    current_max = max(a)
    l[l.index(current_max)]=min(l)
    val=l[0]
    for i in range(len(l)):
        if l[i] > val:
            val = l[i]
    return val + current_max
    


def generate_instance(size, lower_bound, upper_bound, sort=False):
    """
    pre: size >= 0
    post: returns a list of randomly chosen unique integers within [lb, ub)
    :param size : positive integer
    :param lower_bound: positive integer
    :param upper_bound: positive integer
    :param sort : boolean specifying whether tab should be sorted
    """
    try:
        liste = random.sample(range(lower_bound,upper_bound),size)
        return liste
    
    except ValueError:
         print('Sample size exceeded population size.')
         
         
def bench_search(sizes=(50,100, 200,500,1000), num_inst=10, num_keys=10):
    paire_max_time = {s: [] for s in sizes}
    paire_max_efficace_time = {s: [] for s in sizes}
    random.seed(42)  # Fix random seed for reproducible results
    # Loop over instance sizes
    for s in sizes:
        # Loop over various instances of the same size
        for i in range(num_inst):
            # Generate an instance of size s including unique integers in [0, 2s)
            tab = generate_instance(s, 0, 2*s, sort=False)
            # Timing for paire_max
            start = time.process_time()
            pos1 = paire_max(tab)
            stop = time.process_time()
            paire_max_time[s].append((stop-start) * 1000)

            # Timing for paire_max_efficace
            start = time.process_time()
            pos2 = paire_max_efficace(tab)
            stop = time.process_time()
            paire_max_efficace_time[s].append((stop-start) * 1000)

            # Check that both searches give the same result
            assert pos1 == pos2
    return paire_max_efficace_time, paire_max_time 
        


sizes=(500,1000, 2000,5000,10000)
p_max_e,p_max = bench_search(sizes)
# Compute median values, first and third quartiles
medians_paire_max_efficace = [np.percentile(p_max_e[s], 50) for s in sizes]
medians_paire_max = [np.percentile(p_max[s], 50) for s in sizes]
q1_p_max_e = [np.percentile(p_max_e[s], 25) for s in sizes]
q3_p_max_e= [np.percentile(p_max_e[s], 75) for s in sizes]
q1_p_max = [np.percentile(p_max[s], 25) for s in sizes]
q3_p_max = [np.percentile(p_max[s], 75) for s in sizes]


plt.figure(figsize=(10, 6))
plt.plot(sizes, medians_paire_max_efficace, 'bo-', label="Paire Max Efficace")
plt.plot(sizes, medians_paire_max, 'ro-', label="Paire Max")
plt.xticks(sizes)
plt.legend(loc=2)
plt.xlabel("Taille des instances")
plt.ylabel("Temps CPU en msec")
# add error bars
plt.errorbar(sizes, medians_paire_max_efficace, yerr=[q1_p_max_e, q3_p_max_e], ecolor='b', fmt='none', capsize=5)
plt.errorbar(sizes, medians_paire_max, yerr=[q1_p_max, q3_p_max], ecolor='r', fmt='none', capsize=5)
plt.show()











