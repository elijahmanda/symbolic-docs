Object Model
============

The Symbolic language uses a unified object model where all values are objects inheriting from ``SymbolicObject``.

SymbolicObject Base Class
-------------------------

All objects in Symbolic inherit from the ``SymbolicObject`` base class (defined in ``symbolic_object.py``), which provides:

* Common methods and operators
* Type information and introspection
* Serialization and display capabilities
* Protocol implementations

Core Types
----------

The language provides several built-in types that extend ``SymbolicObject``:

Numbers
~~~~~~~

Defined in ``numbers.py``, supports:

* **Integers**: Arbitrary precision integers
* **Floats**: High-precision floating point (using mpmath)
* **Complex**: Complex numbers with real and imaginary parts
* **Rational**: Exact rational numbers (planned)

.. code-block:: symbolic

   x = 5              # Integer
   y = 3.14           # Float  
   z = 2 + 3i         # Complex
   ratio = 1/3        # Rational

Strings
~~~~~~~

Defined in ``strings.py``, provides:

* Unicode support
* String methods (slicing, searching, manipulation)
* Immutable string objects

.. code-block:: symbolic

   s = "hello"
   name = 'Symbolic'
   multi = """multi-line
   string"""

Collections
~~~~~~~~~~~

Defined in ``collections.py``, includes:

* **Lists**: Ordered, mutable sequences
* **Dictionaries**: Key-value mappings
* **Sets**: Unordered collections of unique elements
* **Tuples**: Immutable sequences

.. code-block:: symbolic

   list = [1, 2, 3]
   dict = {"a": 1, "b": 2}
   set = {1, 2, 3}
   tuple = (1, 2, 3)

Type System Features
--------------------

Type Inheritance
~~~~~~~~~~~~~~~~

All types form a hierarchy with ``SymbolicObject`` at the root:

.. code-block:: text

   SymbolicObject
   ├── Number
   │   ├── Integer
   │   ├── Float
   │   └── Complex
   ├── String
   ├── Boolean
   └── Collection
       ├── List
       ├── Dictionary
       ├── Set
       └── Tuple

Dynamic Typing with Optional Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Symbolic is dynamically typed but supports optional type annotations:

.. code-block:: symbolic

   # Dynamic typing
   x = 5        # x is Integer
   x = "hello"  # x is now String
   
   # Type annotations
   fn process(data: [Integer]) -> Boolean {
       # Annotated function
   }

Protocol-based Polymorphism
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objects implement protocols rather than relying on classical inheritance:

.. code-block:: symbolic

   # Any object with __str__ can be printed
   fn print_all(items: [SymbolicObject]) {
       for item in items {
           print(item.__str__())
       }
   }

Common Methods
--------------

All ``SymbolicObject`` instances provide these common methods:

String Representation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   obj.__str__()     # User-friendly string
   obj.__repr__()    # Developer representation

Comparison
~~~~~~~~~~

.. code-block:: symbolic

   obj.__eq__(other)  # Equality
   obj.__neq__(other) # Inequality
   obj.__lt__(other)  # Less than
   # ... other comparisons

Serialization
~~~~~~~~~~~~~

.. code-block:: symbolic

   obj.serialize()    # Convert to portable format
   obj.deserialize(data)  # Recreate from serialized data

Type Information
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   obj.type_name()    # Get type as string
   obj.is_type(type)  # Check if instance of type
   obj.attributes()   # Get available attributes

Operator Overloading
--------------------

Types can overload operators by implementing special methods:

Arithmetic Operators
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   obj.__add__(other)      # +
   obj.__sub__(other)      # -
   obj.__mul__(other)      # *
   obj.__div__(other)      # /
   obj.__pow__(other)      # ^

Comparison Operators
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   obj.__eq__(other)       # ==
   obj.__lt__(other)       # <
   obj.__gt__(other)       # >
   # ... etc

Container Protocols
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   obj.__getitem__(key)    # [key]
   obj.__setitem__(key, value)  # [key] = value
   obj.__len__()           # Length
   obj.__contains__(item)  # in operator

Example Type Implementations
----------------------------

From the provided .sym files:

Vector Class
~~~~~~~~~~~~

The ``Vector`` class from ``vector.sym`` demonstrates a user-defined type:

.. code-block:: symbolic

   class Vector {
       fn __init__(self, components: [Integer || Float]) {
           self.components = components.map((x) => Float(x))
           self.dimension = components.length()
       }
       
       fn dot(self, other: Vector) {
           # Dot product implementation
           return (0..<self.dimension)
               |> ((i) -> self.components[i] * other.components[i])
               .reduce((a, b) => a + b)
       }
   }

Mathematical Constants
~~~~~~~~~~~~~~~~~~~~~~

Constants from ``constants.sym`` show immutable value objects:

.. code-block:: symbolic

   const pi = 3.141592653589793238462643383279502884197
   const e = 2.718281828459045235360287471352662497757

Integration Functions
~~~~~~~~~~~~~~~~~~~~~

Functions from ``integration.sym`` demonstrate functional programming:

.. code-block:: symbolic

   fn trapezoid(f, a: Integer || Float, b: Integer || Float, n = 1000) -> Float {
       # Numerical integration implementation
   }

The object model provides a consistent foundation for all Symbolic programs. Continue to :doc:`types/index` for detailed type documentation.