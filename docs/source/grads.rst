NetCDF do GrADS
===============

O Grid Analysis and Display System – GrADS  (http://cola.gmu.edu/grads/) é uma ferramenta interativa utilizada para acessar, manipular e visualizar dados científicos. Ele trabalha com matrizes de dados nos formatos BINÁRIO, GRIB, NetCDF e HDF-SDS.

Utilizando o exemplo {ref}`Recuperar Dados e Salvar em NetCDF`. Recuperar Dados e Salvar em NetCDF um  arquivo NetCDF sera gerado no diretorio local de seu computador.

Utilizar o Climate Data Operators (https://code.mpimet.mpg.de/projects/cdo) para a geracao de um arquivo ctl para o GrADS.

.. code-block:: console

  cdo gradsdes arquivo.nc

Após o  comando será gerado o arquivo.ctl na mesma pasta de trabalho.







