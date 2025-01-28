from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import json
import time

class RoboAspirador(State):

    def __init__(self, op, posicao_robo, situacao_esq, situacao_dir):
        super().__init__(op)
        self.posicao_robo = posicao_robo
        self.situacao_esq = situacao_esq
        self.situacao_dir = situacao_dir
            
    def successors(self):
        successors = []
        # ir p/ esquerda
        successors.append(RoboAspirador('ir p/ esquerda','ESQ',self.situacao_esq,self.situacao_dir))
        # ir p/ direita
        successors.append(RoboAspirador('ir p/ direita','DIR',self.situacao_esq,self.situacao_dir))
        # limpar
        if self.posicao_robo == 'ESQ':
            successors.append(RoboAspirador('limpar',self.posicao_robo,'LIMPO',self.situacao_dir))
        else:
            successors.append(RoboAspirador('limpar',self.posicao_robo,self.situacao_esq,'LIMPO'))       
        return successors
    
    def is_goal(self):
        return self.situacao_esq == 'LIMPO' and self.situacao_dir == 'LIMPO' and self.posicao_robo == 'ESQ'
    
    def description(self):
        return "Robo simples limpador de chao"
    
    def cost(self):
        return 1
    
    def env(self):
        return json.dumps(self.__dict__)

def main():
    print('Busca em largura')
    state = RoboAspirador('','ESQ','SUJO','SUJO')
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