# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| message: false
#| warning: false

import rich
import dataclasses
import pandas as pd
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
x = 10
y = 'Danilo'

print(type(x))
print(type(y))
#
#
#
#
#
#
#
print(id(x))
print(id(y))
#
#
#
#
#
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(id(lista1))
print(id(lista2))
#
#
#
#
#
#
#
#
#
dados = pd.DataFrame({"nome": ["Ana", "Bruno", "Carlos"],"idade": [20, 25, 30]})

print(dados.shape)
print(dados.columns)
print(dados.index)
#
#
#
#
#
#
#
#
#
#
#
s = 'Esse é um string'

# operação sobre os dados contidos no string 's'
print(s.upper())

# operação através da combinação do string 's' com o outro string
print(s.replace('Esse','Este'))
#
#
#
#
#
lista1 = [1,2,3]
lista1[0] = 'primeiro elemento'

print(lista1)
#
#
#
#
#
lista2 = [1,2,3]
lista2.__setitem__(0,'primeiro elemento')

print(lista2)
#
#
#
#
#
# uso da função nativa
print(len(lista2))

# uso do método
print(lista2.__len__())
#
#
#
#
#
#
lista1 = [1,2,3]
rich.inspect(lista1, methods=True)
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
class Municipio:
    def __init__(self,nome,estado,area,populacao):
        
        self.nome = nome
        self.uf = estado
        self.km2 = area
        self.pop = populacao
#
#
#
#
#
dracena = Municipio('Dracena','SP',487.688,45474)
sp = Municipio('São Paulo','SP',1521.202,11451999)

print(type(dracena))
#
#
#
print(dracena.nome)
print(dracena.km2)
print(sp.pop)
#
#
#
#
#
class Municipio:
    def __init__(self,nome,estado,area,populacao):
        
        self.nome = nome
        self.uf = estado
        self.km2 = area
        self.pop = populacao

    def densidade_pop(self):
        return self.populacao / self.area    
#
#
#
#
#
dracena = Municipio('Dracena','SP',487.688,45474)
sp = Municipio('São Paulo','SP',1521.202,11451999)

print(dracena.densidade_pop())
print(sp.densidade_pop())
#
#
#
#
#
#
#
@dataclass
class Municipio:
    nome: str
    uf: str
    km2: float
    pop: int

    def densidade_pop(self):
        return self.pop / self.km2
#
#
#
#
#
dracena = Municipio('Dracena','SP',487.688,45474)

print(dracena.nome)
print(dracena.densidade_pop())
#
#
#
#
#
#
#
#
#
#
#
