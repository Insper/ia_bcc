from aigyminsper.search.search_algorithms import BuscaCustoUniforme, AEstrela, BuscaGananciosa
from aigyminsper.search.graph import State
import json
import argparse
import time
import pandas as pd

heuristics = pd.read_csv('../data/MapHeuristics.csv', sep=',', header=0).to_dict(orient='records')

class MapLivro(State):

    def __init__(self, op, atual, objetivo, Mapa, custo):
        super().__init__(op)
        self.Mapa = Mapa
        self.atual = atual
        self.objetivo = objetivo
        self.custo = custo
    
    def successors(self):
        successors = []
        for custo, city in self.Mapa[self.atual]:
            successors.append(MapLivro(f'ir para {city}', city, self.objetivo, self.Mapa, custo))
        return successors
    
    def is_goal(self):
        return self.atual == self.objetivo
    
    def description(self):
        return "Problema do mapa de cidades do livro"
    
    def cost(self):
        return self.custo
    
    def env(self):
        return json.dumps(self.__dict__)
    
    def h(self):
        for item in heuristics:
            if item['atual'] == self.atual and item['destino'] == self.objetivo:
                return item['h']

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--origem", required=True)
    argparser.add_argument("--destino", required=True)
    argparser.add_argument("--algol", required=True)
    args = argparser.parse_args()

    Mapa = {
            'a':[(3,'b'),(6,'c')],
            'b':[(3,'a'),(3,'h'),(3,'k')],
            'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
            'd':[(3,'c'),(1,'f'),(1,'e')],
            'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
            'f':[(1,'g'),(1,'e'),(1,'d')],
            'g':[(2,'c'),(1,'f'),(2,'h')],
            'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
            'i':[(2,'e'),(2,'h')],
            'l':[(1,'k')],
            'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
            'm':[(2,'n'),(1,'x'),(14,'e')],
            'n':[(2,'m'),(3,'k')],
            'o':[(2,'c')],
            'p':[(2,'c')],
            'x':[(1,'m')]
        }

    if args.algol == 'BCU':
        algol = BuscaCustoUniforme()
    elif args.algol == 'A':
        algol = AEstrela()
    else:
        algol = BuscaGananciosa()

    state = MapLivro('', args.origem, args.destino, Mapa, 0)

    start = time.time()     
    result = algol.search(state)
    end = time.time()

    if result is None:
        print('Caminho não encontrado')
    else:
        print(f'Solução: {result.show_path()}')
        print(f'Custo: {result.g}')
        print(f'Tempo: {end-start} segundos')

#
# Exemplo de utilização: 
#
# python MapLivro.py --origem i --destino x --algol A
#
# possibilidade de algol: BCU, BG e A
#
#
    
