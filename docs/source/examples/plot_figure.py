# Importa a ferramenta
import cptecmodel.CPTEC_ETA as ETA
import matplotlib.pyplot as plt

# Inicializa o construtor
eta = ETA.model()

# Data condição inicial (IC)
date = '2022111800'

# variaveis
vars = ['u10m']

# Quantos passos previstos após inicialização do modelo
steps = 5

# O resultado da requisição dos dados são armazenados na variavel f
f = eta.load(date=date, var=vars, steps=steps)

# Para verificar as datas disponiveis, latitudes, longitudes e niveis quando presente use o exemplo abaixo
print('Horarios disponiveis:', f.time.values, '\n')
print('Latitude :', f.latitude.values, '\n')
print('Longitude:', f.longitude.values, '\n')
# print('Level:', f.level)

# Plot simples para verificação dos campos
# selecionando apenas por tempo

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
f.sel(time='20221118T01:00').u10m.plot.pcolormesh(
          ax=axes, robust=True, add_colorbar=True, add_labels=True)
axes.set_title('Eta 2022-11-18T01:00 U10M', ha='center')
plt.show()

# Plot simples dando zoom em area
# selecionando apenas por tempo
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))

f.sel(time='20221118T01:00', latitude=slice(-30,5), longitude=slice(280, 300)).u10m.plot.pcolormesh(
          ax=axes, robust=True, add_colorbar=True, add_labels=True)

axes.set_title('Eta 2022-11-18T01:00 U10M', ha='center')

plt.show()

quit()
