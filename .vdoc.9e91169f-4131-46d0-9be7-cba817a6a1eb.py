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
#| message: false
#| warning: false

import numpy as np
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
5 == 5
#
#
#
5 == 6
#
#
#
lista1 = [1,2,3,4,5]
lista2 = [5,4,3,2,1]

lista1 == lista2
#
#
#
#
#
#
#
42 and True
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
x=5

if x > 0:
    print('x é positivo')
#
#
#
#
#
#
#
#
#
idade = 17

if idade >= 18:
    print('Indivíduo é maior de idade')
else:
    print('Indivíduo é menor de idade')
#
#
#
#
#
#
#
#
#
x = 5
y = 6

if x < y:
    print('x é menor do que y')
elif x > y:
    print('x é maior do que y')
else:
    print('x e y são iguais')
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
print(list(range(0,10)))
#
#
#
for i in list(range(0,10)):
    
    u = np.random.uniform()
    print(u)
#
#
#
#
#
for i in list(range(0,10)):
    
    u = np.random.uniform()
    string='Essa é a iteração '+str(i+1)+' e o número sorteado foi: {:.2f}'
    print('Essa é a iteração '+str(i+1)+' e o número sorteado foi: {:.2f}'.format(u)) 
#
#
#
#
#
#
#
#
str1 = 'Vou nadaaaa'

for c in str1:
    print(c)
#
#
#
#
lista1 = ['Minha terra tem palmeiras','onde canta o sabiá','seno A cosseno B','seno B cosseno A']

for f in lista1:
    print(f)
#
#
#
#
#
#
#
#
for i in ['foo','bar','baz','qux']:
    
    if 'b' in i:
        break
    print(i)
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
str1 = 'O Tata é foota, o Tata é foota'

# Algumas linhas de código adicionais para excluir pontuação e transformar o string em uma lista de palavras
str1 = str1.replace('.','')
str1 = str1.replace(',','')
str1 = str1.replace('?','')
lista1 = str1.split()

for c in lista1:
    print(c)
#
#
#
#
#
#
for count,value in enumerate(lista1):
    
    print('Elemento '+str(count)+' = '+value)
#
#
#
#
#
#
print(lista1)
#
#
#
#
lista2 = list(range(0,len(lista1)))
print(lista2)
#
#
#
#
len(lista1) == len(lista2)
#
#
#
#
for count,value in zip(lista2, lista1):
    
    print('Elemento '+str(count)+' = '+value)
#
#
#
#
#
#
professores = ['Danilo Souza','Danilo Souza','Claudio Lucinda']
turmas = ['2024201','2024202','2024221']

for p,t in zip(professores,turmas):
    
    print('Nesse curso, a turma '+t+' é de responsabilidade do professor '+p)
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
lista1 = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
lista2 = []

for x in lista1:
    lista2.append(int(x**0.5))
    
print(lista2)
#
#
#
#
#
#
lista2 = [int(x**0.5) for x in lista1] 

print(lista2)
#
#
#
#
#
#
import time 
lista1 = list(range(1,1000000))

# list comprehension
start_comp = time.time()

list_comp  = [int(x**0.5) for x in lista1]

end_comp   = time.time()


# loop
start_loop = time.time()

list_loop = []
for x in lista1:
    list_loop.append(int(x**0.5))  
    
end_loop   = time.time()

ratio = (start_loop - end_loop) / (start_comp - end_comp)
#
#
#
#
#
#
print('Tempo necessário para a realização dos cálculos utilizando list comprehensions: {:.4f} segundos'.format(end_comp - start_comp))
print('Tempo necessário para a realização dos cálculos utilizando loop: {:.4f} segundos'.format(end_loop - start_loop))
print('\nA abordagem de loop demorou {:.1%} mais tempo! Dê uma chance para list comprehensions ;)'.format(ratio - 1))
#
#
#
#
#
#
#
#
x = 5
print(x)
#
#
#
#
x = 7
print(7)
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
a = 5
b = a # a e b agora são iguais

print('Valor de a: '+str(a)+'\nValor de b: '+str(b))

a = 3 # a e b não são mais iguais

print('\nValor de a: '+str(a)+'\nValor de b: '+str(b))
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
#
#
n = 5

while n > 0:
    n = n-1
    print(n)
    
print('\nÀ partir de agora as instruções fora do loop serão executadas.')
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
a = ['foo', 'bar', 'baz']
print(a)

while a:
    
    a.pop(-1)
    print(a)
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
n = 5
print(n)

while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
    
print('Loop ended.')
#
#
#
#
#
#
n = 5

while n > 0:
    n = n - 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
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
import numpy as np

x = np.random.uniform(-40, 40, 10)
print(x)
#
#
#
#
#
#
x = np.random.uniform(-40, 40, 10)
print(x)
#
#
#
#
#
#
np.random.seed(1)

x = np.random.uniform(-40, 40, 10)
print(x)
#
#
#
#
np.random.seed(1)

x = np.random.uniform(-40, 40, 10)
print(x)
#
#
#
#
#
#
np.mean(x)
#
#
#
#
#
#
#
#
# number of sample
n = 10 
means = [] 

np.random.seed(1)

for j in list(range(0,n)):
    
    lista_sorteio = np.random.uniform(-40, 40, 50)
    x = np.mean(lista_sorteio)
    means.append(x)

means = [np.round(elem,2) for elem in means]
print(means)
np.mean(means)
#
#
#
#
#
#
# number of sample
n = 100 
means = [] 

np.random.seed(1)

for j in list(range(0,n)):
    
    lista_sorteio = np.random.uniform(-40, 40, 50)
    x = np.mean(lista_sorteio)
    means.append(x)

means = [np.round(elem,2) for elem in means]
print(means)
np.mean(means)
#
#
#
#
#
#
expoentes = [1,2,3,4,5,6,7,8,9,10]
N = [2**exp for exp in expoentes]

means = [] 

np.random.seed(1)
for n in N:
    
    means_atual = [] 
    for j in list(range(0,n)):
        
        lista_sorteio = np.random.uniform(-40, 40, 100)
        x = np.mean(lista_sorteio)
        means_atual.append(x)
        
    means.append(np.mean(means_atual))
#
#
#
#
for m in means:
    
    print(np.round(m,2))
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
