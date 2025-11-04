Arithmetic Operators
====================

Basic arithmetic operators for mathematical computations.

Addition (+)
------------

.. code-block:: symbolic

   # Number addition
   sum = 5 + 3;           # 8
   total = 2.5 + 1.75;    # 4.25
   
   # String concatenation
   greeting = "Hello" + " " + "World";  # "Hello World"
   
   # List concatenation
   combined = [1, 2] + [3, 4];          # [1, 2, 3, 4]
   
   # Complex number addition
   complex_sum = (2 + 3i) + (1 + 2i);   # 3 + 5i

Subtraction (-)
---------------

.. code-block:: symbolic

   # Number subtraction
   difference = 10 - 4;        # 6
   negative = 5 - 10;          # -5
   
   # Floating point subtraction
   result = 7.5 - 2.25;        # 5.25
   
   # Complex number subtraction
   complex_diff = (5 + 4i) - (2 + 1i);  # 3 + 3i
   
   # Set difference
   set_a = {1, 2, 3, 4};
   set_b = {3, 4, 5, 6};
   set_diff = set_a - set_b;    # {1, 2}

Multiplication (*)
------------------

.. code-block:: symbolic

   # Number multiplication
   product = 6 * 7;           # 42
   area = 5.5 * 3.2;          # 17.6
   
   # String repetition
   stars = "*" * 10;          # "**********"
   pattern = "abc" * 3;       # "abcabcabc"
   
   # List repetition
   repeated = [1, 2] * 3;     # [1, 2, 1, 2, 1, 2]
   
   # Complex multiplication
   complex_prod = (2 + 3i) * (1 + 2i);  # -4 + 7i

Division (/)
------------

.. code-block:: symbolic

   # True division
   quotient = 10 / 3;         # 3.333...
   result = 7.5 / 2.5;        # 3.0
   
   # Complex division
   complex_quotient = (6 + 8i) / (2 + 2i);  # 3.5 + 0.5i
   
   # Division by zero
   try {
       invalid = 5 / 0;
   } catch e {
       print("Division by zero error");
   }

Floor Division (//)
-------------------

.. code-block:: symbolic

   # Integer division
   whole = 10 // 3;           # 3
   negative = -10 // 3;       # -4 (rounds toward -∞)
   
   # Floating point floor division
   result = 7.8 // 2.5;       # 3.0
   result2 = -7.8 // 2.5;     # -4.0

Modulo (%)
----------

.. code-block:: symbolic

   # Remainder division
   remainder = 10 % 3;        # 1
   even_check = 15 % 2;       # 1 (odd)
   
   # Floating point modulo
   result = 7.5 % 2.5;        # 0.0
   result2 = 7.8 % 2.5;       # 0.3
   
   # String formatting
   message = "Value: %d" % 42;  # "Value: 42"
   formatted = "%.2f" % 3.14159; # "3.14"

Exponentiation (^)
------------------

.. code-block:: symbolic

   # Number exponentiation
   square = 5 ^ 2;            # 25
   cube = 2 ^ 3;              # 8
   
   # Fractional exponents
   sqrt = 16 ^ 0.5;           # 4.0
   cube_root = 27 ^ (1/3);    # 3.0
   
   # Negative exponents
   reciprocal = 2 ^ -1;       # 0.5
   
   # Complex exponents
   complex_power = (1 + 1i) ^ 2;  # 2i

Unary Plus and Minus
--------------------

.. code-block:: symbolic

   # Unary plus (mostly for symmetry)
   positive = +5;             # 5
   positive_float = +3.14;    # 3.14
   
   # Unary minus (negation)
   negative = -10;            # -10
   negative_float = -2.5;     # -2.5
   negative_complex = -(3 + 4i);  # -3 - 4i

Compound Assignment Operators
-----------------------------

.. code-block:: symbolic

   x = 10;
   
   # Addition assignment
   x += 5;        # x = 15
   
   # Subtraction assignment  
   x -= 3;        # x = 12
   
   # Multiplication assignment
   x *= 2;        # x = 24
   
   # Division assignment
   x /= 4;        # x = 6.0
   
   # Floor division assignment
   x //= 2;       # x = 3
   
   # Modulo assignment
   x %= 2;        # x = 1
   
   # Exponentiation assignment
   x ^= 3;        # x = 1

Practical Examples
------------------

Financial Calculations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_compound_interest(principal, rate, years) {
       amount = principal * (1 + rate) ^ years;
       interest = amount - principal;
       return (amount, interest);
   }
   
   fn calculate_monthly_payment(principal, annual_rate, years) {
       monthly_rate = annual_rate / 12;
       periods = years * 12;
       
       # PMT formula
       payment = principal * monthly_rate * (1 + monthly_rate) ^ periods;
       payment /= (1 + monthly_rate) ^ periods - 1;
       
       return payment;
   }

Geometry Calculations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn circle_properties(radius) {
       area = π * radius ^ 2;
       circumference = 2 * π * radius;
       return (area, circumference);
   }
   
   fn distance_between_points(x1, y1, x2, y2) {
       dx = x2 - x1;
       dy = y2 - y1;
       return (dx ^ 2 + dy ^ 2) ^ 0.5;
   }

Statistical Calculations
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_variance(numbers) {
       mean = numbers.sum() / numbers.length();
       squared_differences = numbers.map(x => (x - mean) ^ 2);
       return squared_differences.sum() / (numbers.length() - 1);
   }
   
   fn normalize_data(data) {
       min_val = data.min();
       max_val = data.max();
       range = max_val - min_val;
       
       return data.map(x => (x - min_val) / range);
   }

Physics Calculations
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_kinetic_energy(mass, velocity) {
       return 0.5 * mass * velocity ^ 2;
   }
   
   fn calculate_gravitational_force(m1, m2, distance) {
       G = 6.674