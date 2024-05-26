from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa, BuscaLargura
from aigyminsper.search.Graph import State

class MyAgent(State):

    def __init__(self, map, op, position, goal):
        self.map = map
        self.operator = op
        self.position = position
        self.goal = goal

    def successors(self):
        #
        # os sucessores que devem ser considerados são: 
        # 0 - cima
        # 1 - baixo
        # 2 - esquerda
        # 3 - direita
        #
        sucessors = []
        if self.position[0] > 0 and self.map[self.position[0]-1][self.position[1]] == '0':
            sucessors.append(MyAgent(self.map, '0', (self.position[0]-1, self.position[1]), self.goal))
        else:
            sucessors.append(MyAgent(self.map, '0', self.position, self.goal))

        if self.position[0] < len(self.map)-1 and self.map[self.position[0]+1][self.position[1]] == '0':
            sucessors.append(MyAgent(self.map, '1', (self.position[0]+1, self.position[1]), self.goal))
        else:
            sucessors.append(MyAgent(self.map, '1', self.position, self.goal))
        
        if self.position[1] > 0 and self.map[self.position[0]][self.position[1]-1] == '0':
            sucessors.append(MyAgent(self.map, '2', (self.position[0], self.position[1]-1), self.goal))
        else:
            sucessors.append(MyAgent(self.map, '2', self.position, self.goal))
        
        if self.position[1] < len(self.map[0])-1 and self.map[self.position[0]][self.position[1]+1] == '0':
            sucessors.append(MyAgent(self.map, '3', (self.position[0], self.position[1]+1), self.goal))
        else:
            sucessors.append(MyAgent(self.map, '3', self.position, self.goal))
        
        return sucessors

    def is_goal(self):
        return self.position == self.goal

    def description(self):
        return "Agente que sabe andar em um grid simples"

    def cost(self):
        return 1

    def env(self):
        return f'{self.position[0]};{self.position[1]}'

def get_actions(map, position, goal):
    #
    # Esta fnção deve retornar uma lista de ações que o agente deve executar
    # Assim conseguimos executar o agente no ambiente usando a biblioteca
    # gym_simplegrid
    #

    state = MyAgent(map, '', position, goal)
    algorithm = BuscaLargura()
    result = algorithm.search(state,pruning='general')
    if result != None:
        return result.show_path()
    else:
        return None

def parser_actions(str_actions):
    if str_actions != None:
        actions = str_actions.split(';')
        actions = list(map(int, actions[1:]))
        return actions
    return None

