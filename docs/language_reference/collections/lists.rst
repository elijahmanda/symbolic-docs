Lists
=====

Lists are ordered, mutable sequences that can hold elements of any type.

List Creation
-------------

Basic List Creation
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Empty list
   empty_list = [];
   
   # List with elements
   numbers = [1, 2, 3, 4, 5];
   mixed = [1, "hello", 3.14, true];
   nested = [[1, 2], [3, 4], [5, 6]];
   
   # Using range
   from_range = (1..10).list();
   
   # List comprehension
   squares = [x * x for x in 1..10];
   even_squares = [x * x for x in 1..10 if x % 2 == 0];

List Operations
---------------

Accessing Elements
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   numbers = [10, 20, 30, 40, 50];
   
   first = numbers[0];       # 10
   last = numbers[-1];       # 50
   slice = numbers[1..4];    # [20, 30, 40]
   every_other = numbers[::2]; # [10, 30, 50]

Modifying Lists
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   numbers = [1, 2, 3];
   
   # Append
   numbers.append(4);        # [1, 2, 3, 4]
   
   # Insert
   numbers.insert(1, 1.5);   # [1, 1.5, 2, 3, 4]
   
   # Extend
   numbers.extend([5, 6]);   # [1, 1.5, 2, 3, 4, 5, 6]
   
   # Remove
   numbers.remove(1.5);      # [1, 2, 3, 4, 5, 6]
   
   # Pop
   last = numbers.pop();     # 6, list: [1, 2, 3, 4, 5]
   second = numbers.pop(1);  # 2, list: [1, 3, 4, 5]

List Methods
------------

Searching and Checking
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   numbers = [1, 2, 3, 2, 4, 2];
   
   # Searching
   index = numbers.index(3);     # 2
   count = numbers.count(2);     # 3
   contains = numbers.contains(5); # false
   
   # Checking
   is_empty = numbers.is_empty(); # false
   length = numbers.length();     # 6

Sorting and Reordering
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   numbers = [3, 1, 4, 1, 5, 9, 2];
   
   # Sorting
   ascending = numbers.sorted();          # [1, 1, 2, 3, 4, 5, 9]
   descending = numbers.sorted(reverse=true); # [9, 5, 4, 3, 2, 1, 1]
   
   # Custom sort
   words = ["apple", "banana", "cherry"];
   by_length = words.sorted(key = word => word.length());
   # ["apple", "cherry", "banana"]
   
   # In-place sort
   numbers.sort();  # Modifies original list

Transformation
~~~~~~~~~~~~~~

.. code-block:: symbolic

   numbers = [1, 2, 3, 4, 5];
   
   # Map
   squared = numbers.map(x => x * x);  # [1, 4, 9, 16, 25]
   
   # Filter
   evens = numbers.filter(x => x % 2 == 0);  # [2, 4]
   
   # Reduce
   sum = numbers.reduce((a, b) => a + b);    # 15
   product = numbers.reduce((a, b) => a * b); # 120
   
   # Flat map
   nested = [[1, 2], [3, 4], [5, 6]];
   flat = nested.flat_map(x => x);  # [1, 2, 3, 4, 5, 6]

List Comprehensions
-------------------

Basic Comprehensions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Simple comprehension
   squares = [x * x for x in 1..10];
   
   # With condition
   even_squares = [x * x for x in 1..10 if x % 2 == 0];
   
   # Nested comprehension
   matrix = [[i * j for j in 1..5] for i in 1..3];
   # [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

Advanced Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Multiple generators
   pairs = [(x, y) for x in 1..3 for y in 1..3];
   # [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
   
   # With conditional logic
   results = [
       if x % 2 == 0 then "even" else "odd"
       for x in 1..10
   ];
   
   # Complex conditions
   filtered = [
       x * y
       for x in 1..10
       for y in 1..10
       if x + y == 10 and x < y
   ];

Practical Examples
------------------

Data Processing
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_sales_data(sales) {
       # Filter and transform
       high_value_sales = sales
           .filter(sale => sale.amount > 1000)
           .map(sale => {
               return {
                   id: sale.id,
                   amount: sale.amount,
                   tax: sale.amount * 0.08,
                   net: sale.amount * 0.92
               };
           });
       
       # Calculate statistics
       total_sales = high_value_sales
           .map(sale => sale.amount)
           .sum();
       
       average_sale = total_sales / high_value_sales.length();
       
       return {
           transactions: high_value_sales,
           summary: {
               total: total_sales,
               average: average_sale,
               count: high_value_sales.length()
           }
       };
   }

Matrix Operations
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn matrix_multiply(a, b) {
       if a[0].length() != b.length() {
           throw "Incompatible matrices";
       }
       
       result = [];
       for i in 0..<a.length() {
           row = [];
           for j in 0..<b[0].length() {
               sum = 0;
               for k in 0..<a[0].length() {
                   sum += a[i][k] * b[k][j];
               }
               row.append(sum);
           }
           result.append(row);
       }
       return result;
   }
   
   fn matrix_transpose(matrix) {
       return [
           [matrix[j][i] for j in 0..<matrix.length()]
           for i in 0..<matrix[0].length()
       ];
   }

Text Processing
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_text(text) {
       words = text.split(" ")
           .map(word => word.trim().lower())
           .filter(word => word != "");
       
       # Word frequency
       frequency = {};
       for word in words {
           frequency[word] = (frequency[word] or 0) + 1;
       }
       
       # Top 10 words
       top_words = frequency.entries()
           .sorted((a, b) => b[1] - a[1])
           .take(10)
           .map(entry => entry[0]);
       
       return {
           word_count: words.length(),
           unique_words: frequency.keys().length(),
           top_words: top_words,
           frequency: frequency
       };
   }

Game Development
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Inventory {
       items = [];
       
       fn add_item(item) {
           # Check if item already exists and stack
           existing = self.items.find(i => i.id == item.id);
           if existing != null and existing.is_stackable() {
               existing.quantity += item.quantity;
           } else {
               self.items.append(item);
           }
       }
       
       fn remove_item(item_id, quantity = 1) {
           item = self.items.find(i => i.id == item_id);
           if item != null {
               if item.quantity > quantity {
                   item.quantity -= quantity;
               } else {
                   self.items.remove(item);
               }
               return true;
           }
           return false;
       }
       
       fn get_sorted_inventory(sort_by = "name") {
           return self.items.sorted((a, b) => 
               match sort_by {
                   "name" => a.name.compare(b.name);
                   "value" => b.value - a.value;
                   "weight" => a.weight - b.weight;
                   _ => a.id - b.id;
               }
           );
       }
   }

Performance Tips
----------------

Preallocate Lists When Possible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - preallocate known size
   results = [].fill(0, 1000);  # List of 1000 zeros
   for i in 0..<1000 {
       results[i] = calculate(i);
   }
   
   # Less efficient - append in loop
   results = [];
   for i in 0..<1000 {
       results.append(calculate(i));  # May cause reallocations
   }

Use List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - comprehension is optimized
   squares = [x * x for x in 1..1000];
   
   # Less efficient - manual loop
   squares = [];
   for x in 1..1000 {
       squares.append(x * x);
   }

Avoid Unnecessary Copies
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - modify in place when possible
   numbers.sort();  # In-place sort
   
   # Creates new list
   sorted_numbers = numbers.sorted();  # New list

Use Built-in Methods
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - use built-in reduce
   total = numbers.reduce(+, 0);
   
   # Less efficient - manual accumulation
   total = 0;
   for num in numbers {
       total += num;
   }