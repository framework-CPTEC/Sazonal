Como Usar
=========

Import
------

import sazonal.CPTEC_SAZ as SAZ

Inicialização
-------------

Ex. de Pedido
Durante a inicialização do construtor informações sobre os dados são exibidas

saz = SAZ.model()


Pedido
------

Data
----

date= '20240201'

.. warning::
  Alterar a data para os valores exibidos na inicialização

Variaveis
---------
Uma única variável

var = ['prec']

Lista de variáveis

var = ['prec','t2mt']


**Lista de variáveis disponíveis:**

- prec -> precipitação
- t2mt -> temperatura de 2 metros
- psnm -> pressão ao nível do mar
- role -> radiação de onda longa de saída
- tp85 -> temperatura a 850 hPa
- gz50 -> altura geopotencial em 500 hPa
- uv85 -> vento zonal a 850 hPa
- uv20 -> vento zonal a 200 hPa
- vv85 -> vento meridional a 850 hPa
- vv20 -> vento meridional a 200 hPa

Arquivos de dados de previsão calibrados são gerados para valores totais de temperatura e precipitação de 2 metros, probabilidade do tercil mais provável, probabilidade de anomalia positiva e anomalias.

- prec_ca -> precipitação calibrada
- t2mt_ca -> temperatura de 2 metros calibrada


Produto
-------

product = 'mnth'

**Lista de produtos disponíveis:**

- seas -> média ou acúmulo de 3 meses, para os períodos 01 e 02
- mnth -> média ou acúmulo de 30 dias, para os meses 01, 02, 03 e 04

Campo
-----

field='anomalies'

**Lista de campos calibrados determinísticos e probabilísticos disponíveis:**

- anomalies -> anomalias de previsão
- prob_positive_anomaly  -> probabilidade de previsão de anomalia positiva
- prob_terciles -> probabilidade de previsão do tercil mais provável
- totals -> valor total previsto


Steps = Número da figura disponível por produto.
------------------------------------------------

step = '01'

A opção pode ser omitida e trará todos os tempos do produto.

- seas -> dado médio de 3 meses ou acumulação (01 e 02)
- mnth -> dado médio ou acúmulo de 30 dias (01, 02, 03 e 04)


Exemplo de solicitação do Pedido
--------------------------------

f = saz.load(date='20240201', var='prec', product='mnth',field='anomalies')


