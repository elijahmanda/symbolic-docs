Syntax Reference
================

This document describes the formal syntax of the Symbolic language, derived from the parser implementation and .sym files.

Core Grammar
------------

The Symbolic parser uses a precedence-climbing algorithm with multi-position token support. The grammar is defined in the ``SymbolicParser`` class and supporting .sym files.

Expression Grammar
~~~~~~~~~~~~~~~~~~

.. productionlist::
   expression: ternary_expression
   ternary_expression: logical_or_expression ("?" expression ":" expression)?
   logical_or_expression: logical_and_expression ("||" logical_and_expression)*
   logical_and_expression: equality_expression ("&&" equality_expression)*
   equality_expression: relational_expression (("==" | "!=") relational_expression)*
   relational_expression: additive_expression (("<" | ">" | "<=" | ">=") additive_expression)*
   additive_expression: multiplicative_expression (("+" | "-") multiplicative_expression)*
   multiplicative_expression: prefix_expression (("*" | "/" | "//" | "%") prefix_expression)*
   prefix_expression: ("+" | "-" | "!" | "~" | "..") prefix_expression | postfix_expression
   postfix_expression: primary_expression ("!" | "°" | "'" | "%")*
   primary_expression: number | string | identifier | "(" expression ")" | "[" expression_list "]" | "{" dict_or_set "}" | function_call | attribute_access

Statement Grammar
~~~~~~~~~~~~~~~~~

.. productionlist::
   statement: expression_statement
            :| assignment_statement
            :| if_statement
            :| while_statement
            :| for_statement
            :| return_statement
            :| function_definition
            :| class_definition
   expression_statement: expression ";"
   assignment_statement: identifier assignment_operator expression ";"
   assignment_operator: "=" | ":=" | "+=" | "-=" | "*=" | "/=" | "//=" | "%=" | "|=" | "||=" | "^=" | "<<=" | ">>=" | "?="

Multi-position Token System
---------------------------

Symbolic supports tokens that can appear in multiple syntactic positions:

Question Mark (?)
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   ?x           # Prefix: maybe operator or placeholder
   x ? y : z    # Infix: ternary condition  
   ?            # Standalone: placeholder

Plus/Minus (+/-)
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   +5           # Prefix: positive operator
   x + y        # Infix: addition
   x+           # Postfix: increment (planned)

Bang (!)
~~~~~~~~

.. code-block:: symbolic

   !condition   # Prefix: logical NOT
   x!           # Postfix: factorial

Parser States
-------------

The parser maintains state for context-sensitive parsing:

* **NORMAL**: Default parsing state
* **IN_LOOP**: Inside loop constructs (enables break/continue)
* **IN_FUNCTION**: Inside function definitions
* **IN_TERNARY**: Parsing ternary expressions
* **IN_CLASS**: Inside class definitions

Examples from .sym Files
------------------------

The language syntax is also demonstrated in the provided .sym files:

Function Definitions
~~~~~~~~~~~~~~~~~~~~

From ``integration.sym``:

.. code-block:: symbolic

   fn trapezoid(f, a: Integer || Float, b: Integer || Float, n = 1000) -> Float {
       # Function implementation
   }

Class Definitions
~~~~~~~~~~~~~~~~~

From ``vector.sym``:

.. code-block:: symbolic

   class Vector {
       fn __init__(self, components: [Integer || Float]) {
           self.components = components.map((x) => Float(x))
           self.dimension = components.length()
       }
   }

Constants
~~~~~~~~~

From ``constants.sym``:

.. code-block:: symbolic

   const pi = 3.141592653589793238462643383279502884197
   const e = 2.718281828459045235360287471352662497757

Type Annotations
~~~~~~~~~~~~~~~~

Symbolic supports optional type annotations:

.. code-block:: symbolic

   fn process(x: Integer || Float, items: [String]) -> Boolean {
       # Function with type annotations
   }

The complete lexical structure and token definitions are covered in :doc:`lexicon`.