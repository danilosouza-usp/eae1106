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

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs
import plotly as ply
#
#
#
#
#
#
#
#
#
#
#
# substituir esse caminho de diretório pelo caminho que você estiver utilizando no seu computador
os.chdir('C:/Users/user/Desktop/EAE1106')

columns_to_read = ['country','year','pop','emp','rgdpna','avh']
df_pwt = pd.read_csv('pwt110_selected.csv', sep=';', encoding='utf8',usecols=columns_to_read)
df_pwt.info()
#
#
#
#
#
#
df_pwtbr = df_pwt.loc[df_pwt['country']=='Brazil',:].reset_index(drop=True)

x = df_pwtbr['year']
y = df_pwtbr['avh'] / 260 

# construção do gráfico
plt.plot(x, y, 'b-', linewidth=2)
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
df_pwtbr.describe()
#
#
#
#
#
x_ticks = [1950,1960,1970,1980,1990,2000,2010,2020]
x_labels = ['1950','1960','1970','1980','1990','2000','2010','2020']
y_ticks = [5,6,7,8,9,10]
y_labels = ['5','6','7','8','9','10']

plt.plot(x, y, color='#1f77b4', linewidth=1, marker='o') # Saiba que o código "#1f77b4" é um código hexadecimal de cores. Para entender qual cor esse código representa acesse: https://htmlcolorcodes.com/

plt.xticks(x_ticks, x_labels)
plt.yticks(y_ticks, y_labels)
plt.ylim([4.8, 10.2])
plt.title('Horas médias trabalhadas por dia no Brasil')
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
fig, ax = plt.subplots()

ax.plot(x, y, 'b-', linewidth=2)
plt.show()
#
#
#
#
#
#
#
#
fig, ax = plt.subplots()

fig.set_facecolor("red")
ax.set_facecolor("blue")

plt.show()
#
#
#
#
#
x_ticks = [1950,1960,1970,1980,1990,2000,2010,2020]
x_labels = ['1950','1960','1970','1980','1990','2000','2010','2020']
y_ticks = [5,6,7,8,9,10]
y_labels = ['5','6','7','8','9','10']

fig, ax = plt.subplots()

ax.plot(x, y, color='#1f77b4', linewidth=1, marker='o')
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)
ax.set_ylim(4.8, 10.2)

plt.title('Horas médias trabalhadas por dia no Brasil')
plt.show()
#
#
#
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Tipo de gráfico a ser plotado
ax.plot(x, y, color='#1f77b4', linewidth=1, marker='o', markersize=4)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Mostrar o resultado
plt.show()
#
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Tipo de gráfico a ser plotado
ax.plot(x, y, color='#1f77b4', linewidth=1, marker='o', markersize=4)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Mostrar o resultado
plt.show()
#
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Tipo de gráfico a ser plotado
ax.plot(x, y, color='#1f77b4', linewidth=1, marker='o', markersize=4)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Marcadores dos eixos
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=10, fontweight='light')
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=10, fontweight='light')

# Limites dos eixos
ax.set_xlim(1949, 2024)
ax.set_ylim(4.8, 10.2)

# Mostrar o resultado
plt.show()
#
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Tipo de gráfico a ser plotado
ax.plot(x, y, color='#1f77b4', linewidth=1, marker='o', markersize=4)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Marcadores dos eixos
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=10, fontweight='light')
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=10, fontweight='light')

# Limites dos eixos
ax.set_xlim(1949, 2024)
ax.set_ylim(4.8, 10.2)

# Linha de referência
ax.plot([1949, 2024], [y.mean(), y.mean()], 'r--', lw=1.0)
ax.annotate('Média de horas trabalhadas\npor dia útil: {:,.2f}'.format(y.mean()),xy=(1949, 0.95*y.mean()),fontsize=9.5,color='r',fontweight='normal',style='italic')

# Mostrar o resultado
plt.show()
#
#
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Tipo de gráfico a ser plotado
ax.plot(x, y, color='#1f77b4', linewidth=1, marker='o', markersize=4)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Marcadores dos eixos
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=10, fontweight='light')
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=10, fontweight='light')

# Limites dos eixos
ax.set_xlim(1949, 2024)
ax.set_ylim(4.8, 10.2)

# Linha de referência
ax.plot([1949, 2024], [y.mean(), y.mean()], 'r--', lw=1.0)
ax.annotate('Média de horas trabalhadas\npor dia útil: {:,.2f}'.format(y.mean()),xy=(1949, 0.95*y.mean()),fontsize=9.5,color='r',fontweight='normal',style='italic')

# Título e fonte
plt.suptitle('Horas médias trabalhadas por dia - Brasil',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=15)

# Salvar a figura e mostrar o resultado
plt.savefig('avhbr_pwt11.png', bbox_inches='tight')
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
x_ticks = [1950,1960,1970,1980,1990,2000,2010,2020]
x_labels = ['1950','1960','1970','1980','1990','2000','2010','2020']
y_ticks = [5,6,7,8,9,10]
y_labels = ['5','6','7','8','9','10']

x = df_pwt.loc[0:73,'year']
y1 = df_pwt.loc[df_pwt['country']=='Brazil','avh'] / 260 
y2 = df_pwt.loc[df_pwt['country']=='United States','avh'] / 260
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Séries a serem plotadas
ax.plot(x, y1, color='#1f77b4',linewidth=2,marker='o',markersize=4)
ax.plot(x, y2, color='#d62728',linewidth=2,marker='s',markersize=4)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Marcadores dos eixos
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=10, fontweight='light')
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=10, fontweight='light')

# Limites dos eixos
ax.set_xlim(1949, 2024)
ax.set_ylim(4.8, 10.2)

# Título e fonte
plt.suptitle('Horas médias trabalhadas por dia - Brasil',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=15)

# Salvar a figura e mostrar o resultado
plt.savefig('avh_countries_pwt11.png', bbox_inches='tight')
plt.show()
#
#
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Séries a serem plotadas
ax.plot(x, y1, color='#1f77b4',linewidth=2,marker='o',markersize=4,label='Brasil')
ax.plot(x, y2, color='#d62728',linewidth=2,marker='s',markersize=4,label='Estados Unidos')

# Legenda
ax.legend(loc='center',bbox_to_anchor=(0.2,0.2),framealpha=0,ncol=1,prop={'size': 12})

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Marcadores dos eixos
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=10, fontweight='light')
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=10, fontweight='light')

# Limites dos eixos
ax.set_xlim(1949, 2024)
ax.set_ylim(4.8, 10.2)

# Título e fonte
plt.suptitle('Horas médias trabalhadas por dia - Brasil',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=15)

# Salvar a figura e mostrar o resultado
plt.savefig('avh_countries_pwt11.png', bbox_inches='tight')
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
num_rows = 1
num_cols = 1
height = 6
fig, ax = plt.subplots(num_rows,num_cols, figsize=(1.50*height, height))

type(ax)
#
#
#
#
#
num_rows = 2
num_cols = 1
height = 6
fig, ax = plt.subplots(num_rows,num_cols, figsize=(1.50*height, height))

type(ax)
#
#
#
#
#
num_rows = 2
num_cols = 1
height = 6
fig, ax = plt.subplots(num_rows,num_cols, figsize=(1.50*height, height))

# Séries a serem plotadas
ax[0].plot(x, y1, color='#1f77b4',linewidth=2,marker='o',markersize=4,label='Brasil')
ax[1].plot(x, y2, color='#d62728',linewidth=2,marker='s',markersize=4,label='Estados Unidos')

for i in range(0,2):
    # Legenda
    ax[i].legend(loc='upper left',bbox_to_anchor=(0.05,0.2),framealpha=0,ncol=1,prop={'size': 10})

    # Visibilidade das bordas
    ax[i].spines['top'].set_visible(False)
    ax[i].spines['right'].set_visible(False)
    ax[i].spines['left'].set_visible(False)
    ax[i].spines['bottom'].set_visible(True)
    ax[i].spines['bottom'].set_alpha(0.3)

    # Linhas de grid
    ax[i].grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

    # Marcadores dos eixos
    ax[i].set_xticks(x_ticks)
    ax[i].set_xticklabels(x_labels, fontsize=10, fontweight='light')
    ax[i].set_yticks(y_ticks)
    ax[i].set_yticklabels(y_labels, fontsize=10, fontweight='light')

    # Limites dos eixos
    ax[i].set_xlim(1949, 2024)
    ax[i].set_ylim(4.8, 10.2)

# Título e fonte
plt.suptitle('Horas médias trabalhadas por dia - Brasil',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=195)

# Salvar a figura e mostrar o resultado
plt.savefig('avh_countries2_pwt11.png', bbox_inches='tight')
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
df_pwt['pibpc'] = df_pwt['rgdpna'] / df_pwt['pop']

x = df_pwt.loc[df_pwt['year']==2010,'avh'] / 260
y = df_pwt.loc[df_pwt['year']==2010,'pibpc']
y = np.log(y)

x_ticks = [5,7,9,11]
x_labels = ['5','7','9','11']
y_ticks = [5,7,9,11,13]
y_labels = ['5','7','9','11','13']
#
#
#
#
height = 6
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Séries a serem plotadas
ax.scatter(x,y,color='#1f77b4',marker='o',s=50)

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Marcadores dos eixos
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=10, fontweight='light')
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=10, fontweight='light')

# Limites e título dos eixos
ax.set_xlim(4.8, 12)
ax.set_ylim(4.8, 13.2)
ax.set_xlabel('Número médio de horas trabalhadas por dia útil',fontsize=12, fontweight='light', labelpad=20)
ax.set_ylabel('Log do PIB per capita (US$)',fontsize=12, fontweight='light', labelpad=20)

# Título e fonte
plt.suptitle('Horas trabalhadas e PIB per capita, 2010',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=15)

# Salvar a figura e mostrar o resultado
plt.savefig('avh_pibpc_scatter.png', bbox_inches='tight')
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
df_pwt_top10 = df_pwt[df_pwt['year']==2010].copy()
df_pwt_top10.sort_values(['pibpc'],ascending=False,ignore_index=True,inplace=True)

# Manter no dataframe apenas os países que possuem informações para todas as colunas
df_pwt_top10.dropna(inplace=True)

# Selecionar apenas os 10 países mais ricos
df_pwt_top10 = df_pwt_top10.iloc[0:10,:].reset_index(drop=True)
df_pwt_top10
#
#
#
#
# Para não dar problema com os labels do eixo x serem muito grandes, vamos substituir aqueles que tem nomes compostos
df_pwt_top10.loc[5,'country'] = 'United\nArab\nEmirates'
df_pwt_top10.loc[9,'country'] = 'United\nStates'
#
#
#
#
#
#
#
x = df_pwt_top10['country']
y = df_pwt_top10['avh']

height = 8
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Séries a serem plotadas
ax.bar(x,y,align='center',color='#1f77b4')

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Título e fonte
plt.suptitle('Número médio de horas trabalhadas nos 10 países mais ricos, 2010',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=25)

# Salvar a figura e mostrar o resultado
plt.savefig('avh_bar.png', bbox_inches='tight')
plt.show()
#
#
#
#
#
height = 8
fig, ax = plt.subplots(1,1, figsize=(1.50*height, height))

# Séries a serem plotadas
ax.barh(x,y,align='center',color='#1f77b4')

# Visibilidade das bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)

# Linhas de grid
ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

# Título e fonte
plt.suptitle('Número médio de horas trabalhadas nos 10 países mais ricos, 2010',fontsize=15,fontweight='normal')
plt.title('Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal',pad=25)

# Salvar a figura e mostrar o resultado
plt.savefig('avh_barh.png', bbox_inches='tight')
plt.show()
#
#
#
#
#
#
#
#
df_pwt2010 = df_pwt[df_pwt['year']==2010].copy()
df_pwt2010.dropna(inplace=True)
df_pwt2010['pibpc'] = np.log(df_pwt2010['pibpc'])
# Exclusão de China e Índia, países com mais de 1 bilhão de habitantes, para melhor visualização
df_pwt2010 = df_pwt2010.loc[df_pwt2010['pop']<1000,:]

num_rows = 2
num_cols = 2
height = 8
fig, ax = plt.subplots(num_rows,num_cols, figsize=(1.50*height, height))

# Séries a serem plotadas
ax[0,0].hist(df_pwt2010['pop'],color='#1f77b4',bins=40)
ax[0,1].hist(df_pwt2010['emp'],color='#1f77b4',bins=40)
ax[1,0].hist(df_pwt2010['avh'],color='#1f77b4',bins=40)
ax[1,1].hist(df_pwt2010['pibpc'],color='#1f77b4',bins=40)

ax[0,0].set_title('População (milhões)', fontsize=8, fontweight='light')
ax[0,1].set_title('Pessoas empregadas (milhões)', fontsize=8, fontweight='light')
ax[1,0].set_title('Horas trabalhadas por dia útil', fontsize=8, fontweight='light')
ax[1,1].set_title('Log do PIB per capita', fontsize=8, fontweight='light')

for r in range(0,2):
    for c in range(0,2):
        # Visibilidade das bordas
        ax[r,c].spines['top'].set_visible(False)
        ax[r,c].spines['right'].set_visible(False)
        ax[r,c].spines['left'].set_visible(False)
        ax[r,c].spines['bottom'].set_visible(True)
        ax[r,c].spines['bottom'].set_alpha(0.3)

        # Linhas de grid
        ax[r,c].grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.1) 

        
# Ajuste de espaço entre os vários plots
fig.subplots_adjust(hspace = 0.6, wspace = 0.3)

# Título e fonte
plt.suptitle('Características dos países em 2010',y=1.05,fontsize=15,fontweight='normal')
plt.text(2.7, 25.3,'Fonte: Penn World Table, Versão 11.0',fontsize=12,fontweight='normal')

# Salvar a figura e mostrar o resultado
plt.savefig('carac_countries_all.png', bbox_inches='tight')
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
