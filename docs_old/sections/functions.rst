Functions
=========

Functions in Symbolic are first-class citizens and can be anonymous (lambdas). The `fn` keyword is optional when defining functions, allowing for cleaner syntax if preferred. Functions can be defined in various styles and offer flexibility in how they are written and invoked.

Defining Functions
-----------------------

Define reusable functions using `->`, with or without the `fn` keyword. If `fn` keyword is prefixed then the function name must follow arguments.

.. code-block:: symbolic

    fn gcd(a, b) -> {
        while b != 0 {
            temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };
    print("GCD of 48 and 18 =", gcd(48, 18));

Alternatively, you can omit the `fn` keyword:

.. code-block:: symbolic

    gcd_alt = (a, b) -> {
        while b != 0 {
            temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };
    print("GCD of 48 and 18 (alternative) =", gcd_alt(48, 18));

Compact, One-Line Functions
-------------------------------

For compact functions, write them in a single line:

.. code-block:: symbolic

    fn is_even(x) -> x % 2 == 0;
    print("Is 4 even?", is_even(4));

Or omit the `fn` keyword for brevity:

.. code-block:: symbolic

    is_even_alt = (x) -> x % 2 == 0;
    print("Is 4 even (alternative)?", is_even_alt(4));

Recursive Functions
----------------------

Define recursive functions for problems like factorial:

.. code-block:: symbolic

    fn factorial(n) -> {
        if n <= 1 { return 1; }
        return n * factorial(n - 1);
    };
    print("Factorial of 6 =", factorial(6));

Higher-Order Functions
-------------------------

Symbolic supports higher-order functions. You can pass functions as arguments:

.. code-block:: symbolic

    fn apply_twice(func, x) -> func(func(x));
    fn square(x) -> x * x;
    print("Square of square of 3 =", apply_twice(square, 3));

Or use the optional `fn` syntax:

.. code-block:: symbolic

    apply_twice_alt = (func, x) -> func(func(x));
    square_alt = (x) -> x * x;
    print("Square of square of 3 (alternative) =", apply_twice_alt(square_alt, 3));

Anonymous Functions (Lambdas)
-----------------------------------

You can define and use anonymous functions (lambdas):

.. code-block:: symbolic

    print("Sum of 3 and 5 =", ((x, y) -> x + y)(3, 5));
    print("Product of 3 and 4 =", ((x, y) -> x * y)(3, 4));

Function with Default Arguments
------------------------------------

You can also set default arguments for your functions:

.. code-block:: symbolic

    fn greet(name="Stranger") -> "Hello, " + name + "!";
    print(greet("Alice"));
    print(greet());  # Uses default argument

Or omit the `fn` keyword:

.. code-block:: symbolic

    greet_alt = (name="Stranger") -> "Hello, " + name + "!";
    print(greet_alt("Bob"));
    print(greet_alt());  # Uses default argument
