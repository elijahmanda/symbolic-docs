Basic Syntax
============

The Symbolic language is designed with simplicity in mind, featuring clear and intuitive syntax rules. Below are the key syntax elements you need to understand when writing Symbolic code:

- **Statements**: Each individual statement is terminated by a semicolon (`;`). This indicates the end of an operation and allows for clear separation of statements. For example, variable assignments, function calls, and control structures all end with a semicolon.
  
- **Blocks**: Code blocks, such as the body of functions, loops, and conditionals, are enclosed in curly braces (`{}`). These braces define the scope of the block, grouping related statements together.

- **Comments**: 
  - **Single-line comments**: Use the hash symbol (`#`) to start a comment on a single line. Everything following the hash symbol on that line will be ignored by the interpreter. This is useful for brief explanations or notes within your code.
  - **Multi-line comments**: Symbolic supports multi-line comments using the /* */ syntax. Any text enclosed within these delimiters will be treated as a comment, allowing for comments that span multiple lines.

Example
----------

Below is an example demonstrating the basic syntax in Symbolic:

.. code-block:: symbolic

   # This is a single-line comment explaining the next line of code
   print("Hello, Symbolic!");  # This comment is at the end of a line of code

   # Variable assignment
   x = 5;  # Assigning 5 to variable x

   # Function call
   result = some_function(x);  # Calling a function with argument x
   /*
       This is a multi-line comment
       in Symbolic.
       It can span multiple lines.
   */

