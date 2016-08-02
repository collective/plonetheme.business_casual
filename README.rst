.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
Business Casual
==============================================================================

Business Casual is a full website template for Plone.

.. image:: https://raw.githubusercontent.com/vikas-parashar/plonetheme.business_casual/master/preview.png

Installation
------------

Zip
~~~~~~~~
In zip version you don't get the slider but only a static banner due to limitations.

#. Download the `zip file`_
#. Import the theme from the Diazo theme control panel.

Buildout
~~~~~~~~

Install ``plonetheme.business_casual`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plonetheme.business_casual


and then running ``bin/buildout``


Demo
~~~~

   This theme can be seen in action at the following site:

-  `Business Casual Theme Demo`_

Documentation
-------------

Full documentation for end users can be found `here`_

Contribution
-------------

- Clone the repo.
- Run ``bin/buildout``
- next, install the local dependencies theme requires
    ``$ npm install``
- Watch For Changes & Automatically Refresh
    ``$ grunt watch``
- Build & Optimize(This will create a ``dist`` folder with optimized files and a zip of theme)
    ``$ grunt dist``

License
-------

MIT License

Credit
------

Based on `Business Casual`_ Provided by `Start Bootstrap`_

.. _zip file: https://github.com/vikas-parashar/plonetheme.business_casual/blob/master/plonetheme.business_casual.zip?raw=true
.. _Business Casual Theme Demo: http://107.170.136.197:8080/business-casual
.. _Business Casual: https://startbootstrap.com/template-overviews/business-casual/
.. _Start Bootstrap: https://startbootstrap.com
.. _here: https://github.com/vikas-parashar/plonetheme.business_casual/blob/master/docs/index.rst