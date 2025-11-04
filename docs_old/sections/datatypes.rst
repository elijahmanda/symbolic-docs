Data Types
===========

Symbolic supports a variety of data types to handle both simple and complex data structures. Below is a list of available data types, along with their features and usage.

Primitive Data Types
-------------------------

The basic data types in Symbolic include:

- **Integer**: Represents whole numbers (e.g., `5`, `-10`, `100`).
- **Float**: Represents decimal numbers (e.g., `3.14`, `-0.5`, `2.718`).
- **Boolean**: Represents binary values (`true` or `false`).
- **String**: Represents sequences of characters (e.g., `"hello"`, `'world'`).
- **Null**: Represents the absence of a value (e.g., `null`, `None`).

Complex Data Types
------------------------

Symbolic also supports more complex data types:

- **List**: Represents an ordered collection of items. Lists can be mutable or immutable, with `locked` property controlling the mutability. When a list is locked, any attempt to modify it (such as `pop`, `assign`, or other mutations) raises a `ValueError`.

Example: List
^^^^^^^^^^^^^^^^^^
.. code-block:: symbolic

    numbers = List([1, 2, 3, 4], locked=true); # Immutable list
    try {
        numbers.append(5);  # This will raise a ValueError because the list is locked
    } catch (e) {
        print("Error:", e);
    }
    
    numbers.unlock();  # Makes the list mutable again
    numbers.append(5);  # Now this operation works
    print(numbers);
    
    numbers.lock();    # Locks the list, making it immutable
    try {
        numbers.pop();  # This will raise a ValueError because the list is locked
    } catch (e) {
        print("Error:", e);
    }

- **Set**: Represents a collection of unique items.

Example: Set
^^^^^^^^^^^^^^^^^^
.. code-block:: symbolic

    unique_numbers = {1, 2, 3};

- **Dictionary (Map)**: Represents a collection of key-value pairs.

Example: Dictionary
^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: symbolic

    user = {"name": "Alice", "age": 30};

Advanced Data Types
-------------------------

For more advanced operations, Symbolic supports the following types:

- **Symbol**: Represents symbolic or mathematical constants, variables, or expressions.

Example: Symbol
^^^^^^^^^^^^^^^^^^^
.. code-block:: symbolic

    x = Symbol("x");
    pi = Symbol("π");

- **Complex Number**: Represents complex numbers (e.g., `3 + 4i`).

Example: Complex Numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: symbolic

    z = 3 + 4i;
    w = 5.5 + 7j; # j or i suffix

Custom Data Types (User-defined)
------------------------------------

Symbolic allows users to define custom types:

- **Enumerations (Enum)**: Represents a set of named constants.

Example: Enum
^^^^^^^^^^^^^^^^^^
.. code-block:: symbolic

    enum Day { Monday, Tuesday, Wednesday };

Summary
-----------

The following data types are supported in Symbolic:

1. **Primitive Types**: Integer, Float, Boolean, String, Null
2. **Complex Types**: List, Set, Dictionary
3. **Advanced Types**: Symbol, Complex Number
4. **Custom Types**: Enum