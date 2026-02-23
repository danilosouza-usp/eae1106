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
#
#
#| message: false
#| warning: false

import numpy as np
import time
#
#
#
#
#
#
#
#
#
notas1 = [7.5, 8.0, 6.5]
media1 = sum(notas1) / len(notas1)
print(media1)

notas2 = [9.0, 8.5, 7.0]
media2 = sum(notas2) / len(notas2)
print(media2)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def frase_cinema():
    print('Que a força esteja com você!')
#
#
#
#
#
frase_cinema()
#
#
#
#
#
#
#
#
#
#
#
def my_func(name,place):
    strf='Olá '+name+'! Você é de '+place+'?'
    print(strf)

my_func('Emily','Paris')
#
#
#
#
#
my_func('Ribeirão Preto','Roberto')
#
#
#
#
#
my_func(place='Ribeirão Preto',name='Roberto')
#
#
#
#
#
def total_calc(bill_amount,tip_perc=10):
    total=bill_amount*(1 + tip_perc/100)
    total=round(total,2)
    print('O valor final da sua conta foi: R$'.format(total))
#
#
#
#
#
#
#
#
#
def my_var_sum(*args):
    
    sum = 0
    for arg in args:
        sum=sum+arg
        
    print('A soma total dos números fornecidos é igual a: '+str(sum))
#
#
#
#
#
my_var_sum(99,10,54,23)
my_var_sum(9,87)
my_var_sum(5,21,36,79,45,65)
my_var_sum(1)
#
#
#
#
#
#
#
def myFun(**kwargs):
    
    for key, value in kwargs.items():
        print(key+' == '+value)
  
myFun(first='Geeks', mid='for', last='Geeks')
#
#
#
#
#
def myFun(arg1, **kwargs):
    
    for key, value in kwargs.items():
        print(arg1+key+' == '+value)
  
myFun("Hi - ", first='Geeks', mid='for', last='Geeks')
#
#
#
#
#
#
#
def is_divisible(x, y):
    
    if x % y == 0:
        print(True)
    else:
        print(False)
    
is_divisible(6, 4)
#
#
#
#
#
#
#
states = [' Alabama ','Georgia!','Georgia','georgia','FlOrIda','south carolina##','West virginia?']

def clean_strings(lista_strings):
    result=[]
    
    for value in lista_strings:
        value = value.strip()
        value = value.title()
        value = value.replace('#','')
        value = value.replace('?','')
        value = value.replace('!','')
        result.append(value)
    
    print(result)

print(states)
print()
clean_strings(states)
#
#
#
#
#
#
#
def my_func(name,place):
    
    strf='Olá '+name+'! Você é de '+place+'?'
    return

x = my_func("Jane","Paris")
#
#
#
#
#
#
def raiz(x):
    
    fx = x**0.5

y = raiz(100)
print(y)
#
#
#
#
def raiz(x):
    
    fx = x**0.5
    return fx

y = raiz(100)
print(y)
#
#
#
#
#
#
#
#
def concat_strings(str1,str2):
    
    texto_concatenado = str1 + ' ' + str2
    print(texto_concatenado)
    

texto1 = 'Que a força esteja com você,'
texto2 = 'jovem Padawan.'

concat_strings(texto1,texto2)
#
#
#
#
#
#
#| error: true

print(texto_concatenado)
#
#
#
#
#
#
#
#
def func_tcl(dist=None,intervalo=(0,1),n=100, samples=10):
    
    if dist == None:
        print('Você esqueceu de carregar uma função que defina a distribuição de X!')
    else:
        means = []
        for j in range(0,samples):
            x_func_tcl = dist(intervalo[0],intervalo[1],n)
            mean_x = sum(x_func_tcl)/len(x_func_tcl)
            
            means.append(mean_x)
            mean_of_means = sum(means)/len(means)
        
        print('Essa é a lista de médias:')
        print(means)
        print('\nE essa é a média das médias:')
        print(mean_of_means)
#
#
#
#
np.random.seed(1)

func_tcl(dist=np.random.uniform,intervalo=(-40,40),n=50,samples=10)
#
#
#
#
#
#
#| error: true

print(mean_of_means)
#
#
#
#
#
#
def func_tcl(dist=None,intervalo=(0,1),n=100, samples=10):
    
    if dist == None:
        print('Você esqueceu de carregar uma função que defina a distribuição de X!')
    else:
        means = []
        for j in range(0,samples):
            x_func_tcl = dist(intervalo[0],intervalo[1],n)
            mean_x = sum(x_func_tcl)/len(x_func_tcl)
            
            means.append(mean_x)
            mean_of_means = sum(means)/len(means)
        
        return mean_of_means
#
#
#
#
np.random.seed(1)

func_tcl(dist=np.random.uniform,intervalo=(-40,40),n=50,samples=10)
#
#
#
#
#
#
expoentes = [1,2,3,4,5,6,7,8,9,10]
Y = [2**exp for exp in expoentes]

means_of_means = []

np.random.seed(1)
for y in Y:

    mean_of_means = func_tcl(dist=np.random.uniform,intervalo=(-40,40),n=100,samples=y)
    means_of_means.append(mean_of_means)
#
#
#
#
for m in means_of_means:
    
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
def imprime_tipo(x):
    
    '''
    Função criada para a matéria EAE1106 - Métodos Computacionais para Economia
    Objetivo: função simples que imprime o tipo do objeto recebido como argumento.
    '''
    
    print(type(x))
#
#
#
#
#
#
print(imprime_tipo.__doc__)
#
#
#
#
#
#
# documentação da função nativa len()
print(len.__doc__)
#
#
#
#
# documentação da função time() dentro do pacote time
print(time.time.__doc__)
#
#
#
#
# documentação da função uniform() dentro do pacote NumPy
print(np.random.uniform.__doc__)
#
#
#
#
#
#
# documentação do NumPy
print(np.__doc__)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
#
#
#
#
#
#
#
#
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
