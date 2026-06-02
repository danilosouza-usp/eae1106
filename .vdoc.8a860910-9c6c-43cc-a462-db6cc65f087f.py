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

import os
import pathlib
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
os.chdir('C:/Users/user/Desktop/EAE1106/projeto_empirico')
#
#
#
#
#
## homicidios
df_hrate = pd.read_excel('dados/original/UNDOC CTS - Homicides.xlsx',sheet_name='data_cts_intentional_homicide')
df_hrate = df_hrate.loc[(df_hrate['Indicator']=='Victims of intentional homicide') & 
                        (df_hrate['Dimension']=='Total') & 
                        (df_hrate['Category']=='Total') & 
                        (df_hrate['Sex']=='Total') & 
                        (df_hrate['Age']=='Total') & 
                        (df_hrate['Year']==2015) & 
                        (df_hrate['Unit of measurement']=='Rate per 100,000 population')]

df_hrate = df_hrate[['Iso3_code','Country','Subregion','VALUE']].reset_index(drop=True)
df_hrate.columns = ['country_code','country_name','region','hrate']

## efetivo policial
df_pol = pd.read_excel('dados/original/UNDOC CTS - Police.xlsx',sheet_name='data_cts_access_and_functioning')
df_pol = df_pol.loc[(df_pol['Indicator']=='Criminal Justice Personnel') & 
                    (df_pol['Dimension']=='by type of personnel') & 
                    (df_pol['Category']=='Police personel') & 
                    (df_pol['Sex']=='Total') & 
                    (df_pol['Age']=='Total') & 
                    (df_pol['Year']==2015) & 
                    (df_pol['Unit of measurement']=='Rate per 100,000 population')]

df_pol = df_pol[['Iso3_code','VALUE']].reset_index(drop=True)
df_pol.columns = ['country_code','police']

df_polh = pd.merge(df_hrate, df_pol, on=['country_code'],how='inner')
df_polh['police_log'] = np.log(HomicidioPolicia2015['police'])
HomicidioPolicia2015['hrate_log'] = np.log(HomicidioPolicia2015['hrate'])
df_polh = df_polh.dropna(how='any',axis=0)

## base final
df_polh.to_csv('dados/secundario/UNDOC_HomicidioPolicia2015.csv', sep=',', encoding='utf8',index=False)
#
#
#
#
#
#
#
HomicidioPolicia2015 = pd.read_csv('dados/secundario/UNDOC_HomicidioPolicia2015.csv', sep=',', encoding='utf8')
HomicidioPolicia2015.info()
#
#
#
#
#
#
#
HomicidioPolicia2015.describe()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| warning: false
xticks=[4,5,6,7,8]
yticks=[-2,0,2,4,6]
xtickslabel=['$4$','$5$','$6$','$7$','$8$']
ytickslabel=['$-2$','$0$','$2$','$4$','$6$']

x = HomicidioPolicia2015['police_log']
y = HomicidioPolicia2015['hrate_log']

height = 5
fig, ax = plt.subplots(1, 1, figsize=(1.50*height, height))

ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_alpha(0.3)
ax.spines['left'].set_alpha(0.3)

ax.set_xlim(3.9, 8.1)
ax.set_ylim(-2.1,6.4)

ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_xticklabels(xtickslabel, fontsize=16, fontweight='light')
ax.set_yticklabels(ytickslabel, fontsize=16, fontweight='light')

ax.grid(visible=True, which='major',axis='y', ls='-',lw=0.5,c='k',alpha=0.05)
ax.scatter(x,y,alpha=1.0,color='#1f77b4', s=120)

ax.set_xlabel('Log do número de policiais por $100{,}000$ habitantes',fontsize=18, fontweight='light', labelpad=10, ha='center')
ax.set_ylabel('Log de homicídios por $100{,}000$ habitantes',fontsize=18, fontweight='light', labelpad=10, ha='center')
ax.xaxis.set_label_coords(0.69,-0.09)
ax.yaxis.set_label_coords(-0.09,0.58)

plt.savefig('resultados/policia_crime.pdf', bbox_inches='tight')
plt.show()
#
#
#
#
#
#
HomicidioPolicia2015['constante'] = 1

X = HomicidioPolicia2015[['constante','police_log']]
result = sm.OLS(y,X).fit()
print(result.summary())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
