Function Basics
===============

Functions are fundamental building blocks in Symbolic, allowing code reuse, organization, and abstraction.

Function Definition
-------------------

Basic Function
~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Simple function
   fn greet(name) {
       return "Hello, " + name + "!";
   }
   
   # Function with multiple parameters
   fn calculate_area(length, width) {
       return length * width;
   }
   
   # Function without return (returns null)
   fn log_message(message) {
       print("LOG: " + message);
   }

Mathematical Notation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Mathematical style function
   quadratic(a, b, c, x) = a*x^2 + b*x + c;
   
   # With type annotations
   distance(x1: Float, y1: Float, x2: Float, y2: Float) -> Float {
       dx = x2 - x1;
       dy = y2 - y1;
       return (dx^2 + dy^2).sqrt();
   }

Lambda Functions
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Anonymous functions
   square = (x) => x * x;
   add = (a, b) => a + b;
   is_even = (x) => x % 2 == 0;
   
   # Immediately invoked
   result = ((x, y) => x + y)(5, 3);  # 8

Function Parameters
-------------------

Default Parameters
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn greet(name, greeting = "Hello", punctuation = "!") {
       return greeting + ", " + name + punctuation;
   }
   
   print(greet("Alice"));                # "Hello, Alice!"
   print(greet("Bob", "Hi"));            # "Hi, Bob!"
   print(greet("Charlie", "Hey", "!!")); # "Hey, Charlie!!"

Named Parameters
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn create_user(name, age, email = null, is_active = true) {
       return {
           name: name,
           age: age,
           email: email,
           is_active: is_active
       };
   }
   
   # Using named parameters
   user1 = create_user("Alice", 30);
   user2 = create_user("Bob", 25, email="bob@example.com");
   user3 = create_user(
       name="Charlie",
       age=35,
       is_active=false
   );

Variable Arguments
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn sum_numbers(*numbers) {
       total = 0;
       for num in numbers {
           total += num;
       }
       return total;
   }
   
   print(sum_numbers(1, 2, 3));        # 6
   print(sum_numbers(10, 20, 30, 40)); # 100
   
   fn create_profile(name, *skills) {
       return {
           name: name,
           skills: skills.list()
       };
   }

Keyword Arguments
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn configure_server(**settings) {
       defaults = {
           host: "localhost",
           port: 8080,
           debug: false,
           timeout: 30
       };
       
       # Merge with defaults
       config = defaults.merge(settings);
       return config;
   }
   
   server1 = configure_server();
   server2 = configure_server(port=9000, debug=true);
   server3 = configure_server(
       host="api.example.com",
       timeout=60,
       ssl=true
   );

Return Values
-------------

Multiple Return Values
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_numbers(numbers) {
       if numbers.is_empty() {
           return (0, 0, 0);
       }
       
       count = numbers.length();
       total = numbers.sum();
       average = total / count;
       
       return (count, total, average);
   }
   
   # Unpacking return values
   count, total, avg = analyze_numbers([10, 20, 30, 40]);
   print($"Count: {count}, Total: {total}, Average: {avg}");

Early Returns
~~~~~~~~~~~~~

.. code-block:: symbolic

   fn find_first_even(numbers) {
       for num in numbers {
           if num % 2 == 0 {
               return num;  # Early return
           }
       }
       return null;  # No even numbers found
   }
   
   fn validate_user(user) {
       # Early validation returns
       if user.name == "" {
           return (false, "Name cannot be empty");
       }
       if user.age < 0 {
           return (false, "Age cannot be negative");
       }
       if user.email == "" {
           return (false, "Email is required");
       }
       
       return (true, "User is valid");
   }

Function Scope
--------------

Local Variables
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_statistics(data) {
       # Local variables
       count = data.length();
       total = data.sum();
       average = total / count;
       
       # Nested function with access to outer scope
       fn variance() {
           sum_squares = data.map(x => (x - average)^2).sum();
           return sum_squares / count;
       }
       
       return {
           count: count,
           average: average,
           variance: variance()
       };
   }

Closures
~~~~~~~~

.. code-block:: symbolic

   fn create_multiplier(factor) {
       # Returns a function that "remembers" factor
       return (x) => x * factor;
   }
   
   double = create_multiplier(2);
   triple = create_multiplier(3);
   
   print(double(5));  # 10
   print(triple(5));  # 15
   
   fn create_counter() {
       count = 0;
       return () => {
           count += 1;
           return count;
       };
   }
   
   counter = create_counter();
   print(counter());  # 1
   print(counter());  # 2
   print(counter());  # 3

Practical Examples
------------------

Validation Functions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn validate_email(email) {
       if email == "" {
           return (false, "Email cannot be empty");
       }
       
       if !email.contains("@") {
           return (false, "Email must contain @ symbol");
       }
       
       local_part, domain = email.split("@");
       
       if local_part == "" or domain == "" {
           return (false, "Invalid email format");
       }
       
       if !domain.contains(".") {
           return (false, "Domain must contain a dot");
       }
       
       return (true, "Email is valid");
   }
   
   fn validate_password(password) {
       errors = [];
       
       if password.length() < 8 {
           errors.append("Password must be at least 8 characters");
       }
       
       if !password.matches(/[A-Z]/) {
           errors.append("Password must contain uppercase letter");
       }
       
       if !password.matches(/[a-z]/) {
           errors.append("Password must contain lowercase letter");
       }
       
       if !password.matches(/\d/) {
           errors.append("Password must contain a number");
       }
       
       if errors.is_empty() {
           return (true, "Password is strong");
       } else {
           return (false, errors.join(", "));
       }
   }

Mathematical Functions
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn quadratic_roots(a, b, c) {
       discriminant = b^2 - 4*a*c;
       
       if discriminant < 0 {
           return (null, null, "No real roots");
       }
       
       root1 = (-b + discriminant.sqrt()) / (2*a);
       root2 = (-b - discriminant.sqrt()) / (2*a);
       
       return (root1, root2, "Two real roots");
   }
   
   fn factorial(n) {
       if n < 0 {
           throw "Factorial not defined for negative numbers";
       }
       if n <= 1 {
           return 1;
       }
       return n * factorial(n - 1);
   }
   
   fn fibonacci(n) {
       if n <= 0 {
           return 0;
       }
       if n == 1 {
           return 1;
       }
       
       a, b = 0, 1;
       for i in 2..n {
           a, b = b, a + b;
       }
       return b;
   }

Data Transformation
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn transform_data_for_chart(data, options = {}) {
       defaults = {
           sort: true,
           limit: null,
           format: "percentage"
       };
       config = defaults.merge(options);
       
       # Filter and sort
       processed = data
           .filter(item => item.value != null)
           .map(item => {
               return {
                   label: item.label,
                   value: item.value,
                   formatted: format_value(item.value, config.format)
               };
           });
       
       if config.sort {
           processed = processed.sorted((a, b) => b.value - a.value);
       }
       
       if config.limit != null {
           processed = processed.take(config.limit);
       }
       
       return processed;
   }
   
   fn format_value(value, format) {
       return match format {
           "percentage" => $"{(value * 100):.1f}%";
           "currency" => $"${value:,.2f}";
           "scientific" => $"${value:.2e}";
           _ => value.to_string();
       };
   }

String Processing
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn format_phone_number(number, format = "us") {
       # Remove non-digit characters
       digits = number.replace(/[^\d]/, "");
       
       return match format {
           "us" => 
               $"({digits[0..3]}) {digits[3..6]}-{digits[6..10]}";
           "eu" =>
               $"+{digits[0..2]} {digits[2..5]} {digits[5..8]} {digits[8..12]}";
           "compact" =>
               digits;
           _ =>
               number;
       };
   }
   
   fn slugify(text) {
       return text
           .lower()
           .replace(/[^\w\s-]/, "")  # Remove special chars
           .replace(/[\s_-]+/, "-")  # Replace spaces/underscores with hyphens
           .replace(/^-+|-+$/, "")   # Remove leading/trailing hyphens
           .trim();
   }

Best Practices
--------------

Single Responsibility
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - each function does one thing
   fn calculate_tax(amount, rate) {
       return amount * rate;
   }
   
   fn format_currency(amount) {
       return $"${amount:,.2f}";
   }
   
   fn process_order(order) {
       tax = calculate_tax(order.subtotal, order.tax_rate);
       total = order.subtotal + tax;
       return {
           subtotal: format_currency(order.subtotal),
           tax: format_currency(tax),
           total: format_currency(total)
       };
   }

Descriptive Names
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - clear, descriptive names
   fn calculate_monthly_compound_interest(principal, annual_rate, years) {
       monthly_rate = annual_rate / 12;
       periods = years * 12;
       return principal * (1 + monthly_rate) ^ periods;
   }
   
   fn is_valid_credit_card_number(number) {
       # Implementation of Luhn algorithm
       return luhn_check(number);
   }

Keep Functions Small
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - small, focused functions
   fn validate_user_input(input) {
       errors = [];
       
       errors.extend(validate_name(input.name));
       errors.extend(validate_email(input.email));
       errors.extend(validate_age(input.age));
       
       return errors;
   }
   
   fn validate_name(name) {
       if name == "" {
           return ["Name is required"];
       }
       if name.length() < 2 {
           return ["Name must be at least 2 characters"];
       }
       return [];
   }