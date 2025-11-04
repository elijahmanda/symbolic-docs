Mathematics Domain: Calculus
============================

The mathematics domain provides comprehensive support for calculus operations including derivatives, integrals, and limits.

@$d - Derivatives
-----------------

Computes derivatives of functions with support for partial and higher-order derivatives.

Syntax
~~~~~~

Basic Derivative:

.. code-block:: symbolic

   @$d/dx expression

Higher-order Derivative:

.. code-block:: symbolic

   @$d^n/dx^n expression

Mixed Partial Derivatives:

.. code-block:: symbolic

   @$d^{order}/{dx^m, dy^n} expression

Examples
~~~~~~~~

.. code-block:: symbolic

   @$d/dx sin(x)                    # Basic derivative: cos(x)
   @$d^2/dx^2 x^3                   # Second derivative: 6x
   @$d/dx (x^2 * y^3)               # Partial derivative w.r.t x: 2x * y^3
   @$d^{2}/{dx^2, dy} (x^2 * y^3)   # Mixed partial: 12x * y^2

@$integral - Integration
------------------------

Computes definite and indefinite integrals.

Syntax
~~~~~~

Indefinite Integral:

.. code-block:: symbolic

   @$integral expression, dx

Definite Integral:

.. code-block:: symbolic

   @$integral [var=a to b] expression, dx

Examples
~~~~~~~~

.. code-block:: symbolic

   @$integral x^2, dx                # Indefinite: (1/3)x^3 + C
   @$integral [x=0 to 1] x^2, dx     # Definite: 1/3
   @$integral [theta=0 to pi] sin(theta), dtheta  # Definite: 2

@$lim - Limits
---------------

Computes limits of functions as variables approach specific values.

Syntax
~~~~~~

.. code-block:: symbolic

   @$lim {var -> point} expression
   @$lim {var -> point+} expression   # Right-hand limit
   @$lim {var -> point-} expression   # Left-hand limit

Examples
~~~~~~~~

.. code-block:: symbolic

   @$lim {x -> 0} sin(x)/x           # Famous limit: 1
   @$lim {x -> 0+} 1/x               # Right-hand limit: +∞
   @$lim {x -> 0-} 1/x               # Left-hand limit: -∞
   @$lim {x -> inf} (1 + 1/x)^x      # Limit definition of e: e

Numerical Methods
-----------------

The provided .sym files include numerical implementations:

Numerical Differentiation
~~~~~~~~~~~~~~~~~~~~~~~~~

From ``differentiation.sym``:

.. code-block:: symbolic

   fn derivative(f, x: Integer || Float, h: Float = 1e-8) -> Float {
       /**
        * Compute numerical derivative using central difference
        * f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
        */
       return (f(x + h) - f(x - h)) / (2 * h)
   }

   fn gradient(f, x: [Integer || Float], h: Float = 1e-8) -> [Float] {
       /**
        * Compute numerical gradient of multivariable function
        * Returns vector of partial derivatives
        */
       grad = []
       for i in 0..<x.length() {
           x_plus = x.copy()
           x_minus = x.copy()
           x_plus[i] += h
           x_minus[i] -= h
           
           partial_deriv = (f(x_plus) - f(x_minus)) / (2 * h)
           grad.append(partial_deriv)
       }
       return grad
   }

Numerical Integration
~~~~~~~~~~~~~~~~~~~~~

From ``integration.sym``:

.. code-block:: symbolic

   fn trapezoid(f, a: Integer || Float, b: Integer || Float, n = 1000) -> Float {
       /**
        * Numerical integration using trapezoidal rule
        */
       h = (b - a) / n
       result = (f(a) + f(b)) / 2.0
       
       for i = 1, i < n, 1 {
           x = a + i * h
           result += f(x)
       }
       
       return result * h
   }

   fn simpson(f, a: Integer || Float, b: Integer || Float, n = 1000) -> Float {
       /**
        * Numerical integration using Simpson's rule
        * n must be even
        */
       if n % 2 != 0 {
           n += 1  # Make n even
       }
       
       h = (b - a) / n
       result = f(a) + f(b)
       
       for i = 1, i < n, 2 {
           x = a + i * h
           result += 4 * f(x)
       }
       
       for i = 2, i < n, 2 {
           x = a + i * h
           result += 2 * f(x)
       }
       
       return result * h / 3.0
   }

Advanced Calculus
-----------------

Multiple Integration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Double integral
   @$integral [x=a to b] (@$integral [y=c to d] f(x,y), dy), dx
   
   # Triple integral  
   @$integral [x=a to b] (@$integral [y=c to d] (@$integral [z=e to f] f(x,y,z), dz), dy), dx

Line Integrals
~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Scalar line integral
   @$integral_C f(x,y) ds
   
   # Vector line integral
   @$integral_C F · dr

Surface Integrals
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Surface integral
   @$integral_S f(x,y,z) dS
   
   # Flux integral
   @$integral_S F · n dS

Practical Examples
------------------

Physics Applications
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Velocity from acceleration
   velocity = @$integral [t=0 to T] acceleration(t), dt
   
   # Work as line integral of force
   work = @$integral_C F · dr

Engineering Applications
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Area under curve
   area = @$integral [x=a to b] f(x), dx
   
   # Volume of revolution
   volume = @$integral [x=a to b] pi * f(x)^2, dx

Economics Applications
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Marginal cost from total cost
   marginal_cost = @$d/dx total_cost(x)
   
   # Consumer surplus
   surplus = @$integral [q=0 to Q] (demand_price(q) - market_price), dq

The calculus support in Symbolic's mathematics domain provides both symbolic and numerical approaches, making it suitable for educational, scientific, and engineering applications.