# PSPD

| Aluno | Matrícula |
| :-- | :--: |
| Lucas Gabriel Bezerra | 180125770 |
| Lucas Ursulino Boaventura | 180114093 |

## LAB. Map Reduce

Nesse laboratório foi colocado em prática os aprendizados sobre o uso do padigma Map Reduce no framework do Hadoop.

## Atividade 1

Para esse exercício, era necessário a listagem de notas para filmes de cada usuário seguindo o arquivo **movies_rating/movies.txt**.

- Na primeira etapa foi feito o código **movies_rating/normal.py** sem o uso do map reduce, com o código rodando através do comando:

```sh
 python normal.py
```

- Na segunda etapa foi feito o código **movies_rating/mapper.py** e **movies_rating/reducer.py**, com o código rodando através do comando:

```sh
# cat movies.txt | python3 mapper.py | sort -k 1,1 | python3 reducer.py
cd movies_rating/ && sh run_map_reduce.sh
```

As mudanças feitas no código, foi primeiro, a quebra da etapa de mapeamento (_mapper.py_) dos dados advindos do input do processo (_movies.txt_). E também a criação da etapa de consolidação dos dados ordenados (_reducer.py_) que foram output do processo de mapeamento.

E para respeitar esse processo foi feito a leitura através do stream de input dos processos com o auxílio do seguinte código:

```python3
"""mapper.py"""
mapper_input = sys.stdin.readlines()

# Despreza a primeira linha de cabeçalho do arquivo
for linha in mapper_input[1::]:
    linha = linha.strip()
    ...

    # Ao final o conteúdo de output do map é a seguinte string montada
    # > "6783 \t 76 \t 4 \t 7833427\n"
    print(f'{self.user_id}\t{self.movie_id}\t{self.rating}\t{self.ts}')
```

O resultado do comando utilizando o script é o seguinte:

```sh
# É necessário ajustar o caminho para os arquivos e o .jar

./hadoop-3.3.6/bin/hadoop jar hadoop-streaming-3.3.6.jar -input /user/lucas/movies.txt -output /user/lucas/output-la.txt -mapper ../LABS/MOVIES/mapper.py -reducer ../LABS/MOVIES/reducer.py
```
![Imagem](./assets/ex1-resultado_map_reduce_local.png)

- Na terceira etapa, foi colocado o código a prova com o auxílio do framework do hadoop, conforme o comando e o print:

![](./assets/ex1-resultado-hadoop.png)

## Atividade 2