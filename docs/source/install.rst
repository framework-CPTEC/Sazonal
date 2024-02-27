Instalação
==========

- Criar ambiente conda

.. code-block:: console

  conda create -n cptec python=3.10

  conda activate cptec

**Via conda**
  
.. code-block:: console

  conda install -c conda-forge  cptec-model
  

**Via pip**
  
.. code-block:: console

  pip install cptec-model
  
**Via fonte**

- Instalar Pacotes Requeridos

.. code-block:: console

  conda install -c conda-forge matplotlib pycurl cfgrib netCDF4 pynio xarray dask esmpy scipy mpi4py xesmf ipykernel

- Instalar Pacote cptec-model

.. code-block:: console
 
  git clone https://github.com/framework-CPTEC/CPTEC-user.git

  cd CPTEC-user

  python setup.py install

Erros Encontrados
=================

- EcCodes

.. code-block:: console

  Engine 'cfgrib' loading failed:
  Could not load the ecCodes library!

Ação

.. code-block:: console

  python -m eccodes selfcheck
  RuntimeError: Could not load the ecCodes library!

  pip uninstall eccodes

  pip install eccodes==1.2.0

  python -m eccodes selfcheck
  ecCodes library not found using ['eccodes', 'libeccodes.so', 'libeccodes']

  pip install ecmwflibs

  python -m eccodes selfcheck
  Found: ecCodes v2.30.0.
  Your system is ready.

- PyNio

.. code-block:: console

  Unexpected err=ValueError("unrecognized engine pynio must be one of: ['netcdf4', 'scipy', 
  'cfgrib', 'store']"), type(err)=<class 'ValueError'>

Ação

.. code-block:: console

  conda install -c conda-forge pynio

- PyCurl

.. code-block:: console

  import pycurl
  ImportError: pycurl: libcurl link-time ssl backends (secure-transport, openssl) 
  do not include compile-time ssl backend (none/other)

Ação

.. code-block:: console

  1 - pip uninstall pycurl 
  2 - conda install -c conda-forge  pycurl   


Caso o erro persista, verifique o link para maiores detalhes:
`<http://pycurl.io/docs/7.21.5/install.html#ssl>`_.
