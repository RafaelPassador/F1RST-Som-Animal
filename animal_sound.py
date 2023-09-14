'''
Rafael Passador
09/23
Desafio F1RST - Enghenaria de Dados
'''

#Utilizando o padrão de projeto Singleton, que garante que apenas uma instância da classe seja criada,
class AnimalSound:
    _instance = None
    _history = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def make_sound(self, animal):
        from animais.gato import Gato
        from animais.cachorro import Cachorro

        if animal == 1:
            animal_obj = Gato()
        elif animal == 2:
            animal_obj = Cachorro()
        else:
            raise ValueError("Opção inválida")

        sound = animal_obj.make_sound()
        self._history.append((animal, sound))
        return sound

    def show_history(self):
        if not self._history:
            return "Histórico vazio"
        return "\n".join([f"{animal} {sound}" for animal, sound in self._history])
