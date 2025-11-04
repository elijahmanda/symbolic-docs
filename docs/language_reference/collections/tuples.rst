Tuples
======

Tuples are immutable, ordered sequences that can hold elements of any type. They are ideal for fixed collections of related values.

Tuple Creation
--------------

Basic Tuple Creation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Empty tuple
   empty = ();
   
   # Single element tuple (note the comma)
   single = (42,);
   not_a_tuple = (42);  # This is just the number 42
   
   # Multiple elements
   coordinates = (3, 4);
   person = ("Alice", 30, "Engineer");
   mixed = (1, "hello", 3.14, true);
   
   # From other collections
   from_list = tuple([1, 2, 3]);
   from_range = tuple(1..5);

Tuple Unpacking
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Basic unpacking
   point = (10, 20);
   x, y = point;
   print(x);  # 10
   print(y);  # 20
   
   # Extended unpacking
   numbers = (1, 2, 3, 4, 5);
   first, *middle, last = numbers;
   print(first);   # 1
   print(middle);  # [2, 3, 4]
   print(last);    # 5
   
   # Ignoring elements
   name, _, profession = ("Bob", 25, "Designer");
   print(name);       # "Bob"
   print(profession); # "Designer"

Tuple Operations
----------------

Accessing Elements
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   data = ("apple", "banana", "cherry", "date");
   
   # Indexing
   first = data[0];     # "apple"
   last = data[-1];     # "date"
   second = data[1];    # "banana"
   
   # Slicing
   first_two = data[0..2];   # ("apple", "banana")
   last_two = data[2..];     # ("cherry", "date")
   every_other = data[::2];  # ("apple", "cherry")

Tuple Methods
-------------

Basic Methods
~~~~~~~~~~~~~

.. code-block:: symbolic

   colors = ("red", "green", "blue", "green");
   
   # Count occurrences
   green_count = colors.count("green");  # 2
   red_count = colors.count("red");      # 1
   
   # Find index
   green_index = colors.index("green");  # 1
   blue_index = colors.index("blue");    # 2
   
   # Length
   size = colors.length();  # 4

Tuple Properties
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   data = (1, 2, 3);
   
   # Immutability check
   is_immutable = data.is_immutable();  # true
   
   # Hashability (if all elements are hashable)
   is_hashable = data.is_hashable();    # true
   
   # Conversion to other types
   as_list = data.list();    # [1, 2, 3]
   as_set = data.set();      # {1, 2, 3}
   as_string = data.to_string();  # "(1, 2, 3)"

Practical Examples
------------------

Function Return Values
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_numbers(numbers) {
       if numbers.is_empty() {
           return (0, 0, 0, 0);  # count, sum, min, max
       }
       
       count = numbers.length();
       total = numbers.sum();
       minimum = numbers.min();
       maximum = numbers.max();
       
       return (count, total, minimum, maximum);
   }
   
   data = [10, 20, 30, 40, 50];
   count, total, min_val, max_val = analyze_numbers(data);
   
   print($"Count: {count}, Total: {total}");
   print($"Range: {min_val} - {max_val}");

Coordinate Systems
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_line_properties(point1, point2) {
       x1, y1 = point1;
       x2, y2 = point2;
       
       # Calculate slope and intercept
       if x1 == x2 {
           return (∞, x1);  # Vertical line
       }
       
       slope = (y2 - y1) / (x2 - x1);
       intercept = y1 - slope * x1;
       
       return (slope, intercept);
   }
   
   fn midpoint(point1, point2) {
       x1, y1 = point1;
       x2, y2 = point2;
       
       mid_x = (x1 + x2) / 2;
       mid_y = (y1 + y2) / 2;
       
       return (mid_x, mid_y);
   }
   
   # Usage
   line = calculate_line_properties((0, 0), (4, 4));
   center = midpoint((1, 1), (5, 5));
   print($"Line: y = {line[0]}x + {line[1]}");
   print($"Midpoint: {center}");

Database Records
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_user_records(records) {
       valid_users = [];
       errors = [];
       
       for record in records {
           match record {
               (id, name, email) if is_valid_email(email) => {
                   user = {
                       "id": id,
                       "name": name,
                       "email": email
                   };
                   valid_users.append(user);
               }
               (id, name, email) => {
                   errors.append(($"Invalid email for user {id}", email));
               }
               _ => {
                   errors.append(("Malformed record", record));
               }
           }
       }
       
       return (valid_users, errors);
   }
   
   # Simulated database records
   user_records = [
       (1, "Alice", "alice@example.com"),
       (2, "Bob", "invalid-email"),
       (3, "Charlie", "charlie@test.org")
   ];
   
   valid, errors = process_user_records(user_records);
   print($"Valid users: {valid.length()}");
   print($"Errors: {errors.length()}");

Color Systems
~~~~~~~~~~~~~

.. code-block:: symbolic

   # RGB color operations
   fn blend_colors(color1, color2, ratio = 0.5) {
       r1, g1, b1 = color1;
       r2, g2, b2 = color2;
       
       r = r1 * (1 - ratio) + r2 * ratio;
       g = g1 * (1 - ratio) + g2 * ratio;
       b = b1 * (1 - ratio) + b2 * ratio;
       
       return (r.round(), g.round(), b.round());
   }
   
   fn calculate_luminance(color) {
       r, g, b = color;
       # Standard luminance formula
       return 0.299 * r + 0.587 * g + 0.114 * b;
   }
   
   # Usage
   red = (255, 0, 0);
   blue = (0, 0, 255);
   purple = blend_colors(red, blue, 0.5);
   print($"Purple: {purple}");  # (128, 0, 128)

Time and Date Handling
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn parse_date_time(datetime_str) {
       # Parse "YYYY-MM-DD HH:MM:SS" format
       parts = datetime_str.split(" ");
       date_parts = parts[0].split("-");
       time_parts = parts[1].split(":");
       
       year = date_parts[0].to_int();
       month = date_parts[1].to_int();
       day = date_parts[2].to_int();
       hour = time_parts[0].to_int();
       minute = time_parts[1].to_int();
       second = time_parts[2].to_int();
       
       return (year, month, day, hour, minute, second);
   }
   
   fn format_duration(seconds) {
       hours = seconds // 3600;
       minutes = (seconds % 3600) // 60;
       secs = seconds % 60;
       
       return (hours, minutes, secs);
   }
   
   # Usage
   datetime = parse_date_time("2024-01-15 14:30:25");
   duration = format_duration(3665);  # 1 hour, 1 minute, 5 seconds
   print($"Date: {datetime[0]}-{datetime[1]}-{datetime[2]}");
   print($"Duration: {duration[0]}h {duration[1]}m {duration[2]}s");

Matrix Operations
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn matrix_dimensions(matrix) {
       rows = matrix.length();
       if rows == 0 {
           return (0, 0);
       }
       cols = matrix[0].length();
       return (rows, cols);
   }
   
   fn matrix_transpose(matrix) {
       rows, cols = matrix_dimensions(matrix);
       result = [];
       
       for j in 0..<cols {
           new_row = [];
           for i in 0..<rows {
               new_row.append(matrix[i][j]);
           }
           result.append(tuple(new_row));
       }
       
       return tuple(result);
   }
   
   # Usage
   original = (
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9)
   );
   
   transposed = matrix_transpose(original);
   print("Original:");
   for row in original {
       print(row);
   }
   print("Transposed:");
   for row in transposed {
       print(row);
   }

Advanced Patterns
-----------------

Named Tuples
~~~~~~~~~~~~

.. code-block:: symbolic

   # Using pattern matching as named tuples
   fn process_person_data(data) {
       match data {
           (name, age, "student") => 
               print($"Student {name}, age {age}");
           (name, age, "teacher") => 
               print($"Teacher {name}, age {age}");
           (name, age, role) => 
               print($"${role.capitalize()} {name}, age {age}");
       }
   }

Tuple as Dictionary Keys
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Using tuples as dictionary keys
   color_palettes = {
       ("red", "green", "blue"): "RGB",
       ("cyan", "magenta", "yellow", "black"): "CMYK",
       ("hue", "saturation", "lightness"): "HSL"
   };
   
   point_distances = {};
   points = [(1, 1), (2, 3), (4, 5)];
   
   for i in 0..<points.length() {
       for j in (i + 1)..<points.length() {
           key = (points[i], points[j]);
           distance = calculate_distance(points[i], points[j]);
           point_distances[key] = distance;
       }
   }

Error Handling with Tuples
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn safe_divide(a, b) {
       if b == 0 {
           return (false, "Division by zero", null);
       }
       return (true, null, a / b);
   }
   
   fn process_calculation(x, y) {
       success, error, result = safe_divide(x, y);
       
       if !success {
           print($"Error: {error}");
           return null;
       }
       
       return result * 2;
   }

Performance Benefits
--------------------

Memory Efficiency
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Tuples are more memory efficient than lists
   large_tuple = tuple(1..1000000);
   large_list = (1..1000000).list();
   
   # tuple memory < list memory
   tuple_size = large_tuple.memory_size();
   list_size = large_list.memory_size();

Hashability
~~~~~~~~~~~

.. code-block:: symbolic

   # Tuples can be used as dictionary keys
   coordinates_map = {
       (0, 0): "origin",
       (1, 0): "east",
       (0, 1): "north",
       (-1, 0): "west",
       (0, -1): "south"
   };
   
   position = (1, 0);
   print(coordinates_map[position]);  # "east"

Immutability Advantages
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Thread-safe and predictable
   constants = (
       ("pi", 3.14159),
       ("e", 2.71828),
       ("gravity", 9.81)
   );
   
   # Can be safely shared between threads
   # No risk of accidental modification

Best Practices
--------------

Use Tuples for Heterogeneous Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - different types of related data
   person = ("Alice", 30, "Engineer");  # name, age, profession
   point = (x, y);                      # coordinates
   date = (2024, 1, 15);                # year, month, day
   
   # Avoid - homogeneous data better as list
   numbers = [1, 2, 3, 4, 5];           # Use list for same type

Use Descriptive Unpacking
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - descriptive variable names
   name, age, profession = person;
   x, y = coordinates;
   year, month, day = date;
   
   # Avoid - unclear meaning
   a, b, c = person;

Prefer Tuples for Fixed-Size Collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - fixed number of elements
   rgb_color = (255, 128, 0);
   gps_coordinates = (40.7128, -74.0060);
   
   # Use lists for variable-sized collections
   scores = [85, 92, 78, 96];  # Number of scores may vary