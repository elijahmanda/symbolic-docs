Numerical Expressions and Implied Multiplication in Symbolic
===========================================================

Symbolic offers an intuitive way to work with numbers and mathematical expressions. It simplifies both large numbers with suffixes and mathematical operations with implied multiplication. These features make writing mathematical expressions more natural, readable, and efficient.

Numerical Suffixes
------------------

Symbolic allows the use of suffixes such as `k` (thousand), `M` (million), and other common numeric abbreviations to express large numbers more compactly. These suffixes scale the number accordingly.

Common Suffixes
----------------
- `k`: Represents 1,000.
- `M`: Represents 1,000,000.
- `B`: Represents 1,000,000,000 (billion).
All standard sufffixes are supported.
This functionality makes it easier to express large numbers without manually writing out all the zeros. The suffixes are automatically interpreted by the Symbolic interpreter, which scales the number for you.

Example:
^^^^^^^^^^^
.. code-block:: symbolic

    # Numeric shorthand with suffixes
    population = 7.8M;  # 7.8 million people
    distance = 2k;      # 2,000 meters
    budget = 1.5B;      # 1.5 billion dollars

In these examples:
- `population` will evaluate to 7,800,000.
- `distance` will evaluate to 2,000.
- `budget` will evaluate to 1,500,000,000.

These suffixes provide convenience when working with large datasets, financial figures, or statistical values.

Implied Multiplication
-----------------------

One of the core features of Symbolic is the ability to infer multiplication automatically between numbers, variables, and expressions. This reduces the need for explicit operators, making mathematical notation more concise and closer to traditional mathematical writing.

Implied Multiplication Rules
-----------------------------

- **Number and Variable**: When a number is immediately followed by a variable, it implies multiplication.
    - Example: `2PI` is interpreted as `2 * PI` (where `PI` is a constant representing π).
- **Number and Parenthesis**: When a number is immediately followed by an expression in parentheses, it implies multiplication.
    - Example: `7(3x - 8)` is interpreted as `7 * (3x - 8)`.
- **Number and Name**: When a number is followed by a name (which could be a variable or a symbol), it implies multiplication.
    - Example: `23oranges` is interpreted as `23 * oranges` (assuming `oranges` is a variable).

This feature helps in reducing visual clutter and allows you to express algebraic equations in a more readable way.

Example:
^^^^^^^^^^
.. code-block:: symbolic

    # Implied multiplication examples
    result = 2PI + 3x^2 + 9;    # 2 * PI + 3 * x^2 + 9
    area = 7(3x - 8);            # 7 * (3x - 8)
    fruitCount = 23oranges;      # 23 * oranges

In the first example, the expression `2PI + 3x^2 + 9` is equivalent to `2 * PI + 3 * x^2 + 9`. The second expression, `7(3x - 8)`, simplifies to `7 * (3x - 8)`. Finally, `23oranges` is interpreted as `23 * oranges`, implying that `oranges` is a variable representing a count or quantity.

Benefits of Implied Multiplication
-----------------------------------

- **Simplified Syntax**: You no longer need to write `*` every time you multiply numbers and variables, making expressions shorter and easier to understand.
- **Closer to Mathematical Notation**: The implied multiplication syntax follows the conventions commonly used in algebra and calculus, allowing you to write equations more like you would on paper.
- **Enhanced Readability**: The removal of extra multiplication symbols makes the expressions clearer and more intuitive, especially when working with complex formulas.

Implied Multiplication in Algebraic Expressions
------------------------------------------------

In algebraic expressions, implied multiplication allows you to easily combine terms, whether they're simple constants or more complex variables.

Examples of Algebraic Expressions
----------------------------------
- `3x^2 + 9` means `3 * x^2 + 9`.
- `2y(3x + 5)` means `2 * y * (3x + 5)`.
- `5a^2b` means `5 * a^2 * b`.

Example:
^^^^^^^^^^
.. code-block:: symbolic

    # Algebraic expression examples
    expression1 = 3x^2 + 9;        # 3 * x^2 + 9
    expression2 = 2y(3x + 5);      # 2 * y * (3x + 5)
    expression3 = 5a^2b;           # 5 * a^2 * b

In these examples:
- `expression1` evaluates to `3 * x^2 + 9`.
- `expression2` evaluates to `2 * y * (3x + 5)`.
- `expression3` evaluates to `5 * a^2 * b`.

Implied Multiplication in Functions and Constants
--------------------------------------------------

Implied multiplication can also be applied when working with functions and constants in Symbolic. This feature ensures that even function calls and constants can be written in a more natural, intuitive way.

Example:
^^^^^^^^^^^^
.. code-block:: symbolic

    # Function and constant examples
    f = 3x^2 + 5x - 2;         # f(x) = 3 * x^2 + 5 * x - 2
    g = 2(3x - 4);             # g(x) = 2 * (3x - 4)

Here:
- `f = 3x^2 + 5x - 2` is interpreted as `f(x) = 3 * x^2 + 5 * x - 2`.
- `g = 2(3x - 4)` is interpreted as `g(x) = 2 * (3x - 4)`.

This allows you to create and write functions in a concise way, removing the need to explicitly use multiplication symbols.

Implied Multiplication and Numbers Followed by Names
-----------------------------------------------------

When a number is immediately followed by a name or a variable, Symbolic interprets this as multiplication. This is a powerful feature for creating formulas where numbers are dynamically multiplied by variables or constants.

Example:
^^^^^^^^^^
.. code-block:: symbolic

    # Numbers followed by names
    totalCost = 10items;    # 10 * items
    pricePerUnit = 20perItem;  # 20 * perItem

In these examples:
- `totalCost = 10items` is interpreted as `totalCost = 10 * items`.
- `pricePerUnit = 20perItem` is interpreted as `pricePerUnit = 20 * perItem`.

This feature helps when dealing with quantities, units, or even more complex formulas, and enables more flexible, human-readable code.

Summary of Numerical and Implied Multiplication Features
--------------------------------------------------------

Symbolic simplifies the writing and evaluation of numerical expressions by supporting:
- **Numerical suffixes** for representing large numbers like `k` for thousands and `M` for millions.
- **Implied multiplication** in expressions involving numbers, variables, and parentheses, reducing the need for explicit multiplication operators.
- **Concise, natural mathematical expressions** that resemble traditional algebraic notation.
- **Flexibility** in defining and using formulas, constants, and functions.

These features not only make writing code more efficient but also bring Symbolic closer to real-world mathematical writing, making it more intuitive for those familiar with mathematical syntax.

By utilizing these features, you can write expressions, functions, and algorithms with ease, allowing for more readable and mathematically aligned code.
