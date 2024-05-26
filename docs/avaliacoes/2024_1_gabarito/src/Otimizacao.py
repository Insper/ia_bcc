from aigyminsper.search.CSPAlgorithms import SubidaMontanhaEstocastico, SubidaMontanha
from aigyminsper.search.Graph import State
import numpy as np
import math

class Otimizacao(State):

    def __init__(self, x):
        self.x = x

    def successors(self):
        sucessores = []
        sucessores.append(Otimizacao(self.x + 0.1))
        sucessores.append(Otimizacao(self.x - 0.1))
        return sucessores
    
    def h(self):
        #return (np.power(self.x + 2, 2)) - (16 * np.exp2(-np.power((self.x - 2), 2)))
        return (self.x + 2)**2 - 16 * math.exp(-(self.x - 2)**2)
    
    # eu não sei dizer qual eh o goal entao nao vou usar este 
    # metodo. se eu não uso este metodo entao eu nao posso usar
    # o subida da montanha estocastico
    def is_goal(self):
        return False
    
    def cost(self):
        return 1
    
    def env(self):
        return self.x
    
    def description(self):
        return "Problema de otimizacao de funcao"

# sabemos que o subida da montanha tem problema de minimo local
# desta forma eu vou iniciar varias vezes a busca sempre a partir de um
# valor diferente e vou guardar o valor de x e y melhores a cada iteracao

x = -11
y = math.inf

for i in range(-10,10,1):
   inicial = Otimizacao(i)
   result = SubidaMontanha().search(inicial)
   if  result == None:
       print("Nao encontrou solucao")
   else:
       print(f'Começando com i = {i} Valor de y = {result.h()} para x = {result.env()}')
       if result.h() < y:
           x = result.env()
           y = result.h()

print(f'=================================')
print(f'Melhor valor de x = {x} e y = {y}')



