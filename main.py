import sys
import time
import random
import matplotlib.pyplot as plt

# function without "desarolamento"
def f(n):
    '''
        This recursive function alows us to see the basic usage of recursion.
    '''
    if n == 1:
        return 0
    return f(n-1) + 2 * n  - 1

# function "desarolada"
def _f(n):
    '''
        This function allows us to see the O(n²) notation behavior. 
    '''
    return n * n

if __name__ == "__main__":
    max_recursion = sys.getrecursionlimit() - 4  # python sucks, the minus four is the language limitation
    print(f'Max number of recursion stack: {max_recursion}')
    # number gen
    n_lista = [random.randint(1, max_recursion) for x in range(0,1000)] 
    tempos_n_1, tempos_n_2 = [], []
    
    # processing and populating graphic data
    for n in n_lista:
        start_n_1 = time.time()
        n_1 = f(n)
        end_n_1  = time.time()
        tempos_n_1.append(end_n_1 - start_n_1)

        start_n_2 = time.time()
        n_2 = _f(n)
        end_n_2  = time.time()
        tempos_n_2.append(end_n_2 - start_n_2)

    # generating table data (to copy to clipboard), can I use the tabulate here maybe.
    with open('tabular','w') as t:
        t.write('Table content of f(n-1) + 2 * n  - 1:\n')
        for i in range(len(n_lista)):
            t.write(f'{tempos_n_1[i]:.10f}, {n_lista[i]}\n')

        t.write('\n')
        t.write('Table content of n²:\n')
        for i in range(len(n_lista)):
            t.write(f'{tempos_n_2[i]:.10f}, {n_lista[i]}\n')
    print('Table file generated!')

# generating graphics in row setup.
plt.subplot(2,1,1) # rows, cols, index (position).
plt.plot(n_lista, tempos_n_1, 'r', label="Função SEM desenrolamento")
plt.ylabel("Tempo de execução")
plt.xlabel("Valores de n")
plt.legend()

plt.subplot(2,1,2) 
plt.plot(n_lista, tempos_n_1, 'g', label="Função COM desenrolamento")
plt.ylabel("Tempo de execução")
plt.xlabel("Valores de n")
plt.legend()

plt.savefig('graphic.png')
# end ༼つಠ益ಠ༽つ ─=≡ΣO))
