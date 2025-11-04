Implied Multiplication
======================

Symbolic supports implied multiplication (also known as implicit multiplication or juxtaposition) for mathematical expressions, following standard mathematical notation.

Overview
--------

Implied multiplication allows you to write mathematical expressions in a more natural, mathematical notation by omitting the explicit multiplication operator (``*``) in certain contexts.

Basic Usage
-----------

.. code-block:: symbolic

   2x              # Equivalent to 2 * x
   3y              # Equivalent to 3 * y
   2(x + 1)        # Equivalent to 2 * (x + 1)
   x(y + z)        # Equivalent to x * (y + z)

Important Note on Multiple Variables
------------------------------------

When multiple variables appear together without operators, they are treated as a single identifier:

.. code-block:: symbolic

   xy              # Treated as single variable "xy", NOT x * y
   2xy             # Treated as 2 * xy (where xy is a single variable)

For multiple variable multiplication, use explicit operators or spacing:

.. code-block:: symbolic

   2x y            # Equivalent to 2 * x * y
   2 x y           # Equivalent to 2 * x * y  
   x * y           # Explicit multiplication (recommended)
   2 * x * y       # Fully explicit (clearest)

Rules and Constraints
---------------------

The parser applies implied multiplication when:

1. **Number followed by identifier/variable**:

   .. code-block:: symbolic

      2x            # Valid: 2 * x
      3.14y         # Valid: 3.14 * y

2. **Number followed by parenthesized expression**:

   .. code-block:: symbolic

      2(x + 1)      # Valid: 2 * (x + 1)
      3(5 + 2)      # Valid: 3 * (5 + 2)

3. **Identifier followed by parenthesized expression**:

   .. code-block:: symbolic

      x(y + z)      # Valid: x * (y + z)

Constraints
-----------

Implied multiplication is **not** applied in these cases:

1. **Between two identifiers** (they form a single variable name):

   .. code-block:: symbolic

      xy            # Single variable "xy"
      ab            # Single variable "ab"

2. **Between two numbers**:

   .. code-block:: symbolic

      2 3           # Invalid: this is a syntax error, not 2 * 3

3. **When it would create ambiguity with function calls**:

   .. code-block:: symbolic

      f(x)          # Always a function call, never f * x
      sin(x)        # Always trigonometric function, never sin * x

Examples from Mathematical Contexts
-----------------------------------

Polynomial Expressions
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Polynomial: 2x² + 3x + 1
   polynomial = 2x^2 + 3x + 1
   
   # Use explicit multiplication for multiple variables
   area = length * width          # Good: explicit
   area = length width            # Invalid: treated as single variable
   volume = 2x y z                # Good: 2 * x * y * z

Mathematical Formulas
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Area of circle: πr²
   area = pi r^2                  # Good: pi * r^2
   
   # Linear equation: y = mx + b
   y = m x + b                    # Good: m * x + b
   
   # Quadratic formula components
   discriminant = b^2 - 4 a c     # Good: b^2 - 4 * a * c

Best Practices
--------------

1. **Use for single variable multiplication**: Implied multiplication works well for coefficients

2. **Use explicit operators for multiple variables**: Always use ``*`` when multiplying multiple variables

3. **Use spacing for clarity**: ``2x y`` is clearer than potentially ambiguous expressions

4. **Use parentheses for complex expressions**: When in doubt, use parentheses to clarify grouping

.. code-block:: symbolic

   # Recommended styles
   area = length * width                    # Explicit
   circumference = 2 pi radius             # Implied with constant
   polynomial = 3x^2 + 2x y + y^2          # Mixed: 3*x^2 + 2*x*y + y^2
   volume = 2 * x * y * z                  # Fully explicit (safest)

This feature makes Symbolic particularly well-suited for mathematical and scientific programming where traditional mathematical notation is expected, while maintaining clarity through explicit operators for multiple variables.