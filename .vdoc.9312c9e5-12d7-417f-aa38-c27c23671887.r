#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
#
#
x <- 10
y <- 200

# teste condicional único
x > 20

# expressões condicionais
x > 20 & y > 20
x > 20 | y > 20
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

# R base
municipios1 <- data.frame(nome=nomes_mun,populacao=pop_mun)

# tidyverse
municipios2 <- tibble(nome=nomes_mun,populacao=pop_mun)

print(municipios1)
print(municipios2)
#
#
#
#
#
#
#
#
#
idade <- 20

if (idade >= 18) {
  print('Maior de idade')
} else {
  print('Menor de idade')
}
#
#
#
#
#
for (i in 1:5) {
  print(i)
}
#
#
#
#
#
contador <- 1

while (contador <= 3) {
  print(contador)
  contador <- contador + 1
}
#
#
#
#
#
#
#
#
#
frase_cinema <- function() {
    print('Que a força esteja com você!')
}

frase_cinema()
#
#
#
#
#
total_calc <- function(bill_amount,tip_perc=10){
    total <- bill_amount*(1 + tip_perc/100)
    print(paste('O valor final da sua conta foi: R$ ',total))
}

# Cálculo do valor final da conta utilizando a gorjeta padrão de 10%
total_calc(bill_amount=10)

# Cálculo do valor final da conta utilizando uma gorjeta de 17%
total_calc(bill_amount=10,tip_perc=17)
#
#
#
#
#
#
#
#
#
#
#
ocupadas <- c(90593,92170,92962,92366,90174,92228,93534,95515,87225,95747)
desocupadas <- c(6730,6151,6555,9222,12476,12453,12413,11903,14412,12011)
na_forca <- c(97322,98321,99516,101588,102650,104682,105947,107418,101637,107758)
fora_da_forca <- c(58007,59244,60162,60092,60953,60777,61299,61579,69042,64525)
ano <- seq(2012,2021)

dados <- tibble(ano=ano,
                ocupadas=ocupadas,
                desocupadas=desocupadas,
                na_forca=na_forca,
                fora_da_forca=fora_da_forca)

str(dados)
#
#
#
#
#
#
#
#
#
#
#
df <- dados %>%
      mutate(taxa_desemp = desocupadas / (ocupadas + desocupadas)) %>%
      mutate(razao_part = na_forca / (na_forca + fora_da_forca)) %>%
      filter(ano>=2014) %>%
      select(ano, taxa_desemp, razao_part)

df
#
#
#
#
#
#
#
#
#
#
#
#
#
ggplot(df, aes(x=ano,y=taxa_desemp)) +
  geom_line() +
  labs(title='Evolução da taxa de desemprego no Brasil',x='Ano')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
