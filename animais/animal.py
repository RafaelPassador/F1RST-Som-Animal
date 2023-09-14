'''
Rafael Passador
09/23
Desafio F1RST - Enghenaria de Dados
'''

from abc import ABC, abstractmethod

#Classe abstrata
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
