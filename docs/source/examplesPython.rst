Exemplos Python
===============

.. warning::
  Alterar a data para os valores exibidos na inicialização
  
.. note::

  **Definição de Steps**
  
  steps = **<int>**
  
  Define o número de steps que serão pedidos
  
  Ex. steps = ``6``
  
  O pedido será os steps ``0,1,2,3,4,5,6``
  
  steps = **<list>**
  
  Define os steps que serão pedidos
  
  Ex. steps =  ``[0,2,4,6]``
  
  O pedido será os steps específicos pedidos ``0,2,4,6``
  

Recuperar Dados de Modelos Numéricos
------------------------------------
.. code-block:: console

  # Importa a ferramenta
  import cptecmodel.CPTEC_BAM as BAM
  
  # Inicializa o construtor
  bam = BAM.model()

  # Data Condição Inicial (IC)
  date = '2022111800'

  # variaveis
  vars = ['t2m', 'u', 'omega']

  # Quantos passos previstos após inicialização do modelo
  steps = 5

  # Niveis desejados (aplicado apenas as variaveis em niveis)
  levels = [1000, 850]

  # Para ativar a função de escrita em disco com uma copia da resição basta alterar a função save_netcdf para True
  bam.dict['save_netcdf'] = True

  # # Diretorio onde serão salvas as requisições
  # # Por padrão, quando não aterado, um diretorio chamado INPE será criado na pasta corrente do usuario

  # bam.dict['path_to_save'] = '/home/framework/modelos'

  # Requisição dos dados
  f = bam.load(date=date, var=vars, level=levels, steps=steps)

  # Um diretorio BAM será criado no diretorio corrente, no caso apresentado os dados serão salvos em:
  # INPE/BAM/TQ0666L064/brutos/hibrido/2022/11/18/00/GPOSNMC20220818002022081906P.fct.TQ0666L064.nc4

  quit()

Download :download:`get_data_oper.py <examples/get_data_oper.py>`.

Recuperar Dados e Salvar em NetCDF
-----------------------------------
.. code-block:: console

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

Download :download:`get_netcdf.py <examples/get_netcdf.py>`.

Recuperar Dados e Plotar Figuras
---------------------------------
.. code-block:: console

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


Download :download:`plot_figure.py <examples/plot_figure.py>`.
