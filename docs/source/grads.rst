NetCDF do GrADS
===============

O Grid Analysis and Display System – **GrADS** (http://cola.gmu.edu/grads/) é uma ferramenta interativa utilizada para acessar, manipular e visualizar dados científicos. Ele trabalha com matrizes de dados nos formatos BINÁRIO, GRIB, NetCDF e HDF-SDS.

Recuperar os Dados e Salvar um arquivo NetCDF utilizando o exemplo **Recuperar Dados e Salvar em NetCDF** em :doc:`Exemplos Python <examplesPython>`.

Utilizar o Climate Data Operators (https://code.mpimet.mpg.de/projects/cdo) para a geração do arquivo ctl com a saída NetCDF do script do Recuperar Dados e Salvar em NetCDF.

.. code-block:: console

  cdo gradsdes arquivo.nc

Após o comando será gerado o arquivo.ctl na mesma pasta de trabalho.

Executar o Grads:

.. code-block:: console

  grads

Dentro do Grads:

.. code-block:: console

  open arquivo.ctl

	














