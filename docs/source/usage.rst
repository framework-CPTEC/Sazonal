Como Usar
=========

Modelos Disponíveis
-------------------

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Modelo
     - import
   * - BAM
     - import cptecmodel.CPTEC_BAM as BAM
   * - Eta
     - import cptecmodel.CPTEC_ETA as ETA
   * - GFS
     - import cptecmodel.CPTEC_GFS as GFS
   * - WRF
     - import cptecmodel.CPTEC_WRF as WRF
   * - BRAMS
     - import cptecmodel.CPTEC_BRAMS as BRAMS

.. list-table::  Outros Pacotes
   :widths: 30 70
   :header-rows: 0

   * - CPTEC_UTIL
     - Funções para uso nos diversos modelos 
   * - CPTEC_Widgets
     - Funções para uso no sistema interativo

Utilizando o BAM

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

.. code-block:: console

  # Import para os modelos disponiveis
  # CPTEC_BAM, CPTEC_WRF, CPTEC_ETA, CPTEC_GFS
  import cptecmodel.CPTEC_BAM as BAM

  # Durante a inicialização do construtor informações sobre os dados são exibidas
  # Entre elas informações de variaveis, niveis e frequência disponiveis para consulta

  bam = BAM.model()

  # Data da IC
  date = '2023011700'

  # Variaveis 
  vars = ['t']

  # Niveis
  levels = [1000]

  # Steps = Numero de simulações futuras a partir da inicialização do modelo
  steps = 1

  # Utizando o método load
  f = bam.load(date=date, var=vars,level=levels, steps=steps)
  
  # Imprimir os valores recuperados
  print(f)

Observações
-----------

Após a inicialização do Modelo Específico algumas configurações são plotadas.

Exemplo do BAM

The Brazilian Global Atmospheric Model (TQ0666L064 / Hybrid)

Forecast data available for reading between 20221211 and 20221221.

Surface variables: t2m, u10m, v10m, slp, psfc, precip terrain, sbcape, sbcin, pw. Level variables: t, u, v, rh, g, omega.

levels (hPa): 1000 925 850 775 700 500 400 300 250 200 150 100 70 50 30 20 10 3.

Frequency: every 6 hours [0, 6, 12, 18,...,168].

.. warning::

  Usar essas informações da inicialização na definição dos valores das variáveis (date,vars,levels,steps)



