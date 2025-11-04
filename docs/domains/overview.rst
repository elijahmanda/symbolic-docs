Domain System Overview
======================

Symbolic features a pluggable domain architecture that allows specialized syntax and constructs for different computational domains.

Architecture
------------

The domain system consists of:

* **Core Parser** (``SymbolicParser``): Handles general language syntax
* **Domain Parsers** (``DomainParser`` subclasses): Handle domain-specific constructs
* **Domain Contexts**: Scoped blocks for domain-specific code

Domain Registration
-------------------

Domains are automatically loaded and registered:

.. code-block:: python

   # In SymbolicParser.__init__()
   self._domain_parsers: Dict[str, DomainParser] = _load_domain_parsers(self)

Available Domains
-----------------

Currently Supported
~~~~~~~~~~~~~~~~~~~

* **Mathematics** (``math``): Comprehensive mathematical constructs
* **Physics** (planned): Physical units, constants, and equations
* **Chemistry** (planned): Chemical formulas and reactions  
* **Biology** (planned): Biological data and computations
* **Finance** (planned): Financial calculations and models

Domain Syntax
-------------

Domain Blocks
~~~~~~~~~~~~~

Use ``@$domain`` to enter a domain context:

.. code-block:: symbolic

   @$domain math {
       # Mathematical constructs available here
       @$integral x^2, dx
       @$vector [1, 2, 3]
   }

Domain Constructs
~~~~~~~~~~~~~~~~~

Domain-specific constructs use the ``@$`` prefix:

.. code-block:: symbolic

   @$var x              # Math domain: variable declaration
   @$equ x + y = 10     # Math domain: equation
   @$system { ... }     # Math domain: equation system

Domain Switching
~~~~~~~~~~~~~~~~

Domains can be nested and switched:

.. code-block:: symbolic

   @$domain math {
       # Math constructs
       @$integral x^2, dx
   }
   
   @$domain physics {
       # Physics constructs (planned)
       # @$unit 5 kg m/s^2
   }

Implementation
--------------

Domain Parser Base Class
~~~~~~~~~~~~~~~~~~~~~~~~

All domain parsers inherit from ``DomainParser``:

.. code-block:: python

   class DomainParser:
       name: str  # Domain identifier
       
       def parse(self, token) -> ASTNode:
           # Parse domain-specific tokens
           pass
           
       def parse_at_construct(self, name_token) -> ASTNode:
           # Parse @$ constructs
           pass

Mathematics Domain
~~~~~~~~~~~~~~~~~~

The mathematics domain (``MathParser``) provides extensive mathematical support:

.. code-block:: python

   class MathParser(DomainParser):
       name = "math"
       
       def _parse_var(self, token): ...
       def _parse_equation(self, token): ...
       def _parse_integral(self, token): ...
       def _parse_limit(self, token): ...
       # ... many more mathematical constructs

Extending with New Domains
--------------------------

Creating a new domain involves:

1. **Subclass DomainParser**:

   .. code-block:: python

      class PhysicsParser(DomainParser):
          name = "physics"
          
          def parse(self, token):
              # Handle physics-specific tokens
              pass

2. **Register the domain** (automatic via ``_load_domain_parsers``)

3. **Define domain constructs**:

   .. code-block:: python

      def _parse_unit(self, token):
          # Parse @$unit construct
          pass

Benefits
--------

* **Specialized Syntax**: Each domain can have its own natural notation
* **Context Awareness**: Parsers activate only in relevant domains
* **Extensibility**: Easy to add new domains for specialized applications
* **Integration**: Domain code integrates seamlessly with core language

Usage Examples
--------------

Mathematical Programming
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   @$domain math {
       @$vars x, y, z;
       @$equ x^2 + y^2 = z^2;  # Pythagorean theorem
       
       fn circle_area(r) = pi * r^2;
   }

Scientific Computing
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Numerical integration
   area = @$integral [x=0 to 1] x^2, dx
   
   # Limit calculation
   derivative = @$lim {h -> 0} (f(x+h) - f(x))/h

The domain system makes Symbolic exceptionally powerful for domain-specific applications while maintaining a clean, general-purpose core language.

Continue to :doc:`math/index` for detailed mathematics domain documentation.