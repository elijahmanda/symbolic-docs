Pattern Matching
================

Pattern matching allows you to check values against patterns and extract data in a concise, readable way.

Basic Pattern Matching
----------------------

Value Matching
~~~~~~~~~~~~~~

.. code-block:: symbolic

   result = match value {
       0 => "zero";
       1 => "one";
       2 => "two";
       _ => "other number";
   };

Type Matching
~~~~~~~~~~~~~

.. code-block:: symbolic

   fn describe_value(x) {
       return match x {
           Integer => "integer number";
           Float => "floating point number";
           String => "text string";
           Boolean => "true or false";
           _ => "other type";
       };
   }

List Patterns
-------------

Empty List
~~~~~~~~~~

.. code-block:: symbolic

   match list {
       [] => "empty list";
       [x] => $"single element: {x}";
       [x, y] => $"two elements: {x} and {y}";
       [first, *rest] => $"first: {first}, rest: {rest}";
   }

Head-Tail Pattern
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn sum_list(numbers) {
       return match numbers {
           [] => 0;
           [head, *tail] => head + sum_list(tail);
       };
   }

   numbers = [1, 2, 3, 4, 5];
   total = sum_list(numbers);  # 15

Tuple Patterns
--------------

.. code-block:: symbolic

   point = (3, 4);
   match point {
       (0, 0) => "origin";
       (x, 0) => $"on x-axis at {x}";
       (0, y) => $"on y-axis at {y}";
       (x, y) => $"at coordinates ({x}, {y})";
   }

Object Patterns
---------------

Field Matching
~~~~~~~~~~~~~~

.. code-block:: symbolic

   user = {name: "Alice", age: 30, role: "admin"};
   
   match user {
       {role: "admin"} => "administrator user";
       {role: "user", age: age} if age < 18 => "minor user";
       {role: "user", age: age} if age >= 18 => "adult user";
       _ => "unknown user type";
   }

Nested Object Matching
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   data = {
       user: {
           profile: {name: "Bob", age: 25},
           settings: {theme: "dark"}
       }
   };
   
   match data {
       {user: {profile: {name: name, age: age}}} => 
           $"User {name} is {age} years old";
       _ => "Invalid user data";
   }

Guards with Patterns
--------------------

Conditional Patterns
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn categorize_number(n) {
       return match n {
           x if x < 0 => "negative";
           0 => "zero";
           x if x > 0 and x < 10 => "small positive";
           x if x >= 10 and x < 100 => "medium positive";
           x if x >= 100 => "large positive";
       };
   }

Complex Guards
~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_user(user) {
       return match user {
           {age: age, status: "active"} if age >= 18 and age <= 65 => 
               "active working-age user";
           {age: age, status: "active"} if age < 18 => 
               "active minor user";
           {age: age, status: "active"} if age > 65 => 
               "active senior user";
           {status: "inactive"} => "inactive user";
           _ => "unknown user status";
       };
   }

Practical Examples
------------------

JSON Data Processing
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_api_response(response) {
       return match response {
           {status: 200, data: data} => {
               print("Success!");
               return data;
           }
           {status: 404, error: error} => {
               print($"Not found: {error}");
               return null;
           }
           {status: 500, error: error} => {
               print($"Server error: {error}");
               return null;
           }
           {status: status} if status >= 400 => {
               print($"Client error: {status}");
               return null;
           }
           _ => {
               print("Unknown response format");
               return null;
           }
       };
   }

Mathematical Expressions
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn evaluate_expression(expr) {
       return match expr {
           {type: "number", value: n} => n;
           {type: "add", left: l, right: r} => 
               evaluate_expression(l) + evaluate_expression(r);
           {type: "multiply", left: l, right: r} => 
               evaluate_expression(l) * evaluate_expression(r);
           {type: "power", base: b, exponent: e} => 
               evaluate_expression(b) ^ evaluate_expression(e);
           _ => throw "Unknown expression type";
       };
   }
   
   # Example: 2 + 3 * 4
   expr = {
       type: "add",
       left: {type: "number", value: 2},
       right: {
           type: "multiply",
           left: {type: "number", value: 3},
           right: {type: "number", value: 4}
       }
   };
   result = evaluate_expression(expr);  # 14

File Type Handling
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn handle_file(file) {
       return match file {
           {type: "text", content: text, encoding: "utf8"} => 
               process_text(text);
           {type: "image", format: "png", data: data} => 
               process_png_image(data);
           {type: "image", format: "jpg", data: data} => 
               process_jpg_image(data);
           {type: "audio", format: format} if format in ["mp3", "wav"] => 
               process_audio(file);
           {type: "video", duration: dur} if dur > 3600 => 
               "long video - processing in background";
           {type: "video", duration: dur} if dur <= 3600 => 
               process_video(file);
           _ => "unsupported file type";
       };
   }

Game State Management
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn handle_game_input(current_state, input) {
       return match (current_state, input) {
           ("menu", "start") => "transition to gameplay";
           ("menu", "quit") => "exit game";
           ("gameplay", "pause") => "pause game";
           ("gameplay", "attack") => "perform attack";
           ("gameplay", "inventory") => "open inventory";
           ("paused", "resume") => "resume gameplay";
           ("paused", "menu") => "return to menu";
           (state, "help") => $"show help for {state}";
           (state, input) => $"unknown input {input} for state {state}";
       };
   }

Advanced Patterns
-----------------

Multiple Patterns
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn is_weekend(day) {
       return match day {
           "saturday" | "sunday" => true;
           "monday" | "tuesday" | "wednesday" | "thursday" | "friday" => false;
           _ => throw "invalid day";
       };
   }

Pattern with As-binding
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   match complex_data_structure as data {
       {type: "user", id: id, profile: {name: name}} => 
           $"User {name} (ID: {id})";
       {type: "product", sku: sku, price: price} => 
           $"Product {sku} - ${price}";
       other => $"Unknown data: {other}";
   }

Nested Patterns
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_nested_data(data) {
       return match data {
           {results: [{status: "success", data: value}, *rest]} => 
               $"First success: {value}";
           {results: [{status: "error", message: msg}, *rest]} => 
               $"First error: {msg}";
           {results: []} => "No results";
           _ => "Unexpected data format";
       };
   }

Error Handling Patterns
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn safe_divide(a, b) {
       return match (a, b) {
           (_, 0) => {error: "division by zero"};
           (x, y) if !is_number(x) or !is_number(y) => 
               {error: "invalid operands"};
           (x, y) => {result: x / y};
       };
   }

Performance Patterns
--------------------

Early Returns
~~~~~~~~~~~~~

.. code-block:: symbolic

   # Use pattern matching for early validation
   fn process_order(order) {
       return match order {
           null => {error: "order is null"};
           {items: []} => {error: "order has no items"};
           {customer: null} => {error: "no customer specified"};
           {items: items, customer: customer} => {
               # Process valid order
               total = items.map(item => item.price * item.quantity).sum();
               {success: true, total: total};
           }
       };
   }

State Machine
~~~~~~~~~~~~~

.. code-block:: symbolic

   fn traffic_light_transition(current, event) {
       return match (current, event) {
           ("red", "timer_expired") => "green";
           ("green", "timer_expired") => "yellow";
           ("yellow", "timer_expired") => "red";
           ("red", "emergency") => "blinking_red";
           ("blinking_red", "emergency_cleared") => "red";
           (state, event) => {
               print($"Invalid transition: {state} -> {event}");
               state;  # Stay in current state
           }
       };
   }

Best Practices
--------------

Exhaustive Matching
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - covers all cases
   fn handle_http_status(code) {
       return match code {
           200 => "OK";
           404 => "Not Found";
           500 => "Server Error";
           other => $"Unknown status: {other}";
       };
   }

Use Guards for Complex Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - guards for ranges
   match temperature {
       t if t < 0 => "freezing";
       t if t >= 0 and t < 10 => "cold";
       t if t >= 10 and t < 20 => "cool";
       t if t >= 20 and t < 30 => "warm";
       t if t >= 30 => "hot";
   }

Avoid Overly Complex Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Consider refactoring very complex patterns
   fn complex_matcher(data) {
       # If pattern gets too complex, break it down
       if !is_valid(data) {
           return "invalid";
       }
       
       return match data {
           # Simpler patterns here
           pattern1 => result1;
           pattern2 => result2;
       };
   }