# Importa a biblioteca
import sazonal.CPTEC_SAZ as SAZ

# Inicializa o construtor
saz = SAZ.model()

# Data Condição Inicial (IC)
date = '20240401'

# Variável
var = ['prec']

# Produto
product = 'seas'

# Campo
field = 'anomalies'

# Requisição dos dados
f = saz.load(date=date, var=var, product=product ,field=field)

# Salvar o XArray para NetCDF
f.to_netcdf('arquivo.nc')

quit()
