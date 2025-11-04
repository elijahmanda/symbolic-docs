Error Handling
==============

Symbolic provides robust error handling mechanisms including exceptions, pattern matching, and functional error types.

Try-Catch with Pattern Matching
-------------------------------

Basic Exception Handling
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   try {
       result = risky_operation();
       print($"Success: {result}");
   } catch e {
       print($"Error occurred: {e.message}");
   }

Pattern Matching Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   try {
       data = parse_json(input);
       process(data);
   } catch e {
       ValueError {
           print("Invalid data format");
       }
       TypeError {
           print("Wrong data type");
       }
       DivisionByZeroError {
           print("Cannot divide by zero");
       }
       Exception {
           print($"Unexpected error: {e.message}");
       }
   }

Multiple Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   try {
       user = get_user_from_db(user_id);
       profile = fetch_user_profile(user);
       preferences = load_user_preferences(user);
       
       return {user: user, profile: profile, preferences: preferences};
   } catch e {
       DatabaseError {
           print("Database connection failed");
           return null;
       }
       NetworkError {
           print("Network request failed");
           return {user: user, profile: null, preferences: null};
       }
       FileNotFoundError {
           print("Preferences file not found");
           return {user: user, profile: profile, preferences: default_prefs};
       }
   }

Functional Error Handling
-------------------------

Result Type Pattern
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn safe_divide(a, b) {
       if b == 0 {
           return {error: "Division by zero"};
       }
       return {result: a / b};
   }
   
   fn calculate_average(numbers) {
       if numbers.is_empty() {
           return {error: "Empty list"};
       }
       
       total = numbers.sum();
       count = numbers.length();
       
       division_result = safe_divide(total, count);
       return match division_result {
           {error: msg} => {error: $"Average calculation failed: {msg}"};
           {result: value} => {result: value};
       };
   }

Option Type for Nullable Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn find_user_by_email(email) {
       users = get_all_users();
       for user in users {
           if user.email == email {
               return {some: user};
           }
       }
       return {none: true};
   }
   
   fn get_user_display_name(email) {
       user_result = find_user_by_email(email);
       return match user_result {
           {some: user} => user.name;
           {none: true} => "Unknown User";
       };
   }

Practical Examples
------------------

File Operations
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn read_config_file(filename) {
       try {
           content = read_file(filename);
           config = parse_json(content);
           
           # Validate required fields
           if !config.has_key("api_key") or !config.has_key("api_secret") {
               throw ValueError("Missing required configuration fields");
           }
           
           return config;
       } catch e {
           FileNotFoundError {
               print($"Config file {filename} not found, using defaults");
               return default_config();
           }
           JSONParseError {
               print($"Invalid JSON in config file: {e.message}");
               return default_config();
           }
           ValueError {
               print($"Invalid config: {e.message}");
               return default_config();
           }
       }
   }

API Client with Retry
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn api_call_with_retry(url, max_retries = 3) {
       attempts = 0;
       
       while attempts <= max_retries {
           try {
               response = http_get(url);
               if response.status == 200 {
                   return {success: true, data: response.data};
               } else if response.status == 429 {  # Rate limited
                   print("Rate limited, waiting...");
                   wait(1000 * (2 ^ attempts));  # Exponential backoff
                   attempts += 1;
                   skip;  # continue to retry
               } else {
                   return {success: false, error: $"HTTP {response.status}"};
               }
           } catch e {
               NetworkError {
                   print($"Network error (attempt {attempts + 1}): {e.message}");
                   attempts += 1;
                   if attempts > max_retries {
                       return {success: false, error: "Max retries exceeded"};
                   }
                   wait(1000);  # Wait before retry
               }
           }
       }
   }

Database Transactions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn transfer_funds(from_account, to_account, amount) {
       try {
           # Start transaction
           db.begin_transaction();
           
           # Check sufficient funds
           balance = get_balance(from_account);
           if balance < amount {
               throw InsufficientFundsError("Not enough money");
           }
           
           # Perform transfer
           deduct_funds(from_account, amount);
           add_funds(to_account, amount);
           
           # Log transaction
           log_transaction(from_account, to_account, amount);
           
           # Commit if all successful
           db.commit();
           return {success: true, new_balance: balance - amount};
           
       } catch e {
           # Rollback on any error
           db.rollback();
           
           match e {
               InsufficientFundsError => 
                   return {success: false, error: "Insufficient funds"};
               DatabaseError => 
                   return {success: false, error: "Database error"};
               _ => 
                   return {success: false, error: $"Transfer failed: {e.message}"};
           }
       }
   }

Input Validation
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn validate_user_registration(data) {
       errors = [];
       
       # Validate email
       try {
           if !is_valid_email(data.email) {
               errors.append("Invalid email format");
           }
       } catch e {
           errors.append("Email validation error");
       }
       
       # Validate password
       try {
           password_errors = validate_password(data.password);
           if !password_errors.is_empty() {
               errors.extend(password_errors);
           }
       } catch e {
           errors.append("Password validation error");
       }
       
       # Validate age
       try {
           age = data.age.to_int();
           if age < 13 {
               errors.append("Must be at least 13 years old");
           } else if age > 150 {
               errors.append("Invalid age");
           }
       } catch e {
           errors.append("Age must be a valid number");
       }
       
       if errors.is_empty() {
           return {valid: true, user: create_user(data)};
       } else {
           return {valid: false, errors: errors};
       }
   }

Web Request Handling
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn handle_http_request(request) {
       try {
           # Validate request
           if !is_valid_request(request) {
               return response(400, "Bad Request");
           }
           
           # Authenticate user
           user = await authenticate_user(request);
           if user == null {
               return response(401, "Unauthorized");
           }
           
           # Authorize action
           if !user.has_permission(request.action) {
               return response(403, "Forbidden");
           }
           
           # Process request
           result = await process_request(request, user);
           return response(200, result);
           
       } catch e {
           match e {
               RateLimitError => 
                   return response(429, "Too Many Requests");
               DatabaseError => 
                   return response(503, "Service Unavailable");
               NetworkError => 
                   return response(502, "Bad Gateway");
               _ => 
                   return response(500, "Internal Server Error");
           }
       }
   }

Custom Exceptions
-----------------

Defining Custom Errors
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   BusinessError = Exception.define("BusinessError");
   ValidationError = Exception.define("ValidationError", extends: BusinessError);
   PaymentError = Exception.define("PaymentError", extends: BusinessError);

Using Custom Errors
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_order(order) {
       if order.total <= 0 {
           throw ValidationError("Order total must be positive");
       }
       
       if !order.has_valid_payment_method() {
           throw PaymentError("Invalid payment method");
       }
       
       try {
           charge_result = charge_credit_card(order.payment, order.total);
           if !charge_result.success {
               throw PaymentError($"Payment failed: {charge_result.message}");
           }
           
           return {success: true, order_id: generate_order_id()};
           
       } catch e {
           match e {
               PaymentError => {
                   log_payment_failure(order, e.message);
                   throw e;  # Re-throw for caller to handle
               }
               _ => {
                   log_unexpected_error(e);
                   throw BusinessError("Order processing failed");
               }
           }
       }
   }

Error Recovery Strategies
-------------------------

Fallback Values
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn get_user_preferences(user_id) {
       try {
           return load_preferences_from_db(user_id);
       } catch e {
           DatabaseError => {
               # Fallback to cached version
               cached = get_cached_preferences(user_id);
               if cached != null {
                   return cached;
               }
               # Fallback to defaults
               return get_default_preferences();
           }
           _ => {
               return get_default_preferences();
           }
       }
   }

Retry with Exponential Backoff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn resilient_api_call(operation, max_attempts = 5) {
       attempts = 0;
       
       while attempts < max_attempts {
           try {
               return await operation();
           } catch e {
               attempts += 1;
               if attempts >= max_attempts {
                   throw e;  # Final attempt failed
               }
               
               # Exponential backoff with jitter
               delay = (2 ^ attempts) * 1000 + random(0, 1000);
               print($"Attempt {attempts} failed, retrying in {delay}ms");
               await wait(delay);
           }
       }
   }

Circuit Breaker Pattern
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   circuit_breaker_state = "closed";
   failure_count = 0;
   
   fn protected_api_call() {
       if circuit_breaker_state == "open" {
           throw CircuitBreakerError("Service unavailable");
       }
       
       try {
           result = api_call();
           failure_count = 0;  # Reset on success
           return result;
       } catch e {
           failure_count += 1;
           
           if failure_count >= 5 {
               circuit_breaker_state = "open";
               # Schedule reset after 30 seconds
               schedule(() => { circuit_breaker_state = "half-open"; }, 30000);
           }
           
           throw e;
       }
   }

Best Practices
--------------

Specific Error Handling
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - handle specific errors
   try {
       process_data();
   } catch e {
       FileNotFoundError => handle_missing_file();
       PermissionError => request_permissions();
       _ => log_unexpected_error(e);
   }

Don't Ignore Errors
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Bad - silent failure
   try {
       important_operation();
   } catch e {
       # Ignored!
   }
   
   # Good - at least log it
   try {
       important_operation();
   } catch e {
       log_error(e);
   }

Use Functional Error Types When Appropriate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good for operations that can reasonably fail
   fn parse_number(s) {
       try {
           return {success: true, value: s.to_float()};
       } catch e {
           return {success: false, error: "Invalid number format"};
       }
   }