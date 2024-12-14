Operators in Symbolic
=====================

Symbolic provides a variety of operators to support arithmetic, assignment, comparison, and other operations. These operators are grouped into categories for clarity and ease of use.

Assignment Operators
--------------------

Assignment operators assign values to variables. Symbolic supports the following assignment styles:

- **`=`**: Standard assignment.
- **`:=`**: Assignment with initialization.
- **`<-`**: Left arrow assignment.
- **`+=`**: Add and assign.
- **`-=`**: Subtract and assign.
- **`*=`** or **`×=`**: Multiply and assign.
- **`/=`** or **`÷=`**: Divide and assign.
- **`%=`**: Modulus and assign.
- **`|=`**: Bitwise OR and assign.
- **`||=`**: Logical OR and assign.
- **`//=`**: Floor divide and assign.
- **`^=`**: Exponentiate and assign.

Examples:
^^^^^^^^^^^^
.. code-block:: symbolic

    x = 10;       # Standard assignment
    y += 5;       # Increment y by 5
    total /= 2;   # Divide total by 2 and assign

Binary Operators
------------------

Binary operators perform operations on two operands. These include arithmetic, logical, and bitwise operators.

Supported Binary Operators:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Arithmetic: **`+`**, **`-`**, **`*`**, **`/`**, **`//`**, **`÷`**, **`×`**, **`%`**
- Logical: **`||`**, **`&&`**
- Bitwise: **`|`**, **`&`**, **`^`**
- Exponentiation: **`**`**
- Comparison: **`!=`**, **`<`**, **`>`**
- Range and Slicing: **`..`**

Examples:
^^^^^^^^^^^
.. code-block:: symbolic

    sum = a + b;         # Addition
    range = 1..10;       # Range from 1 to 10
    slice = list[2..5];  # Slice from index 2 to 5

Absolute Value
--------------

The absolute value operator `|expression|` returns the magnitude of a number, ignoring its sign.

Examples:
^^^^^^^^^^^^^
.. code-block:: symbolic

    abs_value = |x|;   # Absolute value of x
    print(|-8|);       # Output: 8

Prefix Operators
----------------

Prefix operators work on a single operand placed immediately after the operator.

Supported Prefix Operators:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Arithmetic: **`+`**, **`-`**
- Logical: **`!`**
- Bitwise: **`~`**
- Ranges: **`..`**
- Mixed: **`+/-`** (plus or minus)

Examples:
^^^^^^^^^^^^^
.. code-block:: symbolic

    value = -x;    # Negation
    range = ..5;   # Range from 0 to 5
    not_flag = !true;  # Logical NOT

Postfix Operators
-----------------

Postfix operators operate on a single operand placed before the operator. 

Supported Postfix Operators:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Logical: **`!`**
- Ranges: **`..`**
- Special: **`°`**, **`'`**

Examples:
^^^^^^^^^^^^
.. code-block:: symbolic

    angle = 45°;   # Represents 45 degrees
    complement = x';   # Complement of x

Equality and Comparison Operators
---------------------------------

Equality and comparison operators are used to compare two operands.

Supported Comparison Operators:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **`<`**: Less than
- **`>`**: Greater than
- **`<=`**: Less than or equal to
- **`>=`**: Greater than or equal to
- **`==`**: Equal to
- **`!=`**: Not equal to

Examples:
^^^^^^^^^^^^^
.. code-block:: symbolic

    if x < y {
        print("x is less than y");
    }
    else if x == y {
        print("x is equal to y");
    } else {
        print("x is greater than y");
    }
