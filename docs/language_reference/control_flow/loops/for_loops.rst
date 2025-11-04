For Loops
=========

For loops iterate over sequences, ranges, and collections with various iteration patterns.

Basic For Loop over Collections
-------------------------------

Iterating over Lists
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fruits = ["apple", "banana", "cherry"];
   for fruit in fruits {
       print(fruit);
   }
   # Output: apple, banana, cherry

Iterating over Strings
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   word = "hello";
   for char in word {
       print(char);
   }
   # Output: h, e, l, l, o

Iterating with Index
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   colors = ["red", "green", "blue"];
   for i, color in colors.enumerate() {
       print($"Color {i}: {color}");
   }
   # Output: Color 0: red, Color 1: green, Color 2: blue

Range-based For Loops
---------------------

Inclusive Range (..)
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Count from 1 to 5 (inclusive)
   for i in 1..5 {
       print(i);
   }
   # Output: 1, 2, 3, 4, 5

Exclusive Range (..<)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Count from 0 to 4 (exclusive of 5)
   for i in 0..<5 {
       print(i);
   }
   # Output: 0, 1, 2, 3, 4

With Step
~~~~~~~~~

.. code-block:: symbolic

   # Count by 2s
   for i in 0..10, 2 {
       print(i);
   }
   # Output: 0, 2, 4, 6, 8, 10

   # Count backwards
   for i in 10..0, -1 {
       print(i);
   }
   # Output: 10, 9, 8, ..., 0

Traditional For Loop
--------------------

Initializer, Condition, Step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Traditional C-style for loop
   for i = 0, i < 5, 1 {
       print(i);
   }
   # Output: 0, 1, 2, 3, 4

   # With different step
   for i = 0, i <= 10, 2 {
       print(i);
   }
   # Output: 0, 2, 4, 6, 8, 10

   # Counting down
   for i = 10, i > 0, -1 {
       print(i);
   }
   # Output: 10, 9, 8, ..., 1

Destructuring in For Loops
--------------------------

Tuple Destructuring
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   points = [(1, 2), (3, 4), (5, 6)];
   for (x, y) in points {
       print($"Point at ({x}, {y})");
   }
   # Output: Point at (1, 2), Point at (3, 4), Point at (5, 6)

List Destructuring
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   coordinates = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
   for [x, y, z] in coordinates {
       print($"3D point: ({x}, {y}, {z})");
   }

Object Destructuring
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   users = [
       {name: "Alice", age: 30},
       {name: "Bob", age: 25},
       {name: "Charlie", age: 35}
   ];
   for {name, age} in users {
       print($"User: {name}, Age: {age}");
   }

Practical Examples
------------------

Mathematical Sequences
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Calculate factorial
   fn factorial(n) {
       result = 1;
       for i in 1..n {
           result *= i;
       }
       return result;
   }
   
   for n in 1..10 {
       print($"Factorial of {n} is {factorial(n)}");
   }

Data Processing
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process student records
   students = [
       {name: "Alice", grades: [85, 92, 78]},
       {name: "Bob", grades: [72, 65, 80]},
       {name: "Charlie", grades: [90, 88, 94]}
   ];
   
   for student in students {
       total = 0;
       count = 0;
       for grade in student.grades {
           total += grade;
           count += 1;
       }
       average = total / count;
       print($"Student: {student.name}, Average: {average:.1f}");
   }

Matrix Operations
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Matrix multiplication
   matrix_a = [[1, 2, 3], [4, 5, 6]];
   matrix_b = [[7, 8], [9, 10], [11, 12]];
   
   result = [];
   for i in 0..<len(matrix_a) {
       row = [];
       for j in 0..<len(matrix_b[0]) {
           sum = 0;
           for k in 0..<len(matrix_a[0]) {
               sum += matrix_a[i][k] * matrix_b[k][j];
           }
           row.append(sum);
       }
       result.append(row);
   }
   print(result);  # [[58, 64], [139, 154]]

File Processing
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process lines in a file (conceptual)
   fn process_log_file(filename) {
       lines = read_file_lines(filename);
       error_count = 0;
       warning_count = 0;
       
       for line_num, line in lines.enumerate() {
           if "ERROR" in line {
               error_count += 1;
               print($"Error on line {line_num}: {line}");
           } else if "WARNING" in line {
               warning_count += 1;
           }
       }
       
       print($"Total errors: {error_count}, warnings: {warning_count}");
   }

Nested Loop Patterns
--------------------

Multiplication Table
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Generate multiplication table
   for i in 1..10 {
       for j in 1..10 {
           product = i * j;
           print($"${i} × ${j} = ${product:>2}", end="  ");
       }
       print();  # New line after each row
   }

Pattern Generation
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Generate pyramid pattern
   rows = 5;
   for i in 1..rows {
       # Print spaces
       for j in 1..<(rows - i) {
           print(" ", end="");
       }
       # Print stars
       for k in 1..<(2 * i) {
           print("*", end="");
       }
       print();
   }

Performance Considerations
--------------------------

Precompute Loop Bounds
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - precompute length
   items = large_list;
   count = len(items);
   for i in 0..<count {
       process(items[i]);
   }
   
   # Avoid - recomputing length each iteration
   for i in 0..<len(large_list) {
       process(large_list[i]);
   }

Use Built-in Functions When Possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - use built-in map
   squared = numbers.map(x => x * x);
   
   # Less efficient - manual loop
   squared = [];
   for num in numbers {
       squared.append(num * num);
   }