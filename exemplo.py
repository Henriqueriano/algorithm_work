import time
import matplotlib.pyplot as plt

def f(n):
    if n < 0:
        return 1
    return f(n-1) + 2 * n  - 1


if __name__ == "__main__":
    # Gera a lista de números
    n_lista = [x for x in range(0,996)]
    
    tempos_n_1, tempos_n_2 = [], []
    for n in n_lista:
        start_n_1 = time.time()
        n_1 = f(n)
        end_n_1  = time.time()
        tempos_n_1.append(end_n_1 - start_n_1)


# 
plt.plot(n_lista, tempos_n_1, label="Função SEM desenrolamento")

plt.ylabel("Tempo de execução")
plt.xlabel("Valores de n")
plt.legend()

plt.show()