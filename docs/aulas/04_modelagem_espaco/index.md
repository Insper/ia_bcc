# Modelagem e espaço de busca

Na aula passada implementamos alguns aspiradores de pó com configurações diferentes: 

* [Aspirador de pó com 2 quartos](./src/robo_aspirador.py)
* [Aspirador de pó com 4 quartos](./src/robo_aspirador_quadrado.py)
* [Aspirador de pó com 4 quartos e sofás](./src/robo_aspirador_quadrado_poltrona.py)

Muitos de vocês conseguiram verificar que dependendo da configuração do ambiente o aspirador demorava mais ou menos tempo para limpar o ambiente considerando cenários similares, ou seja, todos os quartos sujos: 

```bash
(venv) ➜  disciplina_ai python robo_aspirador.py 
Busca em largura
Tempo de execucao: 0.0002803802490234375 segundos
Achou!
 ; ir p/ direita ; limpar ; ir p/ esquerda ; limpar
(venv) ➜  disciplina_ai python robo_aspirador_quadrado.py 
Busca em largura
Tempo de execucao: 0.008468866348266602 segundos
Achou!
 ; limpar ; ir p/ direita ; limpar ; ir p/ baixo ; limpar ; ir p/ esquerda ; limpar
(venv) ➜  disciplina_ai python robo_aspirador_quadrado_poltrona.py 
Busca em largura
Tempo de execucao: 0.2716667652130127 segundos
Achou!
 ; limpar ; ir p/ direita ; virar poltrona ; limpar ; ir p/ baixo ; virar poltrona ; limpar ; ir p/ esquerda ; limpar
```

## Qual é a explicação para isto acontecer? 