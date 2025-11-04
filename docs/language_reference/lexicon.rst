Lexical Reference
=================

This document describes the complete set of tokens and lexical elements in the Symbolic language, derived from ``tokens.py``.

Token Types
-----------

The lexer recognizes the following token types:

Basic Tokens
~~~~~~~~~~~~

* ``NUMBER`` - Numeric literals (integer, float, complex)
* ``STRING`` - String literals
* ``IDENTIFIER`` - Variable and function names
* ``COMMENT`` - Single-line (#) and multi-line (/** */) comments
* ``EOF`` - End of file

Keywords
~~~~~~~~

.. list-table::
   :header-rows: 1
   
   * - Keyword
     - Token Type
     - Description
   * - ``if``
     - ``TokenType.IF``
     - Conditional statement
   * - ``else``
     - ``TokenType.ELSE``
     - Conditional alternative
   * - ``while``
     - ``TokenType.WHILE``
     - Loop construct
   * - ``fn``
     - ``TokenType.FN``
     - Function definition
   * - ``class``
     - ``TokenType.CLASS``
     - Class definition
   * - ``static``
     - ``TokenType.STATIC``
     - Static method/field
   * - ``final``
     - ``TokenType.FINAL``
     - Final declaration
   * - ``enum``
     - ``TokenType.ENUM``
     - Enumeration definition
   * - ``extends``
     - ``TokenType.EXTENDS``
     - Class inheritance
   * - ``return``
     - ``TokenType.RETURN``
     - Function return
   * - ``loop``
     - ``TokenType.LOOP``
     - Infinite loop
   * - ``for``
     - ``TokenType.FOR``
     - For loop
   * - ``stop``
     - ``TokenType.STOP``
     - Break statement
   * - ``skip``
     - ``TokenType.SKIP``
     - Continue statement
   * - ``try``
     - ``TokenType.TRY``
     - Exception handling
   * - ``catch``
     - ``TokenType.CATCH``
     - Exception catcher
   * - ``assert``
     - ``TokenType.ASSERT``
     - Assertion
   * - ``raise``
     - ``TokenType.RAISE``
     - Raise exception
   * - ``import``
     - ``TokenType.IMPORT``
     - Module import
   * - ``const``
     - ``TokenType.CONST``
     - Constant declaration
   * - ``domain``
     - ``TokenType.DOMAIN``
     - Domain context
   * - ``async``
     - ``TokenType.ASYNC``
     - Async function
   * - ``await``
     - ``TokenType.AWAIT``
     - Await expression
   * - ``parallel``
     - ``TokenType.PARALLEL``
     - Parallel execution

Operators
---------

Assignment Operators
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   
   * - Operator
     - Token Type
     - Description
   * - ``=``
     - ``TokenType.ASSIGN``
     - Basic assignment
   * - ``:=``
     - ``TokenType.COLON_EQUAL``
     - Declaration assignment
   * - ``+=``
     - ``TokenType.PLUS_EQUAL``
     - Add and assign
   * - ``-=``
     - ``TokenType.MINUS_EQUAL``
     - Subtract and assign
   * - ``*=``
     - ``TokenType.ASTERISK_EQUAL``
     - Multiply and assign
   * - ``/=``
     - ``TokenType.SLASH_EQUAL``
     - Divide and assign
   * - ``//=``
     - ``TokenType.DOUBLE_SLASH_EQUAL``
     - Floor divide and assign
   * - ``%=``
     - ``TokenType.MODULO_EQUAL``
     - Modulo and assign

Binary Operators
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   
   * - Operator
     - Token Type
     - Precedence
     - Associativity
   * - ``+``
     - ``TokenType.PLUS``
     - 5
     - Left
   * - ``-``
     - ``TokenType.MINUS``
     - 5
     - Left
   * - ``*``
     - ``TokenType.ASTERISK``
     - 7
     - Left
   * - ``/``
     - ``TokenType.SLASH``
     - 7
     - Left
   * - ``//``
     - ``TokenType.DOUBLE_SLASH``
     - 7
     - Left
   * - ``%``
     - ``TokenType.MODULO``
     - 7
     - Left
   * - ``^``
     - ``TokenType.CARET``
     - 9
     - Right
   * - ``&&``, ``and``
     - ``TokenType.AND``
     - 3
     - Left
   * - ``||``, ``or``
     - ``TokenType.OR``
     - 2
     - Left
   * - ``==``
     - ``TokenType.EQUAL_TO``
     - 3
     - Left
   * - ``!=``
     - ``TokenType.NOT_EQUAL``
     - 3
     - Left
   * - ``<``
     - ``TokenType.LESS_THAN``
     - 3
     - Left
   * - ``>``
     - ``TokenType.GREATER_THAN``
     - 3
     - Left
   * - ``<=``
     - ``TokenType.LESS_THAN_OR_EQUAL``
     - 3
     - Left
   * - ``>=``
     - ``TokenType.GREATER_THAN_OR_EQUAL``
     - 3
     - Left

Matrix Operators
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   
   * - Operator
     - Token Type
     - Description
   * - ``@+``
     - ``TokenType.MATRIX_ADD``
     - Matrix addition
   * - ``@-``
     - ``TokenType.MATRIX_SUB``
     - Matrix subtraction
   * - ``@*``
     - ``TokenType.MATRIX_MUL``
     - Matrix multiplication
   * - ``@/``
     - ``TokenType.MATRIX_DIV``
     - Matrix division

Set Operators
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   
   * - Operator
     - Token Type
     - Description
   * - ``∩``
     - ``TokenType.INTERSECTION``
     - Set intersection
   * - ``∪``
     - ``TokenType.UNION``
     - Set union
   * - ``⊂``
     - ``TokenType.SUBSET``
     - Proper subset
   * - ``⊆``
     - ``TokenType.SUBSET_EQ``
     - Subset or equal

Special Symbols
---------------

Containers
~~~~~~~~~~

* ``( )`` - ``TokenType.LEFT_PAREN``, ``TokenType.RIGHT_PAREN`` - Grouping, function calls
* ``[ ]`` - ``TokenType.LEFT_BRACKET``, ``TokenType.RIGHT_BRACKET`` - Lists, indexing
* ``{ }`` - ``TokenType.LEFT_BRACE``, ``TokenType.RIGHT_BRACE`` - Blocks, dictionaries, sets

Separators
~~~~~~~~~~

* ``,`` - ``TokenType.COMMA`` - Separator
* ``;`` - ``TokenType.SEMICOLON`` - Statement terminator
* ``:`` - ``TokenType.COLON`` - Type annotation, dictionary pairs
* ``::`` - ``TokenType.DOUBLE_COLON`` - Namespace, slice
* ``.`` - ``TokenType.FULL_STOP`` - Attribute access
* ``->`` - ``TokenType.ARROW_RIGHT`` - Function return type
* ``=>`` - ``TokenType.EQUAL_FORWARD`` - Lambda expression

Other Symbols
~~~~~~~~~~~~~

* ``@`` - ``TokenType.AT`` - Decorators, domain constructs
* ``$`` - ``TokenType.DOLLAR_SIGN`` - Domain-specific constructs
* ``...`` - ``TokenType.ELLIPSIS`` - Variadic, range
* ``?`` - ``TokenType.QUESTION`` - Ternary, optional
* ``??`` - ``TokenType.NULL_COALESCE`` - Null coalescing

Precedence Levels
-----------------

The parser uses the following precedence levels (higher numbers bind tighter):

.. list-table::
   :header-rows: 1
   
   * - Precedence
     - Operators
   * - 15
     - Index ``[]``, Attribute ``.``
   * - 14
     - Container ``()`` ``[]`` ``{}``
   * - 13
     - Function call ``()``
   * - 9
     - Exponentiation ``^``
   * - 7
     - Multiplication ``* / // %``
   * - 5
     - Addition ``+ -``, Bit shifts ``<< >>``
   * - 3
     - Comparison ``< > <= >= == !=``, Logical ``and``
   * - 2
     - Logical ``or``, Pipeline ``|>``
   * - 1
     - Assignment ``= := += -=``

Number Literals
---------------

Symbolic supports various number formats:

Integers
~~~~~~~~

.. code-block:: symbolic

   42           # Decimal
   1_000_000    # With underscores
   0b1010       # Binary (10)
   0o755        # Octal (493)  
   0x1F4        # Hexadecimal (500)

Floats
~~~~~~

.. code-block:: symbolic

   3.14         # Basic float
   1.5e-10      # Scientific notation
   6.022e23     # Large numbers

Complex
~~~~~~~

.. code-block:: symbolic

   3i           # Pure imaginary
   2 + 5i       # Complex number

With Suffixes
~~~~~~~~~~~~~

.. code-block:: symbolic

   2k           # 2000
   5M           # 5,000,000
   3.5B         # 3,500,000,000

See :doc:`number_suffixes` for complete suffix documentation.

String Literals
---------------

.. code-block:: symbolic

   "hello"              # Basic string
   'world'              # Single quotes
   "line1\nline2"       # Escape sequences
   """multi-line        # Triple-quoted
   string"""

This lexical reference provides the foundation for understanding Symbolic syntax. Continue to :doc:`syntax` for grammatical structure.