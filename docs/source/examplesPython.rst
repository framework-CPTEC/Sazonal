Exemplos Python
===============

.. warning::
   Alterar para os valores exibidos na inicialização.

   Inicialização comando:
   sub = SUB.model()

  
.. note::
   **#### The Brazilian Global Atmospheric Model (TQ0666L064 / Hybrid) #####**
   
   **Forecast data available for reading.**

   2023-01-04 - 2023-01-11 - 2023-01-18 - 2023-01-25 - 2023-02-01
   2023-02-08 - 2023-02-15 - 2023-02-22 - 2023-03-01 - 2023-03-08
   2023-03-15 - 2023-03-22 - 2023-03-29 - 2023-04-05 - 2023-04-12
   2023-04-19 - 2023-04-26 - 2023-05-03 - 2023-05-10 - 2023-05-17
   2023-05-24 - 2023-05-31 - 2023-06-07 - 2023-06-14 - 2023-06-21
   2023-06-28 - 2023-07-05 - 2023-07-12 - 2023-07-19 - 2023-07-26
   2023-08-02 - 2023-08-09 - 2023-08-16 - 2023-08-23 - 2023-08-30
   2023-09-06 - 2023-09-13 - 2023-09-20 - 2023-09-27 - 2023-10-04
   2023-10-11 - 2023-10-18 - 2023-10-25 - 2023-11-01 - 2023-11-08
   2023-11-15 - 2023-11-22 - 2023-11-29 - 2023-12-06 - 2023-12-13
   2023-12-20 - 2023-12-27 - 2024-01-03 - 2024-01-10 - 2024-01-17
   2024-01-24 - 2024-01-31 - 2024-02-07 - 2024-02-14 - 2024-02-21
   
   **Variables:** {'prec', 'prec_ca', 't2mt', 't2mt_ca', 'psnm', 'role', 'tp85',
   'zg50', 'uv85', 'uv20', 'vv85', 'vv20', 'cr85', 'cr20'}
   
   **Products:** {'week', 'fort', '3wks', 'mnth'}
  
   **Field:** {'anomalies', 'prob_positve_anomaly', 'prob_terciles', 'totals'}
  
  

Recuperar Dados de Modelos Numéricos
------------------------------------
.. code-block:: console

  # Importa a ferramenta
  import subsaz.CPTEC_SUB as SUB
  
  # Inicializa o construtor
  sub = SUB.model()

  # Data Condição Inicial (IC)
  date = '20230104'

  # variavel
  var = 'prec'

  # produto
  product = 'week'

  # campo
  field = 'anomalies'

  # passo depende do produto escolhido
  step = '01'

  # Requisição dos dados
  f = sub.load(date=date, var=var, step=step, product=product ,field=field)

  quit()

Download :download:`get_data_sub_oper.py <examples/get_data_sub_oper.py>`.


