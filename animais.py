"""
    Um coelho 🐇 viu seis elefantes🐘 quando se dirigia ao rio.
    Cada elefante viu dois macacos🐒 que se dirigiam ao rio.
    Cada macaco levava um papagaio 🦜 no ombro.
    Quantos animais vão até o rio? 🙄
"""

class Animal():
    def __init__(self, tipo_animal_visto, qtd_animais_vistos):
        self.qtd_animais_vistos = qtd_animais_vistos
        self.tipo_animal_visto = tipo_animal_visto

    def __repr__(self):
        return f'''\n=============
Animal = {type(self).__name__}
Viu animais = {self.tipo_animal_visto}
Quantos viu = {self.qtd_animais_vistos}
=============\n'''

class Coelho(Animal):
    pass
    

class Elefante(Animal):
    pass

class Macaco():
    def __init__(self, tipo_animal_ombro = 'papagaio', qtd_animais_ombro = '1'):
        self.qtd_animais_ombro = qtd_animais_ombro
        self.tipo_animal_ombro = tipo_animal_ombro

    def __repr__(self):
        return f'''\n=============
Animal = {type(self).__name__}
Animal no ombro = {self.tipo_animal_ombro}
Quantos no ombro = {self.qtd_animais_ombro}
=============\n'''

coelho = Coelho('Elefante', '6')
elefantes = [Elefante('Macaco', 2) for x in range(6)]
macacos = [Macaco('Papagaio', 1) for x in range(12)]
print(macacos)
print(elefantes)

qtd_macacos = sum([elefante.qtd_animais_vistos for elefante in elefantes])
qtd_papagaios = sum([macaco.qtd_animais_ombro for macaco in macacos])
print(qtd_macacos + qtd_papagaios + 1)


