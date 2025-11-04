Strings
=======

Strings in Symbolic are sequences of Unicode characters with extensive manipulation capabilities.

String Creation
---------------

Basic String Literals
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   single_quoted = 'Hello World';
   double_quoted = "Hello World";
   print(single_quoted);  # Hello World
   print(double_quoted);  # Hello World

Multi-line Strings
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   multiline = "
   This is a
   multi-line
   string
   ";
   
   # Preserves indentation
   code_example = "
   fn example() {
       return 'hello';
   }
   ";

Raw Strings
~~~~~~~~~~~

.. code-block:: symbolic

   # Backslashes treated literally
   path = r"C:\Users\Name\Documents";
   regex = r"\d+\s+\w+";

String Interpolation
--------------------

Basic Interpolation
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   name = "Alice";
   age = 30;
   message = $"Hello {name}, you are {age} years old";
   print(message);  # Hello Alice, you are 30 years old

Formatted Interpolation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   price = 19.99;
   quantity = 3;
   
   # Number formatting
   total = $"Total: ${price * quantity:,.2f}";  # Total: $59.97
   percentage = $"Score: {0.8572:.1%}";         # Score: 85.7%
   padded = $"ID: {42:05d}";                    # ID: 00042
   
   # String formatting
   name = "Bob";
   aligned = $"|{name:<10}|{name:^10}|{name:>10}|";
   # |Bob       |   Bob    |       Bob|

Expression Interpolation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   a = 5;
   b = 3;
   result = $"${a} + ${b} = ${a + b}";  # 5 + 3 = 8
   
   # Function calls in interpolation
   names = ["Alice", "Bob", "Charlie"];
   count_message = $"There are {len(names)} names: {names.join(', ')}";
   # There are 3 names: Alice, Bob, Charlie

String Operations
-----------------

Concatenation
~~~~~~~~~~~~~

.. code-block:: symbolic

   first = "Hello";
   second = "World";
   combined = first + " " + second;  # Hello World
   
   # With += operator
   greeting = "Hello";
   greeting += " World!";
   print(greeting);  # Hello World!

Repetition
~~~~~~~~~~

.. code-block:: symbolic

   stars = "*" * 10;        # **********
   pattern = "abc" * 3;     # abcabcabc
   indent = "  " * 4;       # 8 spaces

String Methods
--------------

Case Conversion
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   text = "Hello World";
   upper = text.upper();      # HELLO WORLD
   lower = text.lower();      # hello world
   title = text.title();      # Hello World
   capitalize = text.capitalize();  # Hello world

Searching and Checking
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   text = "Hello World";
   
   # Checking
   starts = text.starts_with("Hello");  # true
   ends = text.ends_with("World");      # true
   contains = text.contains("lo W");    # true
   
   # Searching
   position = text.find("World");       # 6
   last_pos = text.rfind("l");          # 9
   count = text.count("l");             # 3

Modification
~~~~~~~~~~~~

.. code-block:: symbolic

   text = "  Hello World  ";
   
   # Trimming
   trimmed = text.trim();           # "Hello World"
   left_trim = text.trim_left();    # "Hello World  "
   right_trim = text.trim_right();   # "  Hello World"
   
   # Replacement
   replaced = text.replace("World", "Symbolic");  # "  Hello Symbolic  "
   no_spaces = text.replace(" ", "");             # "HelloWorld"
   
   # Splitting
   words = text.trim().split(" ");  # ["Hello", "World"]
   chars = text.split("");          # [" ", " ", "H", "e", ...]

Padding and Alignment
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   text = "Hello";
   
   padded_left = text.pad_left(10);      # "     Hello"
   padded_right = text.pad_right(10);    # "Hello     "
   padded_center = text.pad_center(11);  # "   Hello  "
   
   # With custom characters
   stars = text.pad_left(10, "*");       # "*****Hello"

String Properties
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   text = "Hello 世界";
   
   length = text.length();          # 7 (characters)
   byte_length = text.byte_length(); # 11 (bytes in UTF-8)
   is_empty = text.is_empty();      # false
   is_blank = text.is_blank();      # false (only whitespace)

Practical Examples
------------------

Text Processing
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_text_content(text) {
       # Remove extra whitespace
       cleaned = text.trim().replace("\s+", " ");
       
       # Split into sentences (simple approach)
       sentences = cleaned.split(/[.!?]+/);
       
       # Process each sentence
       results = [];
       for sentence in sentences {
           if sentence.trim().is_empty() {
               skip;
           }
           
           # Capitalize first letter
           processed = sentence.trim().capitalize();
           results.append(processed);
       }
       
       return results.join(". ") + ".";
   }
   
   input_text = "hello world. this is a test.   multiple   spaces. ";
   output = process_text_content(input_text);
   # "Hello world. This is a test. Multiple spaces."

Template System
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn render_template(template, data) {
       result = template;
       
       for key, value in data {
           placeholder = "${" + key + "}";
           result = result.replace(placeholder, value.to_string());
       }
       
       return result;
   }
   
   template = "
   Dear ${name},
   
   Your order ${order_id} has been shipped.
   Total: $${amount}
   
   Thank you!
   ";
   
   data = {
       name: "Alice",
       order_id: "12345",
       amount: "99.99"
   };
   
   email = render_template(template, data);
   print(email);

CSV Parsing
~~~~~~~~~~~

.. code-block:: symbolic

   fn parse_csv(csv_text) {
       lines = csv_text.trim().split("\n");
       headers = lines[0].split(",");
       
       data = [];
       for i in 1..<len(lines) {
           if lines[i].trim().is_empty() {
               skip;
           }
           
           values = lines[i].split(",");
           if len(values) != len(headers) {
               print($"Skipping invalid line: {lines[i]}");
               skip;
           }
           
           record = {};
           for j in 0..<len(headers) {
               record[headers[j].trim()] = values[j].trim();
           }
           data.append(record);
       }
       
       return data;
   }

Password Validation
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn validate_password(password) {
       if password.length() < 8 {
           return "Password must be at least 8 characters";
       }
       
       if !password.contains(/\d/) {
           return "Password must contain at least one number";
       }
       
       if !password.contains(/[A-Z]/) {
           return "Password must contain at least one uppercase letter";
       }
       
       if !password.contains(/[a-z]/) {
           return "Password must contain at least one lowercase letter";
       }
       
       if !password.contains(/[!@#$%^&*]/) {
           return "Password must contain at least one special character";
       }
       
       return "Password is valid";
   }

String Building
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn build_sql_query(table, filters) {
       query = "SELECT * FROM " + table;
       
       if !filters.is_empty() {
           where_clauses = [];
           for field, value in filters {
               # Proper escaping would be needed in real implementation
               clause = field + " = '" + value.replace("'", "''") + "'";
               where_clauses.append(clause);
           }
           query += " WHERE " + where_clauses.join(" AND ");
       }
       
       return query;
   }

Encoding and Decoding
---------------------

Base64
~~~~~~

.. code-block:: symbolic

   data = "Hello World";
   encoded = data.base64_encode();  # SGVsbG8gV29ybGQ=
   decoded = encoded.base64_decode(); # Hello World

URL Encoding
~~~~~~~~~~~~

.. code-block:: symbolic

   query = "name=John Doe&age=30";
   encoded = query.url_encode();  # name%3DJohn%20Doe%26age%3D30
   decoded = encoded.url_decode(); # name=John Doe&age=30

HTML Escaping
~~~~~~~~~~~~~

.. code-block:: symbolic

   html = "<div>Hello & World</div>";
   escaped = html.escape_html();  # &lt;div&gt;Hello &amp; World&lt;/div&gt;
   unescaped = escaped.unescape_html(); # <div>Hello & World</div>

Regular Expressions
-------------------

Pattern Matching
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   text = "The price is $19.99 and $29.50";
   
   # Find all prices
   prices = text.find_all(/\$\d+\.\d{2}/);
   print(prices);  # ["$19.99", "$29.50"]
   
   # Extract just the numbers
   numbers = text.find_all(/\d+\.\d{2}/);
   print(numbers);  # ["19.99", "29.50"]

Replacement
~~~~~~~~~~~

.. code-block:: symbolic

   text = "Call 555-1234 or 555-5678";
   
   # Mask phone numbers
   masked = text.replace(/\d{3}-\d{4}/, "XXX-XXXX");
   print(masked);  # "Call XXX-XXXX or XXX-XXXX"

Validation
~~~~~~~~~~

.. code-block:: symbolic

   fn validate_email(email) {
       pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
       return pattern.test(email);
   }
   
   fn validate_phone(phone) {
       pattern = /^\(\d{3}\) \d{3}-\d{4}$/;
       return pattern.test(phone);
   }

Performance Tips
----------------

String Building
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Efficient - use join for many strings
   words = ["hello", "world", "this", "is", "a", "test"];
   sentence = words.join(" ");  # Most efficient
   
   # Less efficient - concatenation in loop
   result = "";
   for word in words {
       result += word + " ";  # Creates new string each time
   }

Use String Methods
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - use built-in methods
   if text.contains("error") {
       # handle error
   }
   
   # Less efficient - manual search
   if text.find("error") != -1 {
       # handle error
   }