#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

library(tidyverse)
library(summarytools)
library(data.table)
library(ggplot2)
#
#
#
#
#
#
#
#
#
# Função 'print' imprime o texto entre aspas no console do RStudio
print('Hello, World!')
#
#
#
#
#
X <- 'Hello, World!'
print(X)
#
#
#
#
#
#
#
40 + 2
#
#
#
43 - 1
#
#
#
6 * 7
#
#
#
84 / 2
#
#
#
#
#
2 ^ 4
#
#
#
#
#
((38 + 2) * (2 + 2)) / 16
#
#
#
#
#
#
#
#
#
x <- 'tipo de dado: character'
y <- 10

class(x)
class(y)
#
#
#
#
#
#
#
v <- c(10,20,30)

class(v)
#
#
#
#
#
m <- matrix(c(10,20,30,
              40,50,60,
              70,80,90), nrow=3, ncol=3, byrow=TRUE)

class(m)
#
#
#
#
#
v[2]
m[3,3]
#
#
#
#
#
#
#
#
#
nomes_mun <- c('Dracena','São Paulo','Guarulhos')
pop_mun <- c(45474,11451999,1291784)
municipios <- data.frame(nome=nomes_mun,populacao=pop_mun)

print(municipios)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
