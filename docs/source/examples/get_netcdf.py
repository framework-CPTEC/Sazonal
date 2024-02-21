# Importa a ferramenta
import cptecmodel.CPTEC_WRF as WRF

# Inicializa o construtor
wrf = WRF.model()

# Data Condição Inicial (IC)
date = '2022111800'

# variaveis
vars = ['t', 'precip']

# Quantos passos previstos após inicialização do modelo
steps = 5

# Niveis desejados (aplicado apenas as variaveis em niveis)
levels = [1000, 850]

# Requisição dos dados
f = wrf.load(date=date, var=vars, level=levels, steps=steps)

# Salva arquivo com os dados solicitados
f.to_netcdf('wrf_2022111800.nc')

quit()
