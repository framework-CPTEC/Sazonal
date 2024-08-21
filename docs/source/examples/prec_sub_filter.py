import sazonal.CPTEC_SAZ as SAZ
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Inicializa o construtor
saz = SAZ.model()

# Filtrar area definida
saz.dict['area']['reduce'] = True
saz.dict['area']['minlat'] = -34.44
saz.dict['area']['maxlat'] = -21.43
saz.dict['area']['minlon'] = 301.14
saz.dict['area']['maxlon'] = 320.57

# Requisição dos dados
f = saz.load(date='20240401', var='prec', product='mnth' ,field='anomalies')

# Definir tamanho da figura
fig = plt.figure(figsize=(10,8))

# Setar figura unica
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

# Colocar  Linhas de Borda dos paises e linhas costeiras
ax.add_feature(cfeature.COASTLINE,color='grey')
ax.add_feature(cfeature.BORDERS,color='grey')

# Definir Regiao do Brasil
ax.set_extent([-90,-30,10,-41], ccrs.PlateCarree())

# Setar estados do Brasil
states = cfeature.NaturalEarthFeature(category='cultural',
                                         name='admin_1_states_provinces_lines',
                                         scale='50m', facecolor='none')
# Colocar Estados Brasil
ax.add_feature(states, edgecolor='gray')

# Plotar variavel
f.prec.sel(time="2024-04-01").plot()
plt.show()

