from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import json
import copy
import time

class Quarto:

    def __init__(self, situacao, poltrona, situacao_poltrona):
        self.situacao = situacao    
        self.poltrona = poltrona
        self.estado_poltrona = situacao_poltrona

    def estah_sujo(self):
        return self.situacao == 'SUJO'
    
    def limpar(self):
        self.situacao = 'LIMPO'

    def tem_poltrona(self):
        return self.poltrona
    
    def situacao_poltrona(self):
        return self.estado_poltrona
    
    def virar_poltrona(self):
        self.estado_poltrona = 'VIRADA'

    def desvirar_poltrona(self):
        self.estado_poltrona = 'NORMAL'


class RoboAspiradorQuadrado(State):

    def __init__(self, op, posicao_robo, quartos):
        # You must use this name for the operator!
        self.operator = op
        self.posicao_robo = posicao_robo
        self.quartos = quartos

    def successors(self):
        successors = []
        # ir p/ esquerda
        if self.posicao_robo[1] > 0:
            new_posicao_robo = [self.posicao_robo[0], self.posicao_robo[1]-1]
            successors.append(RoboAspiradorQuadrado('ir p/ esquerda', new_posicao_robo, self.quartos))
        # ir p/ direita
        if self.posicao_robo[1] < 1:
            new_posicao_robo = [self.posicao_robo[0], self.posicao_robo[1]+1]
            successors.append(RoboAspiradorQuadrado('ir p/ direita', new_posicao_robo, self.quartos))
        # ir p/ cima
        if self.posicao_robo[0] > 0:
            new_posicao_robo = [self.posicao_robo[0]-1, self.posicao_robo[1]]
            successors.append(RoboAspiradorQuadrado('ir p/ cima', new_posicao_robo, self.quartos))
        # ir p/ baixo
        if self.posicao_robo[0] < 1:
            new_posicao_robo = [self.posicao_robo[0]+1, self.posicao_robo[1]]
            successors.append(RoboAspiradorQuadrado('ir p/ baixo', new_posicao_robo, self.quartos))
        
        # limpar
        if self.quartos[self.posicao_robo[0]][self.posicao_robo[1]].estah_sujo():

            if not self.quartos[self.posicao_robo[0]][self.posicao_robo[1]].tem_poltrona():
                new_quartos = copy.deepcopy(self.quartos)
                new_quartos[self.posicao_robo[0]][self.posicao_robo[1]].limpar()
                successors.append(RoboAspiradorQuadrado('limpar', self.posicao_robo, new_quartos))
            elif self.quartos[self.posicao_robo[0]][self.posicao_robo[1]].situacao_poltrona() == 'VIRADA':
                new_quartos = copy.deepcopy(self.quartos)
                new_quartos[self.posicao_robo[0]][self.posicao_robo[1]].limpar()
                successors.append(RoboAspiradorQuadrado('limpar', self.posicao_robo, new_quartos))
            elif self.quartos[self.posicao_robo[0]][self.posicao_robo[1]].situacao_poltrona() == 'NORMAL':
                new_quartos = copy.deepcopy(self.quartos)
                new_quartos[self.posicao_robo[0]][self.posicao_robo[1]].virar_poltrona()
                successors.append(RoboAspiradorQuadrado('virar poltrona', self.posicao_robo, new_quartos))

        return successors

    def is_goal(self):
        for lista in self.quartos:
            for quarto in lista:
                if quarto.estah_sujo():
                    return False
        return True

    def description(self):
        return "Robô aspirador de pó em uma matriz 2x2 com poltronas"
    
    def cost(self):
        return 1
    
    def env(self):
        return json.dumps(self.__dict__)
    
def main():
    print('Busca em largura')
    
    state = RoboAspiradorQuadrado(
        op='',
        posicao_robo=[0,0],
        quartos=[[Quarto('SUJO',False,None),Quarto('SUJO',True,'NORMAL')],[Quarto('SUJO',True,'VIRADA'),Quarto('SUJO',True,'NORMAL')]]
    )
    
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