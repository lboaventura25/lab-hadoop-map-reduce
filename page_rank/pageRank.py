import numpy as np

# Função que calcula o PageRank
def calculoPageRank(grafo_web, fator_damping, num_paginas):
    # Calcula a matriz de transição M, considerando o fator de amortecimento e o número de páginas
    M = fator_damping * grafo_web + (1 - fator_damping) / num_paginas
    # Inicializa o vetor de pontuação de PageRank com valores iguais para todas as páginas
    page_rank =  100 * np.ones(num_paginas)/ num_paginas
    # Inicializa o vetor para acompanhar as pontuações de PageRank da iteração anterior
    ultimo_page_rank = page_rank
    page_rank = M @ page_rank

    # Itera até que a norma entre os vetores de PageRank atual e anterior seja menor que 0.9
    while(np.linalg.norm(ultimo_page_rank - page_rank) > 0.9):
        # Atualiza o vetor de PageRank anterior com o atual
        ultimo_page_rank = page_rank
        
        # Calcula um novo vetor de PageRank multiplicando M pelo vetor de PageRank atual
        page_rank = M @ page_rank

    # Retorna as pontuações de PageRank após a convergência
    return page_rank


# Função que mostra o PageRank
def showPageRank(page_rank, num_paginas):
   for i in range(num_paginas):
    print(f"Página {chr(65 + i)}: {page_rank[i]:.4f}")



if __name__ == '__main__':
    # Grafo da web, onde cada linha corresponde a uma página, e cada coluna indica um link de uma página para outra
    # Exemplo:  
    grafo_web = np.array([
    [1. , 1. , 0.5, 0.2, 0.5],
    [0. , 0. , 0. , 0.2, 0. ],
    [0. , 0. , 0.5, 0.2, 0. ],
    [0. , 0. , 0. , 0.2, 0. ],
    [0. , 0. , 0. , 0.2, 0.5]
     ], dtype=float)

    # Fator Damping: O fator de amortecimento representa a probabilidade de o usuário aleatório seguir um link em vez de pular para uma página aleatória. 
    fator_damping = 0.85

    num_paginas = grafo_web.shape[0]
    page_rank = np.ones(num_paginas) / num_paginas

    # Número de iterações
    page_rank = calculoPageRank(grafo_web, fator_damping, num_paginas)
    showPageRank(page_rank, num_paginas)

