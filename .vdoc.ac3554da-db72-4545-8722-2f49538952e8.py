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
    t = ['d', 'c', 'e', 'b', 'a']
    t.sort()
    print(t)
#
#
#
#
#
#
#
#
#
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
#
#
#
#
#
#
s = 'spam'
t = list(s)
print(t)
#
#
#
#
#
#
s = 'pining for the fjords'
t = s.split(' ')
print(t)
#
#
#
#
s = 'spam-spam-spam'
t = s.split('-')
t
#
#
#
#
#
#
t = ['spam','spam','spam']
s = ' - '.join(t)
print(s)
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
t = ('a', 'b', 'c', 'd', 'e')

print(type(t))
#
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
#
t = tuple()
print(t)
#
#
#
#
t = tuple('lupins')
print(t)
#
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
#
#| error: true

t[0] = 'A'
#
#
#
#
#
#
t = ('A',) + t[1:]
print(t)
#
#
#
#
#
#
(0, 1, 2) < (0, 3, 4)
#
#
#
#
(0, 1, 2000000) < (0, 3, 4)
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
#
#
#
#| error: true

a, b = 1, 2, 3
#
#
#
#
#
#
addr = 'monty@python.org'
uname, domain = addr.split('@')
#
#
#
#
#
#
print(uname)
print(domain)
#
#
#
#
#
#
#
#
print(7//3)
print(7%3)
#
#
#
#
t = divmod(7, 3)

print(t)
print(type(t))
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
s = 'abc'
t = [0, 1, 2]
zip(s,t)
#
#
#
#
#
#
for pair in zip(s, t):
    print(pair)
#
#
#
#
#
#
list(zip(s, t))
#
#
#
#
#
#
list(zip('Anne', 'Elk'))
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
eng2sp = dict()
eng2sp
#
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
#
eng2sp
#
#
#
#
#
#
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
eng2sp
#
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
#
#| error: true

eng2sp['four']
#
#
#
#
#
#
len(eng2sp)
#
#
#
#
#
#
'one' in eng2sp
#
#
#
#
'uno' in eng2sp
#
#
#
#
#
#
vals = eng2sp.values()
'uno' in vals
#
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
#
y['two'] = 'dos'
print(y)
#
#
#
#
#
#
#
#
y = {'one': 1, 'two': 2}
print(y)
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
#
x = {'one': 0, 'two': 2}
print(len(x))
#
#
#
#
#
#
#| error: true

y = {'one': 1, 'two': 2}
del y['three']
#
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
