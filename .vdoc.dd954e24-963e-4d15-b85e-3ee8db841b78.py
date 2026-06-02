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
#| message: false
#| warning: false

import os
import pathlib
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
#
#
#
## homicides
df_hrate = pd.read_excel('dados/original/UNDOC CTS - Homicides.xlsx',sheet_name='data_cts_intentional_homicide')
df_hrate = df_hrate.loc[(df_hrate['Indicator']=='Victims of intentional homicide') & 
                        (df_hrate['Dimension']=='Total') & 
                        (df_hrate['Category']=='Total') & 
                        (df_hrate['Sex']=='Total') & 
                        (df_hrate['Age']=='Total') & 
                        (df_hrate['Year']==2015) & 
                        (df_hrate['Unit of measurement']=='Rate per 100,000 population')]

df_hrate = df_hrate[['Iso3_code','Country','VALUE']].reset_index(drop=True)
df_hrate.columns = ['country_code','country_name','hrate']

## police personnel
df_pol = pd.read_excel('UNDOC CTS - Police.xlsx',sheet_name='data_cts_access_and_functioning')
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
df_polh = df_polh.dropna(how='any',axis=0)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
