# CPTEC-user

[![Logo](https://github.com/framework-CPTEC/_static/blob/main/framework.png)](https://www.cptec.inpe.br/)


### Framework-CPTEC 

É um pacote in Python para a distribuição de dados brutos dos Modelos Numéricos de forma segmentada/particionada. Com esse pacote o usuário não necessita fazer o Download de todo o volume bruto o pacote auxilia a manipular somente a sua necessidade.

support Python >= 3.10.

## Inicialização

Ex. de Pedido
Durante a inicialização do construtor informações sobre os dados são exibidas

bam = BAM.model()

## Pedido
- Variaveis 
vars = ['t', 'u10m']

- Niveis
levels = [1000, 850]

- Steps = Numero de simulações futuras a partir da inicialização do modelo
steps = 1

Solicitacao do Pedido
f = bam.load(date=date, var=vars,level=levels, steps=steps)

support Python >= 3.10.

Need Help?
----------

Need help using MetPy? Found an issue? Have a feature request? Checkout our
[support page](https://github.com/Unidata/MetPy/blob/main/SUPPORT.md).

Important Links
---------------

- [HTML Documentation](http://unidata.github.io/MetPy)
- [Unidata Python Gallery](https://unidata.github.io/python-gallery/)
- "metpy" tagged questions on [Stack Overflow](https://stackoverflow.com/questions/tagged/metpy)
- [Gitter chat room](https://gitter.im/Unidata/MetPy)

Dependencies
------------

Other required packages:

- Numpy
- Scipy
- Matplotlib
- Pandas
- Pint
- Xarray

There is also an optional dependency on the pyproj library for geographic
projections (used with cross sections, grid spacing calculation, and the GiniFile interface).

See the [installation guide](https://unidata.github.io/MetPy/latest/userguide/installguide.html)
for more information.

Code of Conduct
---------------

We want everyone to feel welcome to contribute to MetPy and participate in discussions. In that
spirit please have a look at our [Code of Conduct](https://github.com/Unidata/MetPy/blob/main/CODE_OF_CONDUCT.md).

Contributing
------------

**Imposter syndrome disclaimer**: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not ready to be
an open source contributor; that your skills aren't nearly good enough to contribute. What
could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at all,
you can contribute code to open source. Contributing to open source projects is a fantastic
way to advance one's coding skills. Writing perfect code isn't the measure of a good developer
(that would disqualify all of us!); it's trying to create something, making mistakes, and
learning from those mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can help out by
writing documentation, tests, or even giving feedback about the project (and yes - that
includes giving feedback about the contribution process). Some of these contributions may be
the most valuable to the project as a whole, because you're coming to the project with fresh
eyes, so you can see the errors and assumptions that seasoned contributors have glossed over.

For more information, please read the see the [contributing guide](https://github.com/Unidata/MetPy/blob/main/CONTRIBUTING.md).

Philosophy
----------

The space MetPy aims for is GEMPAK (and maybe NCL)-like functionality, in a way that plugs
easily into the existing scientific Python ecosystem (numpy, scipy, matplotlib). So, if you
take the average GEMPAK script for a weather map, you need to:

- read data
- calculate a derived field
- show on a map/skew-T

One of the benefits hoped to achieve over GEMPAK is to make it easier to use these routines for
any meteorological Python application; this means making it easy to pull out the LCL
calculation and just use that, or re-use the Skew-T with your own data code. MetPy also prides
itself on being well-documented and well-tested, so that on-going maintenance is easily
manageable.

The intended audience is that of GEMPAK: researchers, educators, and any one wanting to script
up weather analysis. It doesn't even have to be scripting; all python meteorology tools are
hoped to be able to benefit from MetPy. Conversely, it's hoped to be the meteorological
equivalent of the audience of scipy/scikit-learn/skimage.
