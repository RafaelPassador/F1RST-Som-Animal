'''
Rafael Passador
09/23
Desafio F1RST - Enghenaria de Dados
'''

from .animal import Animal

#Classe concreta com polimorfismo
class Cachorro(Animal):
    def make_sound(self):
        return "Auau"
