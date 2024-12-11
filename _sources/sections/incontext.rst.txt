The `in context` Construct
===========================

The `in context` construct in Symbolic provides a concise and intuitive way to execute a series of operations on an object or owner. This construct allows you to check for method or attribute names within the "context owner" (the specified object), and if the names are not found in the context owner, they are resolved from the outer scope.

Overview
--------

The syntax for the `in context` construct is as follows:

.. code-block:: symbolic

    in context <owner> {
        <operation_1>();
        <operation_2>();
        ...
    }

Key Features:
- **Context Owner Lookup**: The construct prioritizes checking method or attribute names within the specified context owner.
- **Fallback to Outer Scope**: If a name is not found in the context owner, it is resolved from the surrounding (outer) context.
- **Simplified Syntax**: Reduces the need for repeated object references.

Basic Example
-------------

In this example, operations are performed on the `matrix` object:

.. code-block:: symbolic

    matrix = Matrix([[1, 2], [3, 4]]);

    in context matrix {
        transpose();
        normalize();
    }

Explanation:
- The methods `transpose()` and `normalize()` are executed on the `matrix` object. 
- This is equivalent to the following:

  .. code-block:: symbolic

      matrix.transpose();
      matrix.normalize();

Outer Context Fallback
----------------------

If a name is not found in the context owner, it is resolved from the outer scope:

.. code-block:: symbolic

    matrix = Matrix([[1, 2], [3, 4]]);
    epsilon = 0.001;

    in context matrix {
        normalize();
        print(epsilon);  # 'epsilon' is resolved from the outer context
    }

Explanation:
- The `normalize()` method is executed on `matrix`.
- The variable `epsilon` is not part of the `matrix` context, so it is resolved from the outer scope.

Nested `in context` Constructs
-------------------------------

`in context` constructs can be nested to work with multiple context owners:

.. code-block:: symbolic

    matrix = Matrix([[1, 2], [3, 4]]);
    vector = Vector([1, 0]);

    in context matrix {
        transpose();

        in context vector {
            normalize();
        }
    }

Explanation:
- The `transpose()` method is executed on `matrix`.
- Within the nested context, the `normalize()` method is executed on `vector`.

Use Cases
---------

The `in context` construct is particularly useful in scenarios where:
- You need to perform multiple operations on a single object.
- There is a mix of methods/attributes within the context owner and variables from the outer scope.
- Readability and code brevity are priorities.

Conclusion
----------

The `in context` construct enhances Symbolic's ability to streamline operations and reduce repetitive code, making it a powerful feature for managing object-centric workflows.
