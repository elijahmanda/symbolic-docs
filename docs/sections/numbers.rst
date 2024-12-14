Numbers in Symbolic
===================

This section provides a comprehensive guide to working with numbers in Symbolic, including syntax, features, methods, and advanced operations. Numbers are categorized as integers, floating-point numbers, and complex numbers, each with their own specialized methods and operations.

Supported Number Formats
----------------------------------

Symbolic supports multiple number formats, ensuring flexibility and convenience in numerical representation. Below are the primary formats supported:

- **Integers**: Standard integers, binary (`0b`), octal (`0o`), hexadecimal (`0x`), and readable numbers with underscores (`_`).
- **Floating-Point Numbers**: Standard floating-point numbers with support for exponential notation (`e`), underscores, and suffixes for large numbers (`k` for thousand, `M` for million, `B` for billion).
- **Complex Numbers**: Represented using `i` or `j` for the imaginary unit.

Examples:

.. code-block:: symbolic

    10                # An integer
    0b1010            # Binary representation, equivalent to 10
    0o12              # Octal representation, equivalent to 10
    0xA               # Hexadecimal representation, equivalent to 10
    1_000_000         # Readable integer, equivalent to 1000000
    3.14              # A floating-point number
    2.5e3             # Exponential notation, equivalent to 2500
    4.8M              # Suffix for million, equivalent to 4800000.0
    5B                # Suffix for billion, equivalent to 5000000000
    7i                # A complex number with imaginary part 7
    2 + 3j            # A complex number with real part 2 and imaginary part 3

Basic Arithmetic Operations
----------------------------------

Symbolic provides support for standard arithmetic operations. These include addition, subtraction, multiplication, division, modulo, and exponentiation.

Examples:

.. code-block:: symbolic

    5 + 3               # 8
    9 - 4               # 5
    7 * 6               # 42
    15 / 2              # 7.5
    17 % 3              # 2
    2 ** 3              # 8 (Exponentiation)

Advanced Number Operations
----------------------------------

Symbolic includes advanced operations, such as factorial, logarithmic calculations, and trigonometric functions.

- **Factorial**: Calculate the factorial of an integer.

  .. code-block:: symbolic

      5.factorial()       # 120 (5 * 4 * 3 * 2 * 1)

- **Logarithmic Operations**: Compute logarithms to any base or natural logarithms.

  .. code-block:: symbolic

      10.log(2)           # 3.321928094887362 (Log base 2 of 10)
      100.log10()         # 2 (Log base 10 of 100)

- **Trigonometric Operations**: Compute sine, cosine, and tangent of a number (in radians).

  .. code-block:: symbolic

      1.sin()             # 0.8414709848078965
      1.cos()             # 0.5403023058681398
      1.tan()             # 1.5574077246549023

Base Conversions
----------------------

Numbers in Symbolic can be converted between different bases, such as binary, octal, and hexadecimal.

Examples:

.. code-block:: symbolic

    10.to_bin()          # '0b1010' (Binary representation of 10)
    10.to_oct()          # '0o12' (Octal representation of 10)
    10.to_hex()          # '0xA' (Hexadecimal representation of 10)

Spoken Representation
---------------------------

Convert numbers to their spoken-word equivalents for better human understanding.

Examples:

.. code-block:: symbolic

    123.spoken()         # 'one hundred twenty three'
    4.56.spoken()        # 'four point five six'
    (-789).spoken()      # 'negative seven hundred eighty nine'
    (+4.8).spoken()      # 'positive four point eight'

.. NOTE::
   **Operator Precedence Warning**: 

   Due to operator precedence, `.` (method access) has higher precedence than unary operators such as `+` or `-`.  
   For example:

   - `-3.spoken()` will be evaluated as `-(3.spoken())`, resulting in an error because `spoken()` returns a string, and `-` cannot operate on strings.
   - To avoid this, use parentheses to ensure the correct evaluation order:
     
     .. code-block:: symbolic

         (-3).spoken()    # 'negative three'
         (+7.3).spoken()  # 'positive seven point three'

Prime Number Checks
---------------------------

Symbolic includes methods to check whether a number is prime.

Examples:

.. code-block:: symbolic

    13.is_prime()        # true (13 is a prime number)
    15.is_prime()        # false (15 is not a prime number)

Complex Numbers
-----------------------

Symbolic supports operations specific to complex numbers, including magnitude, angle, and polar form.

Examples:

.. code-block:: symbolic

    (3 + 4i).abs()       # 5.0 (Magnitude of the complex number)
    (3 + 4i).angle()     # 0.9272952180016122 (Angle in radians)
    (3 + 4i).polar_form()# '(5.0, 0.9272952180016122)' (Polar representation)

Parsing Strings
-------------------

All numeric classes (`Int`, `Float`, and `Complex`) provide a `parse` method for converting formatted strings into numeric types.

Examples:
^^^^^^^^^^^^^^

.. code-block:: symbolic

    Int.parse("1,000")      # 1000
    Float.parse("3.14e2")   # 314.0
    Complex.parse("7 + 5i") # (7 + 5i)

Methods by Class
---------------------

Symbolic numbers are categorized into `Int`, `Float`, and `Complex`. Below are the specific methods available for each class.

- **Int**: Includes `abs`, `factorial`, `gcd`, `lcm`, `is_prime`, `to_hex`, `to_bin`, and more.
- **Float**: Includes `abs`, `sin`, `cos`, `log`, `sqrt`, `to_string`, and more.
- **Complex**: Includes `abs`, `angle`, `polar_form`, `real`, `imag`, and more.

.. code-block:: symbolic

    # Example Int Methods
    10.abs()               # 10
    5.gcd(15)              # 5
    6.is_even()            # true

    # Example Float Methods
    3.14.sqrt()            # 1.772453850905516
    0.5.exp()              # 1.6487212707001282

    # Example Complex Methods
    (3 + 4i).abs()         # 5.0
    (3 + 4i).angle()       # 0.9272952180016122
