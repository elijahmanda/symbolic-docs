Modules and Imports
========================

Symbolic supports modular programming by allowing you to organize code into modules. You can use the `import` statement to bring in functions, classes, constants, and other components from external or internal modules.

Importing Entire Modules
------------------------------

You can import an entire module to access its contents. This is useful for bringing in a set of related functions, classes, or constants.

.. code-block:: symbolic

    import math;

    pi = math.PI;
    print("Pi =", pi);

In this example, the entire `math` module is imported, and its constants and functions are accessed using the `math` prefix.

Importing Specific Items
-------------------------------

You can import specific components from a module to avoid unnecessary imports and improve clarity.

.. code-block:: symbolic

    import math::{PI, sqrt};

    print("Pi =", PI);
    print("Square root of 16 =", sqrt(16));

Here, only the `PI` constant and the `sqrt` function from the `math` module are imported.

Importing with Aliases
------------------------------

Use aliases to rename modules or components during import, making code easier to read or avoiding naming conflicts.

.. code-block:: symbolic

    import math as m;

    print("Pi =", m.PI);

In this case, the `math` module is imported with the alias `m`, allowing access to its contents via `m.<component>`.

Importing All Contents from a Module
---------------------------------------------

You can import all elements of a module directly into your current scope, so you don’t need to use the module name as a prefix.

.. code-block:: symbolic

    import math::constants::*;

    print("Pi =", PI);
    print("Euler's number =", E);

Here, all constants from `math::constants` are imported, so you can directly use `PI` and `E` without the `math::constants` prefix.

Importing Multiple Modules
------------------------------------

Symbolic allows you to import from multiple modules in a single statement. This can help organize code and reduce redundancy.

.. code-block:: symbolic

    import core::{io, utils};
    import math::{constants, trigonometry};

    io.print("Hello, Symbolic!");
    utils.log("This is a log message.");
    print("Pi =", constants.PI);
    print("Sine of 30 degrees =", trigonometry.sin(30));

This example imports specific submodules from `core` and `math` to demonstrate how multiple components can be accessed efficiently.

Nested Imports
-------------------------

You can also import specific components from nested modules, allowing for more granular control over what is included.

.. code-block:: symbolic

    import core::{io, utils};
    import math::{constants, algebra::linear};

    io.print("Nested import example");
    print("Linear algebra matrix:", linear.createMatrix([1, 2, 3], [4, 5, 6]));

This example demonstrates how to access deeply nested modules such as `algebra::linear` inside the `math` module.

Module Aliases and Conflicts
-----------------------------------

In case of naming conflicts, you can use aliases to resolve issues and make the code more readable.

.. code-block:: symbolic

    import core::io as c_io;
    import utils::io as u_io;

    c_io.print("Message from core io");
    u_io.print("Message from utils io");

In this case, both `io` from `core` and `io` from `utils` are imported with distinct aliases `c_io` and `u_io`, ensuring there is no conflict.


Key Points:
--------------
- **Modular Programming**: Symbolic supports modular programming, allowing you to split your code into separate modules and import them as needed.
- **Importing Specific Components**: You can import individual components from modules to save memory and improve clarity.
- **Aliasing**: Aliases make it easier to use modules or components with long names or resolve naming conflicts.
- **Multiple Imports**: Symbolic allows importing multiple modules and components in a single statement.
- **Nested Imports**: Nested modules can be imported, allowing you to access specific parts of a module efficiently.
