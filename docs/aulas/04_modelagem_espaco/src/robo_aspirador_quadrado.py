from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import json
import copy
import time

class RoboAspiradorQuadrado(State):

    def __init__(self, op, posicao_robo, situacao):
        # You must use this name for the operator!
        self.operator = op
        self.posicao_robo = posicao_robo
        self.situacao = situacao

    def successors(self):
        successors = []
        # ir p/ esquerda
        if self.posicao_robo[1] > 0:
            new_posicao_robo = [self.posicao_robo[0], self.posicao_robo[1]-1]
            successors.append(RoboAspiradorQuadrado('ir p/ esquerda', new_posicao_robo, self.situacao))
        # ir p/ direita
        if self.posicao_robo[1] < 1:
            new_posicao_robo = [self.posicao_robo[0], self.posicao_robo[1]+1]
            successors.append(RoboAspiradorQuadrado('ir p/ direita', new_posicao_robo, self.situacao))
        # ir p/ cima
        if self.posicao_robo[0] > 0:
            new_posicao_robo = [self.posicao_robo[0]-1, self.posicao_robo[1]]
            successors.append(RoboAspiradorQuadrado('ir p/ cima', new_posicao_robo, self.situacao))
        # ir p/ baixo
        if self.posicao_robo[0] < 1:
            new_posicao_robo = [self.posicao_robo[0]+1, self.posicao_robo[1]]
            successors.append(RoboAspiradorQuadrado('ir p/ baixo', new_posicao_robo, self.situacao))
        # limpar
        if self.situacao[self.posicao_robo[0]][self.posicao_robo[1]] == 0:
            new_situacao = copy.deepcopy(self.situacao)
            new_situacao[self.posicao_robo[0]][self.posicao_robo[1]] = 1
            successors.append(RoboAspiradorQuadrado('limpar', self.posicao_robo, new_situacao))

        return successors

    def is_goal(self):
        return self.situacao == [[1,1],[1,1]]

    def description(self):
        return "Robô aspirador de pó em uma matriz 2x2"
    
    def cost(self):
        return 1
    
    def env(self):
        return json.dumps(self.__dict__)
    
def main():
    print('Busca em largura')
    state = RoboAspiradorQuadrado('',[0,0],[[0,0],[0,0]])
    algorithm = BuscaLargura()
    start = time.time()
    result = algorithm.search(state)
    print(f'Tempo de execucao: {time.time() - start} segundos')
    #algorithm = BuscaProfundidade()
    #result = algorithm.search(state, m=5, trace=True)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()