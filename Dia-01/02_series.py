#%%



media = sum(idades) / len(idades)


#%%
import pandas as pd

idades = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


series_idades = pd.Series(idades)
series_idades


#Estatisticas basicas da serie
series_idades.mean()
summary_idades = series_idades.describe()
summary_idades


# %%
