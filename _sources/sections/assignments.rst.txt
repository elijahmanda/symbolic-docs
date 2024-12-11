Assignments
===========

Symbolic supports multiple assignment styles, unpacking, and lazy evaluation.

Variables and Assignments
-------------------------

Normal Assignment
~~~~~~~~~~~~~~~~~
Assign values to variables using the `=` operator:

.. code-block:: symbolic

    x = 10;
    y = 20;
    print("x =", x, "y =", y);

Lazy Assignment
~~~~~~~~~~~~~~~~
Lazy assignment (`:=`) delays evaluation until the variable is accessed:

.. code-block:: symbolic

    x := 5 + 10;
    print("x =", x);  # Evaluates 5 + 10 here

Multiple Assignments
~~~~~~~~~~~~~~~~~~~~
Assign the same value to multiple variables:

.. code-block:: symbolic

    x = y = z = 42;
    print(x, y, z);

Unpacking
~~~~~~~~~
Unpack values from arrays, tuples, or similar structures into individual variables:

.. code-block:: symbolic

    (a, b, c) = [1, 2, 3];
    print("a =", a, "b =", b, "c =", c);

Unpack the head and tail of a list-like structure:

.. code-block:: symbolic

    (*head, tail) = [10, 20, 30, 40];
    print("head =", head, "tail =", tail);
