Numbers
=======

Symbolic provides a comprehensive numeric system supporting integers, floats, complex numbers, and arbitrary precision arithmetic.

Number Types
------------

Integers
~~~~~~~~

Arbitrary precision integers:

.. code-block:: symbolic

   small = 42;
   large = 123456789012345678901234567890;
   negative = -15;
   
   # Different bases
   binary = 0b1010;      # 10
   octal = 0o755;         # 493
   hexadecimal = 0x1F4;   # 500
   
   # With underscores for readability
   million = 1_000_000;
   billion = 1_000_000_000;

Floating Point Numbers
~~~~~~~~~~~~~~~~~~~~~~

High-precision floating point:

.. code-block:: symbolic

   pi = 3.141592653589793;
   small = 0.000001;
   large = 6.022e23;      # Avogadro's number
   negative_float = -2.5e-10;

Complex Numbers
~~~~~~~~~~~~~~~

Native complex number support:

.. code-block:: symbolic

   real = 3 + 0i;         # Real number
   imaginary = 0 + 2i;     # Pure imaginary
   complex = 4 + 3i;       # Complex number
   result = (2 + 3i) * (1 - 2i);  # 8 - i

Arithmetic Operations
---------------------

Basic Arithmetic
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   a = 10;
   b = 3;
   
   sum = a + b;           # 13
   difference = a - b;     # 7
   product = a * b;        # 30
   quotient = a / b;       # 3.333...
   floor_division = a // b; # 3
   remainder = a % b;      # 1
   power = a ^ b;          # 1000

Compound Assignment
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 5;
   x += 3;    # x = 8
   x -= 2;    # x = 6
   x *= 4;    # x = 24
   x /= 3;    # x = 8.0
   x //= 2;   # x = 4
   x %= 3;    # x = 1
   x ^= 2;    # x = 1

Mathematical Functions
----------------------

Basic Functions
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 16;
   
   absolute = x.abs();           # 16
   square_root = x.sqrt();       # 4
   exponential = x.exp();        # e^16
   natural_log = x.log();        # ln(16)
   log10 = x.log10();            # log10(16)
   
   # Trigonometric functions (radians)
   angle = π / 4;               # 45 degrees
   sine = angle.sin();           # √2/2 ≈ 0.707
   cosine = angle.cos();         # √2/2 ≈ 0.707
   tangent = angle.tan();        # 1.0

Rounding Functions
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 3.75;
   
   floor = x.floor();     # 3
   ceil = x.ceil();       # 4
   round = x.round();     # 4
   truncate = x.trunc();  # 3
   
   # Round to specific decimal places
   rounded = x.round(1);  # 3.8

Number Properties
-----------------

Type Checking
~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 42;
   y = 3.14;
   z = 2 + 3i;
   
   is_int = x.is_integer();      # true
   is_float = y.is_float();      # true
   is_complex = z.is_complex();  # true
   is_finite = x.is_finite();    # true

Value Properties
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = -5;
   y = 0;
   z = 10;
   
   is_positive = z.is_positive();  # true
   is_negative = x.is_negative();  # true
   is_zero = y.is_zero();          # true
   is_even = z.is_even();          # true
   is_odd = x.is_odd();            # true

Number Conversion
-----------------

Type Conversion
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 3.75;
   
   to_int = x.to_int();        # 3
   to_float = x.to_float();    # 3.75
   to_complex = x.to_complex(); # 3.75 + 0i
   to_string = x.to_string();   # "3.75"

Base Conversion
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 255;
   
   binary_str = x.to_binary();    # "11111111"
   octal_str = x.to_octal();      # "377"
   hex_str = x.to_hex();          # "ff"
   base36 = x.to_base(36);        # "73"

Practical Examples
------------------

Financial Calculations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_compound_interest(principal, rate, years, compounds_per_year) {
       amount = principal * (1 + rate/compounds_per_year) ^ (compounds_per_year * years);
       interest = amount - principal;
       return {amount: amount, interest: interest};
   }
   
   # $1000 at 5% for 10 years, compounded monthly
   result = calculate_compound_interest(1000, 0.05, 10, 12);
   print($"Total: ${result.amount:.2f}");  # $1647.01
   print($"Interest earned: ${result.interest:.2f}");  # $647.01

Statistical Calculations
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_statistics(data) {
       n = data.length();
       mean = data.sum() / n;
       
       # Variance
       squared_differences = data.map(x => (x - mean) ^ 2);
       variance = squared_differences.sum() / (n - 1);
       std_dev = variance.sqrt();
       
       # Median
       sorted_data = data.sorted();
       middle = n // 2;
       if n % 2 == 0 {
           median = (sorted_data[middle - 1] + sorted_data[middle]) / 2;
       } else {
           median = sorted_data[middle];
       }
       
       return {
           count: n,
           mean: mean,
           median: median,
           std_dev: std_dev,
           variance: variance
       };
   }
   
   test_scores = [85, 92, 78, 96, 88, 72, 91, 84, 79, 95];
   stats = calculate_statistics(test_scores);
   print($"Average: {stats.mean:.1f}");    # 86.0
   print($"Median: {stats.median}");       # 86.5
   print($"Std Dev: {stats.std_dev:.1f}"); # 7.9

Engineering Calculations
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_circuit_values(voltage, resistance, capacitance, frequency) {
       # AC circuit calculations
       angular_frequency = 2 * π * frequency;
       impedance = (resistance ^ 2 + (1 / (angular_frequency * capacitance)) ^ 2).sqrt();
       current = voltage / impedance;
       phase_angle = (1 / (angular_frequency * capacitance * resistance)).atan();
       
       return {
           impedance: impedance,
           current: current,
           phase_angle: phase_angle,
           power: voltage * current * phase_angle.cos()
       };
   }
   
   # 120V, 60Hz, 100Ω, 100μF
   circuit = calculate_circuit_values(120, 100, 100e-6, 60);
   print($"Current: {circuit.current:.3f} A");     # 0.119 A
   print($"Phase angle: {circuit.phase_angle:.1f}°"); # -80.5°

Game Development
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_projectile_trajectory(initial_velocity, angle, gravity = 9.81) {
       angle_rad = angle * π / 180;
       
       # Components
       vx = initial_velocity * angle_rad.cos();
       vy = initial_velocity * angle_rad.sin();
       
       # Time of flight
       flight_time = 2 * vy / gravity;
       
       # Range
       range = vx * flight_time;
       
       # Maximum height
       max_height = (vy ^ 2) / (2 * gravity);
       
       return {
           range: range,
           max_height: max_height,
           flight_time: flight_time,
           components: {x: vx, y: vy}
       };
   }
   
   # Projectile at 45° with 20 m/s
   trajectory = calculate_projectile_trajectory(20, 45);
   print($"Range: {trajectory.range:.1f} m");        # 40.8 m
   print($"Max height: {trajectory.max_height:.1f} m"); # 10.2 m

Complex Number Applications
---------------------------

Electrical Engineering
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_ac_circuit(voltage, resistance, inductance, capacitance, frequency) {
       ω = 2 * π * frequency;
       
       # Complex impedance
       z_resistance = resistance + 0i;
       z_inductance = 0 + ω * inductance * 1i;
       z_capacitance = 0 - 1i / (ω * capacitance);
       
       # Total impedance (series)
       z_total = z_resistance + z_inductance + z_capacitance;
       
       # Current
       current = voltage / z_total;
       
       return {
           impedance: z_total,
           current: current,
           magnitude: current.abs(),
           phase: current.arg() * 180 / π
       };
   }

Signal Processing
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn dft(signal) {
       n = signal.length();
       frequencies = [];
       
       for k in 0..<n {
           sum = 0 + 0i;
           for t in 0..<n {
               angle = -2 * π * k * t / n;
               sum += signal[t] * (angle.cos() + angle.sin() * 1i);
           }
           frequencies.append(sum);
       }
       
       return frequencies;
   }

Number Theory
~~~~~~~~~~~~~

.. code-block:: symbolic

   fn is_prime(n) {
       if n < 2: return false;
       if n == 2: return true;
       if n % 2 == 0: return false;
       
       for i in 3..<(n.sqrt().to_int() + 1), 2 {
           if n % i == 0 {
               return false;
           }
       }
       return true;
   }
   
   fn gcd(a, b) {
       while b != 0 {
           (a, b) = (b, a % b);
       }
       return a;
   }
   
   fn lcm(a, b) {
       return (a * b) / gcd(a, b);
   }

Constants and Utilities
-----------------------

Mathematical Constants
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   π = 3.141592653589793;
   e = 2.718281828459045;
   φ = 1.618033988749894;  # Golden ratio
   ∞ = Float.infinity;
   
   # Using constants in calculations
   circle_area = π * radius ^ 2;
   exponential_growth = initial * e ^ (rate * time);

Random Numbers
~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Random integer in range
   dice_roll = random(1, 6);
   
   # Random float
   probability = random();
   
   # Random choice from list
   colors = ["red", "green", "blue"];
   random_color = colors.random_choice();
   
   # Gaussian distribution
   normal_value = random_normal(mean=0, std_dev=1);

Number Formatting
-----------------

String Formatting
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   x = 1234.5678;
   
   # Different formats
   decimal = $"Value: {x}";           # 1234.5678
   fixed = $"Fixed: {x:.2f}";         # 1234.57
   scientific = $"Scientific: {x:.2e}"; # 1.23e+03
   percentage = $"Percentage: {0.856:.1%}"; # 85.6%
   
   # Padding and alignment
   padded = $"|{42:5d}|";             # |   42|
   zero_padded = $"|{42:05d}|";       # |00042|

Localization
~~~~~~~~~~~~

.. code-block:: symbolic

   # Number formatting with thousands separator
   population = 789654123;
   formatted = $"Population: {population:,}";  # 789,654,123
   
   # Currency
   price = 19.99;
   usd = $"Price: ${price:.2f}";      # $19.99
   euro = $"Price: €{price:.2f}";     # €19.99

Performance Tips
----------------

Use Integer Math When Possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - integer arithmetic is faster
   for i in 0..<1000000 {
       result = i * 2;  # Integer multiplication
   }
   
   # Slower - floating point
   for i in 0..<1000000 {
       result = i * 2.0;  # Float multiplication
   }

Precompute Constants
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - precompute expensive operations
   two_pi = 2 * π;
   for angle in angles {
       result = angle * two_pi;  # Fast
   }
   
   # Slower - recompute each time
   for angle in angles {
       result = angle * 2 * π;  # Slower
   }