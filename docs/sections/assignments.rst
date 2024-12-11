Assignments
==================

Symbolic supports various forms of assignment, including normal assignments, chained assignments, and unpacking of collections. This allows for flexible variable initialization and management.

Normal Single Assignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normal assignment is used to assign a value to a variable.

.. code-block:: symbolic

    x = 1;
    print("x =", x);

Single Value Assignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can assign a single value to multiple variables in one statement, also known as chained assignment.

.. code-block:: symbolic

    x = y = 2;
    print("x = y =", x, y);

Unpack Normal
^^^^^^^^^^^^^^^^^^^

Unpacking allows you to assign values from collections (like lists) to variables.

.. code-block:: symbolic

    (x, y) = [1, 2];
    print("x =", x, "y =", y);

Unpack Asterisk (No Name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The asterisk (`*`) can be used in unpacking to ignore specific elements. This is useful when you want to capture the remaining elements of a collection without naming them.

.. code-block:: symbolic

    (*, y) = [1, 2, 3];
    print("y =", y);

Unpack Asterisk (With Name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also use the asterisk (`*`) to collect the remaining items into a variable, allowing you to capture multiple values at once.

.. code-block:: symbolic

    (*x, y) = [1, 2, 3];
    print("x =", x, "y =", y);

Use Cases
--------------

1. **Multiple Assignments**  
   Use chained assignments to efficiently assign the same value to multiple variables.
   
2. **Unpacking**  
   Unpacking is ideal for extracting elements from lists or tuples into individual variables.

3. **Ignoring Elements**  
   Use the asterisk to discard unwanted values during unpacking while still capturing the ones you need.

Example: Chained Assignment and Unpacking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    # Chained assignment
    a = b = 3;
    print("a =", a, "b =", b);

    # Unpacking a list
    (x, y, z) = [4, 5, 6];
    print("x =", x, "y =", y, "z =", z);

    # Using asterisk to ignore first two elements
    (*_, z) = [4, 5, 6];
    print("z =", z);

    # Using asterisk to collect remaining items
    (*x, y) = [4, 5, 6];
    print("x =", x, "y =", y);
