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
#
#
#| message: false
#| warning: false

import numpy as np
import sympy
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
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
a = np.array([1, 2, 3])
print(a)
print(type(a))
#
#
#
#
#
#| error: true

a = np.array(1, 2, 3)
#
#
#
#
#
a = np.zeros(3)
b = np.ones(3)

print(a)
print(b)
#
#
#
#
#
a = np.zeros(3, dtype=int)
b = np.ones(3, dtype=int)

print(a)
print(b)
#
#
#
#
#
a = np.linspace(0,8,5, dtype=int)

print(a)
#
#
#
#
#
print('Array a =',a)
print('\nPrimeiro elemento de a = ',a[0])
print('Segundo elemento de a = ',a[1])
print('Último elemento de a = ',a[-1])
print('Dois primeiros elementos de a = ',a[0:2])
#
#
#
#
#
#
#
#
#
A_22 = np.array([[1, 2], [3, 4]], dtype=int)

print('Matriz A =\n',A_22)
#
#
#
#
#
print('Matriz identidade 2x2 =\n',np.eye(2,dtype=int))
print('\nMatriz diagonal 3x3 =\n',np.diag([1,2,3]))
#
#
#
#
#
print('Matriz A =\n',A_22)
print('\nTransposta da matriz A =\n',np.transpose(A_22))
print('\nTransposta da matriz A =\n',A_22.T)
#
#
#
#
#
A = np.array([[1,2,3], [4,5,6], [7,8,9]])

print('Matriz A =\n',A)
print('\nElemento 11 de A = ',A[0,0])
print('Elemento 23 de A = ',A[1,2])
print('Primeira linha de A = ',A[0,:])
print('Segunda coluna de A = ',A[:,1])
print('\nSubmatriz de A delimitada pelos elementos 22 e 33 =\n',A[1:,1:])
#
#
#
#
#
#
#
#
#
#
#
#
X1 = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
X2 = X1.flatten() # O método flatten reduz um array de n-dimensões em um array de uma única dimensão

print('Array X1 =\n',X1)
print('\nDimensões de X1 = ', X1.ndim)
print('Shape de X1 = ', X1.shape)
print('Tipo de dado em X1 = ', X1.dtype)
print('Número de elementos em X1 = ', X1.size)

print('\n\nArray X2 =\n',X2)
print('\nDimensões de X2 = ', X2.ndim)
print('Shape de X2 = ', X2.shape)
print('Tipo de dado em X2 = ', X2.dtype)
print('Número de elementos em X2 = ', X2.size)
#
#
#
#
#
X = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]) 

print('Array X1 4x4 =\n',X)
print('\n X1 reorganizado em 2x8 =\n',X.reshape(2,8))
print('\n X1 reorganizado em 8x2 =\n',X.reshape(8,2))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
x = np.array([1,2,3], dtype=int)
print("x =\n", x)
print("\n2 + x =\n", 2 + x)
print("\n2 - x =\n", 2 - x)
print("\n2 * x =\n", 2 * x)
print("\nx / 2 =\n", x / 2)
#
#
#
X = np.ones((2, 2), dtype=int)

print("X =\n", X)
print("\n2 + X =\n", 2 + X)
print("\n2 - X =\n", 2 - X)
print("\n2 * X =\n", 2 * X)
print("\nX / 2 =\n", X / 2)
#
#
#
#
#
x = np.array([2, 4, 6], dtype=int)
y = np.array([2, 2, 1], dtype=int)

print("x =\n", x)
print("\ny =\n", y)
print("\nx + y =\n", x + y)
print("\nx - y =\n", x - y)
#
#
#
X = np.array([[2, 4], [6, 8]], dtype=int)
Y = np.array([[2, 2], [2, 2]], dtype=int)

print("X =\n", X)
print("\nY =\n", Y)
print("\nX + Y =\n", X + Y)
print("\nX - Y =\n", X - Y)
#
#
#
#
#
#
#
#
#
#
#
print('Vetores x e y:')
print('x =',x)
print('y =',y)
print("\n x * y =\n", x * y)
print("\n x / y =\n", x / y)

print('\nMatrizes X e Y:')
print('X =\n',X)
print('Y =\n',Y)
print("\n X * Y =\n", X * Y)
print("\n X / Y =\n", X / Y)
#
#
#
#
#
X= np.array([[1, 2], [3, 4]], dtype=int)
Y= np.array([[10, 20], [30, 40]], dtype=int)

print('X =\n',X)
print('Y =\n',Y)
print('\nX * Y =\n', X @ Y)
print('\nX * Y =\n', np.dot(X,Y))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
x = np.array([1,2,3,4,5])

print('Array x = ',x)
print('\nMínimo de x = ',np.amin(x))
print('Máximo de x = ',np.amax(x))
print('Intervalo de x = ',np.ptp(x))
print('Soma de x = ',np.sum(x))
print('Média de x = ',np.mean(x))
print('Log de x = ',[np.round(elem,2) for elem in np.log(x)])
#
#
#
#
#
#
#
my_array = np.arange(10000000)
my_list = list(range(10000000))
#
#
#
#
#
#
# arrays
start_array = time.time()
my_array2 = my_array * 2
end_array   = time.time()


# listas
start_lista = time.time()
my_list2 = [x * 2 for x in my_list] 
end_lista   = time.time()

ratio = (end_lista - start_lista) / (end_array - start_array)
#
#
#
#
#
print('Tempo necessário para a realização dos cálculos utilizando arrays: {:.4f} segundos'.format(end_array - start_array))
print('Tempo necessário para a realização dos cálculos utilizando listas: {:.4f} segundos'.format(end_lista - start_lista))
print('\nA abordagem de listas demorou {:.0f}x mais tempo! Esqueça listas e use arrays ;)'.format(ratio - 1))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
M = np.array([(2, 2, 1, 1),
              (1, 3, 1, 2),
              (1, 2, 2, -1)],dtype=float)
print('Matriz ampliada =\n',M)
#
#
#
#
#
M[0,:] = M[0,:] / M[0,0]

print(M)
#
#
#
#
#
M[1,:] = M[1,:] - M[0,:]
M[2,:] = M[2,:] - M[0,:]

print(M)
#
#
#
#
#
M[1,:] = M[1,:] / M[1,1]

print(M)
#
#
#
#
#
M[2,:] = M[2,:] - M[1,:]

print(M)
#
#
#
#
#
M[2,:] = M[2,:] / M[2,2]

print(M)
#
#
#
#
#
M[1,:] = M[1,:] - M[1,2] * M[2,:]

print(M)
#
#
#
#
#
M[0,:] = M[0,:] - M[0,2] * M[2,:]

print(M)
#
#
#
#
#
M[0,:] = M[0,:] - M[1,:]

print(M)
#
#
#
#
#
print('A solução de x1 é: {:.2f}'.format(M[0,3]))
print('A solução de x2 é: {:.2f}'.format(M[1,3]))
print('A solução de x3 é: {:.2f}'.format(M[2,3]))
#
#
#
#
#
M_sympy = sympy.Matrix([(2, 2, 1, 1),
                        (1, 3, 1, 2),
                        (1, 2, 2, -1)])

M_sympy.rref()[0]
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
b = np.array([1, 2, -1])
A = np.array([(2, 2, 1), (1, 3, 1), (1, 2, 2)])

np.shape(A)[0] == np.shape(A)[1]
#
#
#
#
#
print('A =')
print(A)

print('\nDeterminante = ',np.round(np.linalg.det(A)))
#
#
#
#
#
print('A =')
print(A)

print("\nInversa de A = ")
print(np.linalg.inv(A))
#
#
#
solution = np.linalg.inv(A) @ b
solution
#
#
#
print('A solução de x1 é: {:.2f}'.format(solution[0]))
print('A solução de x2 é: {:.2f}'.format(solution[1]))
print('A solução de x3 é: {:.2f}'.format(solution[2]))
#
#
#
#
#
np.linalg.solve(A,b)
#
#
#
#
#
#
#
#
#
exp = [15,13,12,13.5,18,3,17.7,11,16,9.3,8,11.2,14,6,4,7,9,15.6]
sal = [99,93,94,88,111,86,103,87,94,90,77,85,86,81,83,81,84,96]

print('O 3º indivíduo possui experiência de {} anos e um salário igual a R${}/hora.'.format(exp[2],sal[2]))
#
#
#
#
#
#| echo: false
import matplotlib.pyplot as plt
plt.scatter(exp,sal)
plt.show()
#
#
#
#
#
#| echo: false
from scipy import stats
b1, b0, r, p, std_err = stats.linregress(exp, sal)
yhat = [(float(b1)*x)+float(b0) for x in exp]

fig,ax=plt.subplots()
ax.scatter(exp,sal)
ax.plot(exp,yhat)
for i in range(len(sal)):
    parx=[exp[i],exp[i]]
    pary=[sal[i],yhat[i]]
    ax.plot(parx,pary,linestyle='--',color='r')
plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
Xlist = []
for x in exp:
    Xlist.append([1,x])

X = np.array(Xlist)
y = sal

XXinv = np.linalg.inv(X.transpose() @ X)

beta = XXinv * X.transpose() * y
print(beta)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
