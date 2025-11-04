Ranges
======

Ranges in Symbolic provide a powerful way to work with sequences of numbers, characters, and custom types with inclusive and exclusive bounds.

Range Creation
--------------

Numeric Ranges
~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Inclusive range (1 through 5)
   inclusive = 1..5;
   print(inclusive.list());  # [1, 2, 3, 4, 5]

   # Exclusive range (1 through 4)
   exclusive = 1..<5;
   print(exclusive.list());  # [1, 2, 3, 4]

   # With step
   even_numbers = 0..10, 2;
   print(even_numbers.list());  # [0, 2, 4, 6, 8, 10]

   # Negative step
   countdown = 10..0, -1;
   print(countdown.list());  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Character Ranges
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Alphabet ranges
   lowercase = 'a'..'z';
   print(lowercase.list());  # ['a', 'b', 'c', ..., 'z']

   uppercase = 'A'..'Z';
   vowels = 'a'..<'f';  # ['a', 'b', 'c', 'd', 'e']

   # Custom character sequences
   hex_digits = '0'..'9' + 'a'..'f';
   print(hex_digits.list());  # ['0','1',...,'9','a','b',...,'f']

Infinite Ranges
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Infinite range from 1
   naturals = 1..;
   first_10 = naturals.take(10);  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   # Infinite range with step
   multiples_of_3 = 0.., 3;
   first_5_multiples = multiples_of_3.take(5);  # [0, 3, 6, 9, 12]

Range Operations
----------------

Membership Testing
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   age = 25;
   if age in 18..65 {
       print("Working age");
   }

   grade = 'B';
   if grade in 'A'..'C' {
       print("Passing grade");
   }

   # Checking bounds
   range = 10..20;
   contains_15 = 15 in range;  # true
   contains_5 = 5 in range;    # false

Range Properties
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   range = 5..15;
   
   start = range.start;      # 5
   end = range.end;          # 15
   step = range.step;        # 1
   is_inclusive = range.is_inclusive;  # true
   length = range.length();  # 11

Range Transformation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   base_range = 1..10;
   
   # Map operation
   squared = base_range.map(x => x * x);
   print(squared.list());  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

   # Filter operation
   evens = base_range.filter(x => x % 2 == 0);
   print(evens.list());  # [2, 4, 6, 8, 10]

   # Slice ranges
   first_half = base_range[..5];    # 1..5
   second_half = base_range[5..];   # 6..10
   middle = base_range[3..7];       # 4..8

Set Operations
--------------

Union and Intersection
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   teens = 13..19;
   adults = 18..65;
   
   # Intersection
   young_adults = teens.intersect(adults);  # 18..19
   
   # Union
   all_ages = teens.union(adults);  # 13..65
   
   # Difference
   only_teens = teens.difference(adults);  # 13..17

Complement
~~~~~~~~~~

.. code-block:: symbolic

   valid_ages = 0..150;
   working_ages = 18..65;
   
   # Ages not in working range
   non_working = valid_ages.complement(working_ages);
   # 0..17 + 66..150

Practical Examples
------------------

Date Ranges
~~~~~~~~~~~

.. code-block:: symbolic

   fn generate_date_range(start_date, end_date, step_days = 1) {
       dates = [];
       current = start_date;
       
       while current <= end_date {
           dates.append(current);
           current = current.add_days(step_days);
       }
       
       return dates;
   }
   
   # Generate business days (conceptual)
   business_days = start_date..end_date
       .filter(date => !date.is_weekend() and !date.is_holiday());

Grade Management
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn assign_grade(score) {
       return match score {
           in 90..100 => "A";
           in 80..<90 => "B";
           in 70..<80 => "C";
           in 60..<70 => "D";
           in 0..<60 => "F";
           _ => "Invalid score";
       };
   }
   
   fn calculate_gpa(grades) {
       grade_points = {
           "A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0
       };
       
       total_points = grades
           .map(grade => grade_points[grade])
           .sum();
       
       return total_points / grades.length();
   }

Inventory Management
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn check_inventory_levels(products) {
       for product in products {
           stock_level = product.current_stock;
           ideal_range = product.min_stock..product.max_stock;
           
           match stock_level {
               in ideal_range => 
                   print($"${product.name}: Adequate stock");
               in ..<product.min_stock => 
                   print($"${product.name}: LOW STOCK - Reorder needed");
               in (product.max_stock..) => 
                   print($"${product.name}: OVERSTOCK - Consider discount");
           }
       }
   }

Sensor Monitoring
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn monitor_temperature_sensors(sensors) {
       normal_range = 18..25;  # Celsius
       warning_range = 15..<18 + 25..<30;
       critical_range = ..<15 + 30..;
       
       for sensor in sensors {
           temp = sensor.read_temperature();
           
           match temp {
               in normal_range => 
                   log_normal(sensor, temp);
               in warning_range => 
                   log_warning(sensor, temp);
               in critical_range => 
                   trigger_alert(sensor, temp);
           }
       }
   }

Financial Ranges
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn categorize_transactions(transactions) {
       ranges = {
           "small": 0..<100,
           "medium": 100..<1000,
           "large": 1000..<10000,
           "very_large": 10000..
       };
       
       categories = {};
       for range_name, range in ranges {
           categories[range_name] = transactions
               .filter(t => t.amount in range)
               .map(t => t.amount)
               .sum();
       }
       
       return categories;
   }

Advanced Range Patterns
-----------------------

Custom Range Types
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Date range implementation
   class DateRange {
       fn __init__(self, start_date, end_date, inclusive = true) {
           self.start_date = start_date;
           self.end_date = end_date;
           self.inclusive = inclusive;
       }
       
       fn contains(self, date) {
           if self.inclusive {
               return self.start_date <= date <= self.end_date;
           } else {
               return self.start_date <= date < self.end_date;
           }
       }
       
       fn __iter__(self) {
           current = self.start_date;
           while self.contains(current) {
               yield current;
               current = current.add_days(1);
           }
       }
   }

Lazy Range Evaluation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Fibonacci sequence as infinite range
   fib_range = {
       a, b = 0, 1;
       loop {
           yield a;
           (a, b) = (b, a + b);
       }
   };
   
   first_10_fib = fib_range.take(10);  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Range Partitioning
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn partition_data(data, partition_ranges) {
       partitions = {};
       
       for item in data {
           for range_name, range in partition_ranges {
               if item.value in range {
                   partitions[range_name].append(item);
                   stop;  # Found matching range
               }
           }
       }
       
       return partitions;
   }
   
   # Usage: Partition sales by amount
   sales_ranges = {
       "small": 0..<50,
       "medium": 50..<200,
       "large": 200..<1000,
       "enterprise": 1000..
   };
   
   sales_partitions = partition_data(sales_data, sales_ranges);

Performance Optimization
------------------------

Lazy Range Generation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - lazy evaluation for large ranges
   large_range = 1..1_000_000;
   processed = large_range
       .filter(x => x % 2 == 0)
       .map(x => x * 2)
       .take(100);  # Only processes first 100 elements

Range vs List
~~~~~~~~~~~~~

.. code-block:: symbolic

   # Use ranges for large sequences
   for i in 1..1_000_000 {
       # Memory efficient - doesn't create actual list
   }
   
   # Use lists when you need random access
   small_list = (1..100).list();
   middle_element = small_list[50];

Best Practices
--------------

Use Descriptive Range Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - descriptive names
   valid_ages = 0..150;
   working_ages = 18..65;
   retirement_ages = 66..;
   
   # Avoid - magic numbers
   if age in 18..65 {  # What do these numbers mean?
       # ...
   }

Prefer Inclusive Ranges for Clarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - clear boundaries
   valid_scores = 0..100;
   passing_scores = 60..100;
   
   # Less clear - exclusive upper bound
   valid_scores = 0..<101;

Use Range Patterns in Match Statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn categorize_temperature(temp) {
       return match temp {
           in ..<0 => "freezing";
           in 0..<10 => "cold";
           in 10..<20 => "cool";
           in 20..<30 => "warm";
           in 30.. => "hot";
       };
   }