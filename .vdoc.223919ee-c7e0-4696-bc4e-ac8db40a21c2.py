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
#| message: false
#| warning: false

import re
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
## Uso de aspas simples
str1 = 'Hello, World'

print(str1)
print(type(str1))
#
#
#
## Uso de aspas duplas
str2 = "Hello, World"

print(str2)
print(type(str2))
#
#
#
#
#
str3 = """Das Utopias

Se as coisas são inatingíveis...ora!
Não é motivo para não querê-las...
Que tristes os caminhos, se não fora
A presença distante das estrelas!
           
Mario Quintana 
"""

print(str3)
print(type(str3))
#
#
#
#
#
#
#
print(str1)
print(str1[2])
#
#
#
#
#
# Extração do segundo caractere do string pelo índice positivo
print(str1[1])

# Extração do segundo caractere do string pelo índice negativo
print(str1[-11])

# Extração do segundo caractere do string através de uma expressão
n = 0
print(str1[n+1])
#
#
#
#
#
print(str1[0:5])
#
#
#
#
#
uniao_str = str1 + ' --- ' + str2
print(type(uniao_str))
print(uniao_str)
#
#
#
#
#
#| error: true

# Tentemos substituir o 'e' do str1 por 'a'
str1[1] = 'a'
#
#
#
#
#
#
#
#
#
str_example=' Hello, World'
#
#
#
#
#
#
#
    print(str_example.upper())
    print(str_example.lower())
#
#
#
#
#
    print(str_example.strip())
#
#
#
#
#
    print(str_example.startswith(' '))
    print(str_example.endswith('d'))
#
#
#
#
#
    print(str_example.find(','))
#
#
#
#
#
    print(str_example.replace('Hello','World'))
#
#
#
#
#
#
#
#
#
pi = 3.1415926535
string_base='O valor de pi arredondado para 2 casas decimais é {:.2f}. Interessante, não?'

print(string_base.format(pi))
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
pesquisa = """
Pesquisa Datafolha divulgada nesta quinta-feira (18) mostra o ex-presidente Luiz Inácio Lula da Silva (PT) à frente, 
com 47% das intenções de voto na corrida pelo Palácio do Planalto. O presidente Jair Bolsonaro (PL) tem 32%. 
O primeiro turno das eleições acontece em 2 de outubro.

Na sequência, aparecem Ciro Gomes (PDT), com 7%; Simone Tebet (MDB), com 2%, e Vera Lúcia (PSTU), com 1%.
"""
print(pesquisa)
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
pesquisa2 = re.sub('[0-9]{1,2}%','ZZZ',pesquisa)

print(pesquisa2)
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
lista1 = [1,2,3,4,5]

print(type(lista1))
print(lista1)
#
#
#
#
#
lista2 = ['Danilo Souza','Artur Viaro']
lista3 = ['Turma 2026101',43.0,'Turmas 2026102',25,'Turmas 2026121',39,'Turmas 2026122',45]
lista4 = [lista1, lista2]

print(lista2)
print(lista3)
print(lista4)
#
#
#
#
#
lista_vazia = []

print(lista_vazia)
#
#
#
#
#
#
#
print(lista2[0])
print(lista2[1])
print(lista3[-1])
print(lista3[0:2])
#
#
#
#
#
numbers = [42, 123]
numbers[1] = 5

print(numbers)
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
produtos_mercado = ['alface','tomate','arroz','ovos','carne moída','sabão líquido']

print(len(produtos_mercado))
#
#
#
novos_produtos = ['papel higiênico','pasta de dente']

lista_concatenada = produtos_mercado + novos_produtos
print(lista_concatenada)
#
#
#
#
#
#
#
list_example=['a', 'c', 'b']
#
#
#
#
#
#
#
    list_example.append('g')

    print(t)
#
#
#
#
#
    l2 = ['e','d','f']
    list_example.extend(l2)

    print(list_example)
#
#
#
#
#
    list_example.sort()

    print(list_example)
#
#
#
#
#
    list_example.remove('e')

    print(list_example)
#
#
#
#
#
t = ['d', 'c', 'e', 'b', 'a']
ts = t.sort()

print(ts)
#
#
#
#
#
s = 'aula'
t = list(s)
print(t)
#
#
#
#
#
j = 'a pressa é inimiga da perfeição'
s = j.split(' ')

print(s)
#
#
#
#
#
s = ['a','pressa','é','inimiga','da','perfeição']
j = ' '.join(s)

print(j)
#
#
#
#
#
#
#
#
#
t = ('a','b','c','d','e')

print(type(t))
#
#
#
#
#
t1 = ('a')
t2 = 'a',
t3 = ('a',)

print(type(t1))
print(type(t2))
print(type(t3))
#
#
#
#
#
t1 = tuple()
t2 = tuple('tupla')

print(t1)
print(t2)
#
#
#
#
#
#
#
t = ('a', 'b', 'c', 'd', 'e')

print(t[0])
print(t[1:3])
#
#
#
#
#
#| error: true

t[0] = 'A'
#
#
#
#
#
#
#
#
a=5
b=6

temp = a
a = b
b = temp

print(b)
#
#
#
#
#
a=5
b=6

a, b = b, a

print(b)
#
#
#
#
#
addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname)
print(domain)
#
#
#
#
#
#
#
s = 'abc'
t = [0, 1, 2]
z = zip(s,t)

print(z)
#
#
#
#
#
print(list(z))
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
eng2sp = dict()

eng2sp
#
#
#
#
#
eng2sp['one'] = 'uno'
#
#
#
#
#
eng2sp
#
#
#
#
#
eng2sp = {'one': 'uno', 'three': 'tres', 'two': 'dos', 'eleven': 'once'}
eng2sp
#
#
#
#
#
eng2sp['two']
#
#
#
#
#
#| error: true

eng2sp['four']
#
#
#
#
#
#
#
y = {}
y['one'] = 1
y['two'] = 2

print(y)
#
#
#
y['two'] = 'dos'
print(y)
#
#
#
#
#
del y['two']
print(y)
#
#
#
#
#
#| error: true

del y['three']
#
#
#
'three' in y
#
#
#
#
#
#
#
dict_example = {'one':1,'two':2,'three':3,'four':4}
#
#
#
#
#
#
#
    dict_update = {'five': 5, 'six': 6}
    
    x.update(y)
    print(x)
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
x = {'one': 0, 'two': 2}
y = {'one': 1, 'three': 3}
print(x)

x.update(y)
print(x)
#
#
#
#
x = {'one': 1, 'two': 2}
print(x.keys())
#
#
#
#
x = {'one': 1, 'two': 2}
print(x.items())
#
#
#
#
y = {'one': 1, 'two': 2}
print(y.get('one'))
print(y.get('three'))
print(y.get('three', 'The key does not exist.'))
#
#
#
#
y = {'one': 1, 'two': 2}
print(y.setdefault('three', '3'))
print(y.setdefault('two', 'dos'))
print(y)
#
#
#
#
print(y.setdefault('four'))
print(y)
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
