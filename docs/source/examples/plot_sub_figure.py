# Importa a ferramenta
import sazonal.CPTEC_SAZ as SAZ
import matplotlib.pyplot as plt

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

# Plotar a variável prec
f.prec.sel(time="2024-04-01").plot()
plt.show()

quit()
