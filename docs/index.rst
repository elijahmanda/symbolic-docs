Symbolic Language Documentation
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   introduction
   language_reference/index
   domains/index
   roadmap

Welcome to Symbolic
-------------------

Symbolic is a powerful, domain-specific programming language designed for mathematical and scientific computing with extensible domain support.

Key Features
------------

* **Pluggable Domain Architecture**: Specialized syntax for mathematics, physics, chemistry, biology, and finance
* **Rich Mathematical Support**: Built-in support for calculus, linear algebra, numerical methods, and more
* **Multi-position Token System**: Flexible operator parsing for complex mathematical expressions
* **High-precision Arithmetic**: Support for arbitrary precision numbers and complex numbers
* **Extensible Syntax**: Custom domain parsers and @$ constructs for specialized domains

Quick Start
-----------

.. code-block:: symbolic

   # Basic arithmetic with implied multiplication
   result = 2x + 3y
   
   # Function definition
   fn quadratic(a, b, c, x) = a*x^2 + b*x + c
   
   # Mathematical domain usage
   @$domain math {
       @$integral x^2, dx
       @$lim {x -> 0} sin(x)/x
   }

Getting Started
---------------

* :doc:`introduction` - Learn the basics of Symbolic
* :doc:`language_reference/index` - Complete language reference
* :doc:`domains/index` - Domain-specific features and syntax
* :doc:`roadmap` - Future development plans

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`