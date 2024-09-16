from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State

import copy
class Puzzle8(State):
    def __init__(self,posicao,operator):
        self.operator = operator
        # matriz 3x3
        self.posicao = posicao

    @staticmethod
    def posicao_vazio(matriz_3_3):
        for i in range(3):
            if 0 in matriz_3_3[i]:
                linha = i
        for j in range(3):
            if 0 == matriz_3_3[linha][j]:
                coluna = j
        return linha,coluna
    
    @staticmethod
    def is_solvable_puzzle(matriz_3_3):
        puzzle_array = []
        num_inversions = 0
        puzzle_array.append(matriz_3_3[0][0])
        puzzle_array.append(matriz_3_3[0][1])
        puzzle_array.append(matriz_3_3[0][2])
        puzzle_array.append(matriz_3_3[1][2])
        puzzle_array.append(matriz_3_3[2][2])
        puzzle_array.append(matriz_3_3[2][1])
        puzzle_array.append(matriz_3_3[2][0])
        puzzle_array.append(matriz_3_3[1][0])
        puzzle_array.append(matriz_3_3[1][1])
        if 0 not in puzzle_array:
            return False


        # Count inversions
        inversions = 0
        for i in range(len(puzzle_array)):
            for j in range(i+1, len(puzzle_array)):
                if puzzle_array[i] != 0 and puzzle_array[j] != 0 and puzzle_array[i] > puzzle_array[j]:
                    inversions += 1
        
        # Puzzle is solvable if inversion count is even
        return inversions % 2 == 0


    def show_path(self):
        algorithm = AEstrela()
        if not Puzzle8.is_solvable_puzzle(self.posicao):
            return 'Nao tem solucao' 
        result = algorithm.search(self, pruning='general')
        if result != None:
            return result.show_path()
        else:
            return 'Nao tem solucao' 


    def successors(self):
        sucessors = []
        linha_vazio, coluna_vazio = Puzzle8.posicao_vazio(self.posicao)
        
        # cima
        if linha_vazio == 0:
            pass
        else:
            mt_posicao = copy.deepcopy(self.posicao)
            mt_posicao[linha_vazio][coluna_vazio] = mt_posicao[linha_vazio-1][coluna_vazio]
            mt_posicao[linha_vazio-1][coluna_vazio] = 0
            sucessors.append(Puzzle8(mt_posicao,"cima"))
        
        # baixo 
        if linha_vazio == 2:
            pass
        else:
            mt_posicao = copy.deepcopy(self.posicao)
            mt_posicao[linha_vazio][coluna_vazio] = mt_posicao[linha_vazio+1][coluna_vazio]
            mt_posicao[linha_vazio+1][coluna_vazio] = 0
            sucessors.append(Puzzle8(mt_posicao,"baixo"))
        
        # esquerda
        if coluna_vazio == 0:
            pass
        else:
            mt_posicao = copy.deepcopy(self.posicao)
            mt_posicao[linha_vazio][coluna_vazio] = mt_posicao[linha_vazio][coluna_vazio-1]
            mt_posicao[linha_vazio][coluna_vazio-1] = 0
            sucessors.append(Puzzle8(mt_posicao,"esquerda"))
        # direita
        if coluna_vazio == 2:
            pass
        else:
            mt_posicao = copy.deepcopy(self.posicao)
            mt_posicao[linha_vazio][coluna_vazio] = mt_posicao[linha_vazio][coluna_vazio+1]
            mt_posicao[linha_vazio][coluna_vazio+1] = 0
            sucessors.append(Puzzle8(mt_posicao,"direita"))
        
        
        return sucessors
    
    def h(self):
        return self.h1()

    def h1(self):
        # soma da distancia de manhattan de cada numero
        linhas = {1:0,2:0,3:0,8:1,0:1,4:1,7:2,6:2,5:2}
        colunas = {1:0,8:0,7:0,2:1,0:1,6:1,3:2,4:2,5:2}
        diff = 0
        for linha in range(3):
            for coluna in range(3):
                num = self.posicao[linha][coluna]
                diff_linha = abs(linhas[num] - linha)
                diff_coluna = abs(colunas[num] - coluna)
                diff += diff_linha
                diff += diff_coluna
        return diff
    
    def h2(self):
        # quantidade de elementos fora do lugar
        goal = [[1,2,3],[8,0,4],[7,6,5]]
        diff = 0
        for linha in range(3):
            for coluna in range(3):
                if self.posicao[linha][coluna] != goal[linha][coluna]:
                    diff += 1
        return diff

    def is_goal(self):
        if self.posicao == [[1,2,3],[8,0,4],[7,6,5]]:
            return True
        else:
            return False
    
    def description(self):
        return "Descrição do problema: Robo tem a missão de limpar uma casinha com duas partes com a missão de antigir um estado final desejado. "
    
    def cost(self):
        return 1
        
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return str(self.posicao) + self.operator
        #return self.operator
