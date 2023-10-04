# Contribuindo com o projeto AIGYMINSPER

Considere a [lista de issues](https://github.com/Insper/ai_gym/issues) do projeto.
Nesta lista de issues existem alguns itens específicos sobre testes que podem ser feitos para melhorar o projeto.

O título dos issues segue o seguinte padrão: 

```
Implementar os testes em test_poda_<algoritmo>.py
```

Onde `<algoritmo>` pode ser `Gananciosa`, `BPI`, `BP`, `BCU` ou `AEstrela`.

O objetivo destes testes é criar um conjunto de rotinas, usando `pytest`, que testam o funcionamento dos algoritmos implementados. Considerando todas as situações possíveis: sem poda alguma, com poda de estados filhos 
iguais aos pais e de estados repetidos como um todo. 

No diretório `tests` existem alguns arquivos de testes que deverão ser utilizados para a implementação dos testes.
O arquivo `tests/test_poda_BCU.py` já possui um teste implementado.

```python
#
# Considerando as implementações: 
#
# - AspiradorPo.py
# - SumOne.py
# - poi.py
#
# Testar o algoritmo: 
#
# 4) Uniform cost search (CustoUniforme)
#
# Com as seguintes configurações de poda: 
#
# - without pruning
# - father-son pruning
# - general pruning
#
#

from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from SumOne import SumOne

def test_sumone_without_pruning():
    state = SumOne(1, '', 11)
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    print(f'\nEstado inicial = {state.env()}')
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; +2  ; +2  ; +2  ; +2  ; +2 "
```

O código acima testa o algoritmo de busca `BuscaCustoUniforme` para o problema `SumOne` sem poda alguma. Você pode utilizar este padrão para implementar os testes para os outros algoritmos e problemas.

Neste exercício você deve realizar as seguintes atividades: 

1. Fazer o fork do projeto [AI Gym Insper](https://github.com/Insper/ai_gym);
1. Atualizar o seu repositório local do projeto AI Gym Insper;
1. Escolher uma das issues de teste para implementar;
1. Criar um branch local para implementar a issue escolhida;
1. Implementar os testes;
1. Fazer o commit das alterações;
1. Fazer o push do branch para o seu repositório remoto;
1. Criar um pull request para o projeto AI Gym Insper. Ao fazer o pull request para o projeto deixe claro no título e na descrição do pull request qual issue você está implementando.

Você deverá implementar diversos testes em um mesmo arquivo. Cada arquivo de teste deve considerar apenas um algoritmo de busca. Mas deve considerar os 3 problemas listados acima (`AspiradorPo`, `SumOne` e `Poi`). 

O objetivo é fazer esta atividade em sala de aula no dia **09/10/2023**. 