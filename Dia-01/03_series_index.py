#%%

import pandas as pd

idades = [10, 20,90, 30, 40, 50, 60, 70, 80,  100]

series_idades = pd.Series(idades)
series_idades


#%%

#Pega o primeiro e o ultimo elemento da lista
idades[0]
idades[-1]


#Pega o primeiro e o ultimo elemento da serie
series_idades[0]


#%%

series_idades = series_idades.sort_values()
series_idades


#%%

series_idades[0]


#%%
series_idades.iloc[-1]


# %%
series_idades.iloc[:3]

#%%
series_idades.iloc[::-1]

# %%
idades = [10, 20,90, 30, 40, 50, 60, 70, 80,  100]

index = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'setimo', 'oitavo', 'nono', 'decimo']

series_idades = pd.Series(idades, index=index)
series_idades