Loop Control
============

Loop control statements allow you to change the normal execution flow within loops.

Break Statement (stop)
----------------------

Exiting Loops Early
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Search for a value and exit when found
   numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8];
   target = 7;
   
   for num in numbers {
       if num == target {
           print("Found the target!");
           stop;  # break out of loop
       }
       print($"Checking {num}");
   }

Breaking Nested Loops
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ];
   target = 5;
   
   outer: for i in 0..<len(matrix) {
       for j in 0..<len(matrix[i]) {
           if matrix[i][j] == target {
               print($"Found {target} at position ({i}, {j})");
               stop outer;  # break both loops
           }
       }
   }

Continue Statement (skip)
-------------------------

Skipping Iterations
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process only even numbers
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
   
   for num in numbers {
       if num % 2 != 0 {
           skip;  # continue to next iteration
       }
       print($"Processing even number: {num}");
   }
   # Output: Processing even number: 2, 4, 6, 8, 10

Skipping with Condition
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process valid data, skip invalid
   data_points = [10, -5, 20, -1, 30, 0, 40];
   
   for value in data_points {
       if value <= 0 {
           print($"Skipping invalid value: {value}");
           skip;
       }
       result = complex_calculation(value);
       print($"Result for {value}: {result}");
   }

Practical Examples
------------------

Data Validation and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_user_data(users) {
       valid_users = [];
       
       for user in users {
           # Skip users with missing required fields
           if user.name == "" or user.email == "" {
               print("Skipping user with missing data");
               skip;
           }
           
           # Skip invalid email formats
           if !is_valid_email(user.email) {
               print($"Skipping user with invalid email: {user.email}");
               skip;
           }
           
           # Stop processing if too many errors
           if error_count > 10 {
               print("Too many errors, stopping processing");
               stop;
           }
           
           valid_users.append(user);
       }
       
       return valid_users;
   }

Search Algorithms
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn find_pair_with_sum(numbers, target_sum) {
       # Find two numbers that add up to target_sum
       for i in 0..<len(numbers) {
           for j in (i + 1)..<len(numbers) {
               if numbers[i] + numbers[j] == target_sum {
                   print($"Found pair: {numbers[i]} + {numbers[j]} = {target_sum}");
                   stop;  # Found first pair, exit early
               }
           }
       }
   }

   numbers = [1, 4, 2, 7, 3, 9, 5];
   find_pair_with_sum(numbers, 10);  # Finds 1 + 9

File Processing with Early Exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn search_in_files(files, search_term, max_results = 10) {
       results = [];
       
       for file in files {
           if !file.exists() {
               print($"Skipping missing file: {file}");
               skip;
           }
           
           content = file.read();
           lines = content.split("\n");
           
           for line_num, line in lines.enumerate() {
               if search_term in line {
                   results.append({file: file.name, line: line_num + 1, content: line});
                   
                   if len(results) >= max_results {
                       print("Reached maximum results limit");
                       stop;  # Exit both loops
                   }
               }
           }
       }
       
       return results;
   }

Prime Number Check
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn is_prime(n) {
       if n < 2 {
           return false;
       }
       
       for i in 2..<(n.sqrt().to_int() + 1) {
           if n % i == 0 {
               return false;  # Found a divisor, not prime
           }
       }
       
       return true;
   }

   # Find first N prime numbers
   fn find_primes(limit) {
       primes = [];
       num = 2;
       
       while len(primes) < limit {
           if is_prime(num) {
               primes.append(num);
           }
           num += 1;
       }
       
       return primes;
   }

Menu System with Exit
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn interactive_menu() {
       while true {
           print("\n1. Add item");
           print("2. Remove item");
           print("3. List items");
           print("4. Exit");
           
           choice = input("Choose option: ");
           
           match choice {
               "1" => add_item();
               "2" => remove_item();
               "3" => list_items();
               "4" => {
                   print("Goodbye!");
                   stop;  # Exit the while loop
               }
               _ => {
                   print("Invalid choice. Please try again.");
                   skip;  # Continue to next iteration
               }
           }
       }
   }

Data Filtering Pipeline
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_sensor_data(readings) {
       clean_data = [];
       
       for reading in readings {
           # Skip null readings
           if reading == null {
               skip;
           }
           
           # Skip out-of-range values
           if reading.value < reading.min_range or reading.value > reading.max_range {
               print($"Skipping out-of-range reading: {reading.value}");
               skip;
           }
           
           # Stop if sensor error detected
           if reading.error_code != 0 {
               print($"Sensor error detected: {reading.error_code}");
               stop;
           }
           
           clean_data.append(reading);
       }
       
       return clean_data;
   }

Performance Optimization
------------------------

Early Exit in Search
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Efficient - stops when found
   fn contains_value(items, target) {
       for item in items {
           if item == target {
               return true;
           }
       }
       return false;
   }

Skipping Unnecessary Work
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Only process relevant data
   fn analyze_data(data, threshold) {
       results = [];
       
       for record in data {
           # Skip records that don't meet threshold
           if record.score < threshold {
               skip;
           }
           
           # Expensive processing only on relevant records
           analysis = expensive_analysis(record);
           results.append(analysis);
       }
       
       return results;
   }

Best Practices
--------------

Use Stop for Early Success
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - exit early when condition met
   fn find_first_match(items, predicate) {
       for item in items {
           if predicate(item) {
               return item;  # Implicit stop
           }
       }
       return null;
   }

Use Skip for Filtering
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - skip invalid items clearly
   for item in data {
       if !is_valid(item) {
           skip;
       }
       process(item);
   }

Avoid Deeply Nested Breaks
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Consider refactoring deeply nested breaks
   fn complex_search(data) {
       for outer in data {
           for middle in outer {
               for inner in middle {
                   if complex_condition(inner) {
                       # Instead of triple break, return
                       return inner;
                   }
               }
           }
       }
       return null;
   }