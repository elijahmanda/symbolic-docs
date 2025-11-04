Conditional Statements
======================

Conditional statements allow your program to make decisions and execute different code paths based on conditions.

If Statements
-------------

Basic If Statement
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   temperature = 25;
   if temperature > 30 {
       print("It's hot outside!");
   }

If-Else Statement
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   score = 85;
   if score >= 90 {
       grade = "A";
   } else {
       grade = "B or below";
   }
   print(grade);

If-Else If-Else Chain
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   temperature = 22;
   if temperature > 30 {
       print("Hot weather");
   } else if temperature > 20 {
       print("Pleasant weather");
   } else if temperature > 10 {
       print("Cool weather");
   } else {
       print("Cold weather");
   }

Ternary Operator
----------------

.. code-block:: symbolic

   age = 20;
   status = age >= 18 ? "adult" : "minor";
   print(status);  # "adult"

   # Equivalent to:
   if age >= 18 {
       status = "adult";
   } else {
       status = "minor";
   }

Practical Examples
------------------

User Authentication
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn authenticate_user(username, password) {
       if username == "" or password == "" {
           return "Username and password required";
       } else if len(password) < 8 {
           return "Password must be at least 8 characters";
       } else if !user_exists(username) {
           return "User not found";
       } else if !verify_password(username, password) {
           return "Invalid password";
       } else {
           return "Login successful";
       }
   }

Grade Calculator
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_grade(score) {
       if score >= 90 {
           return "A";
       } else if score >= 80 {
           return "B";
       } else if score >= 70 {
           return "C";
       } else if score >= 60 {
           return "D";
       } else {
           return "F";
       }
   }

   grades = [85, 92, 78, 45, 67];
   for score in grades {
       grade = calculate_grade(score);
       print($"Score: {score} -> Grade: {grade}");
   }

Price Calculation with Discounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn calculate_price(quantity, is_member, coupon_code) {
       base_price = quantity * 10;
       
       if quantity > 100 {
           discount = 0.20;  # 20% bulk discount
       } else if quantity > 50 {
           discount = 0.15;  # 15% discount
       } else if quantity > 10 {
           discount = 0.10;  # 10% discount
       } else {
           discount = 0;
       }
       
       if is_member {
           discount += 0.05;  # Additional 5% for members
       }
       
       if coupon_code == "SAVE10" {
           discount += 0.10;
       } else if coupon_code == "SAVE5" {
           discount += 0.05;
       }
       
       final_price = base_price * (1 - min(discount, 0.50));  # Max 50% discount
       return final_price;
   }

   # Example usage
   price1 = calculate_price(75, true, "SAVE10");
   price2 = calculate_price(5, false, "");
   print($"Price 1: ${price1:.2f}");  # $510.00
   print($"Price 2: ${price2:.2f}");  # $50.00

Temperature Alert System
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn check_temperature_alert(current_temp, target_temp, tolerance) {
       difference = abs(current_temp - target_temp);
       
       if difference > tolerance * 2 {
           return "CRITICAL: Temperature deviation too high!";
       } else if difference > tolerance {
           return "WARNING: Temperature outside target range";
       } else if current_temp > target_temp + tolerance / 2 {
           return "Notice: Slightly above target";
       } else if current_temp < target_temp - tolerance / 2 {
           return "Notice: Slightly below target";
       } else {
           return "Normal: Within optimal range";
       }
   }

   # Monitoring system temperatures
   temperatures = [72.5, 75.8, 69.2, 80.1, 71.9];
   target = 72.0;
   tolerance = 3.0;
   
   for temp in temperatures {
       alert = check_temperature_alert(temp, target, tolerance);
       print($"Temp: {temp}°F -> {alert}");
   }

Best Practices
--------------

1. **Use descriptive conditions**: Make conditions easy to read and understand

   .. code-block:: symbolic

      # Good
      if user.is_authenticated and user.has_permission("admin") {
          # admin actions
      }
      
      # Avoid
      if u.auth and u.perm == "admin" {
          # hard to understand
      }

2. **Avoid deep nesting**: Use early returns to flatten conditionals

   .. code-block:: symbolic

      # Good
      fn process_order(order) {
          if order == null {
              return "Invalid order";
          }
          if order.items.is_empty() {
              return "Order has no items";
          }
          if !order.is_paid() {
              return "Order not paid";
          }
          # Process valid order
          return "Order processed";
      }

3. **Use ternary for simple assignments**

   .. code-block:: symbolic

      # Good
      discount = is_premium_member ? 0.15 : 0.05;
      
      # Less clear
      if is_premium_member {
          discount = 0.15;
      } else {
          discount = 0.05;
      }