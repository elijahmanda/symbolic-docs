Mathematics Domain: Variables
=============================

The mathematics domain provides specialized syntax for variable declarations and management.

@$var - Single Variable Declaration
-----------------------------------

Declares a single mathematical variable.

Syntax
~~~~~~

.. code-block:: symbolic

   @$var name

Examples
~~~~~~~~

.. code-block:: symbolic

   @$var x
   @$var y
   @$var theta

@$vars - Multiple Variable Declaration
--------------------------------------

Declares multiple mathematical variables in a single statement.

Syntax
~~~~~~

.. code-block:: symbolic

   @$vars var1, var2, var3, ...;

Examples
~~~~~~~~

.. code-block:: symbolic

   @$vars x, y, z;
   @$vars a, b, c, d;
   @$vars u, v, w;

Usage Context
-------------

Variable declarations are typically used at the beginning of mathematical blocks:

.. code-block:: symbolic

   @$domain math {
       @$vars x, y, z;
       @$equ x + y = z;
       @$equ x^2 + y^2 = z^2;
   }

Integration with Core Language
------------------------------

Mathematics domain variables integrate with the core language:

.. code-block:: symbolic

   @$domain math {
       @$var x
       @$var y
   }
   
   # Can be used in regular expressions
   result = x + y
   fn calculate(a, b) = a * x + b * y

Variable Scope
--------------

Variables declared with ``@$var`` and ``@$vars`` have the same scoping rules as regular Symbolic variables:

* **Block Scope**: Variables are scoped to their containing block
* **Mathematical Context**: They represent mathematical variables rather than program variables
* **Type Inference**: Variables can hold any mathematical value (numbers, expressions, etc.)

Examples from .sym Files
------------------------

The provided .sym files demonstrate mathematical variable usage:

Vector Components
~~~~~~~~~~~~~~~~~

From ``vector.sym``:

.. code-block:: symbolic

   class Vector {
       fn __init__(self, components: [Integer || Float]) {
           self.components = components.map((x) => Float(x))
           self.dimension = components.length()
       }
   }

Integration Variables
~~~~~~~~~~~~~~~~~~~~~

From ``integration.sym`` and ``differentiation.sym``:

.. code-block:: symbolic

   fn derivative(f, x: Integer || Float, h: Float = 1e-8) -> Float {
       return (f(x + h) - f(x - h)) / (2 * h)
   }
   
   fn gradient(f, x: [Integer || Float], h: Float = 1e-8) -> [Float] {
       grad = []
       for i in 0..<x.length() {
           # x is used as the variable for differentiation
       }
   }

Best Practices
--------------

1. **Declare at block start**: Place variable declarations at the beginning of mathematical blocks

2. **Use descriptive names**: Choose names that reflect mathematical meaning (e.g., ``theta`` for angles)

3. **Group related variables**: Use ``@$vars`` for related variables (e.g., coordinate axes)

4. **Combine with equations**: Follow variable declarations with equation definitions

Variable declarations form the foundation for mathematical expressions and equations in the mathematics domain.