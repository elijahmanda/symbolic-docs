Contracts
=========

Design by Contract (DbC) in Symbolic enables you to specify preconditions, postconditions, and invariants that are checked at runtime to ensure program correctness.

Preconditions
-------------

Basic Preconditions
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn withdraw(amount: Float, balance: Float)
       requires amount > 0,
                amount <= balance,
                balance >= 0
   {
       return balance - amount;
   }
   
   fn divide(numerator: Float, denominator: Float)
       requires denominator != 0
   {
       return numerator / denominator;
   }

Complex Preconditions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_transaction(transaction, account)
       requires transaction.amount > 0,
                account.is_active(),
                account.balance >= transaction.amount,
                transaction.currency == account.currency
   {
       # Process the transaction
       new_balance = account.balance - transaction.amount;
       return new_balance;
   }
   
   fn matrix_multiply(a: Matrix, b: Matrix)
       requires a.columns == b.rows,
                a.rows > 0,
                b.columns > 0
   {
       # Matrix multiplication implementation
   }

Precondition Lists
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn create_user_profile(name: String, age: Integer, email: String)
       requires [
           name.length() >= 2,
           name.length() <= 50,
           age >= 13,
           age <= 150,
           email.contains("@"),
           email.contains(".")
       ]
   {
       return {
           name: name,
           age: age,
           email: email,
           created_at: time.now()
       };
   }

Postconditions
--------------

Basic Postconditions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn square(x: Float) -> Float
       ensures result >= 0
   {
       return x * x;
   }
   
   fn absolute_value(x: Float) -> Float
       ensures result >= 0
   {
       if x < 0 {
           return -x;
       }
       return x;
   }

Result-Based Postconditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn factorial(n: Integer) -> Integer
       ensures result >= 1
   {
       if n <= 1 {
           return 1;
       }
       return n * factorial(n - 1);
   }
   
   fn find_maximum(numbers: [Float]) -> Float
       requires numbers.length() > 0
       ensures result in numbers,
               all(numbers.map(x => x <= result))
   {
       max_val = numbers[0];
       for num in numbers[1..] {
           if num > max_val {
               max_val = num;
           }
       }
       return max_val;
   }

State-Based Postconditions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn transfer_funds(from_account, to_account, amount: Float)
       requires amount > 0,
                from_account.balance >= amount
       ensures from_account.balance == old(from_account.balance) - amount,
               to_account.balance == old(to_account.balance) + amount,
               total_balance == old(total_balance)
   {
       old_from_balance = from_account.balance;
       old_to_balance = to_account.balance;
       
       from_account.balance -= amount;
       to_account.balance += amount;
   }

Invariants
----------

Class Invariants
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class BankAccount {
       balance: Float;
       is_active: Boolean;
       
       invariant balance >= 0;
       invariant is_active implies balance >= 1.0;  # Minimum balance for active accounts
       
       fn withdraw(self, amount: Float)
           requires amount > 0,
                    amount <= self.balance
           ensures self.balance == old(self.balance) - amount
       {
           self.balance -= amount;
       }
       
       fn deposit(self, amount: Float)
           requires amount > 0
           ensures self.balance == old(self.balance) + amount
       {
           self.balance += amount;
       }
   }

Loop Invariants
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn binary_search(arr: [Integer], target: Integer) -> Integer
       requires arr.is_sorted()
       ensures result == -1 or arr[result] == target
   {
       low = 0;
       high = arr.length() - 1;
       
       while low <= high
           invariant 0 <= low <= high + 1,
                    high < arr.length(),
                    all(arr[0..low].map(x => x < target)),
                    all(arr[high+1..].map(x => x > target))
       {
           mid = (low + high) // 2;
           if arr[mid] == target {
               return mid;
           } else if arr[mid] < target {
               low = mid + 1;
           } else {
               high = mid - 1;
           }
       }
       
       return -1;
   }

Practical Examples
------------------

Financial System Contracts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class InvestmentPortfolio {
       holdings: {String: Float};  # symbol -> quantity
       cash_balance: Float;
       
       invariant cash_balance >= 0;
       invariant all(holdings.values().map(qty => qty >= 0));
       invariant portfolio_value >= 0;
       
       fn portfolio_value(self) -> Float
           ensures result >= 0
       {
           total = self.cash_balance;
           for symbol, quantity in self.holdings.entries() {
               price = get_current_price(symbol);
               total += quantity * price;
           }
           return total;
       }
       
       fn buy_stock(self, symbol: String, quantity: Float, price: Float)
           requires quantity > 0,
                    price > 0,
                    self.cash_balance >= quantity * price
           ensures self.cash_balance == old(self.cash_balance) - quantity * price,
                   self.holdings[symbol] == old(self.holdings.get(symbol, 0)) + quantity
       {
           cost = quantity * price;
           self.cash_balance -= cost;
           self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity;
       }
   }

Data Structure Contracts
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class PriorityQueue {
       heap: [Element];
       
       invariant self.is_heap();
       
       fn is_heap(self) -> Boolean {
           for i in 0..<self.heap.length() {
               left = 2*i + 1;
               right = 2*i + 2;
               
               if left < self.heap.length() and self.heap[i] < self.heap[left] {
                   return false;
               }
               if right < self.heap.length() and self.heap[i] < self.heap[right] {
                   return false;
               }
           }
           return true;
       }
       
       fn push(self, item: Element, priority: Float)
           ensures self.heap.length() == old(self.heap.length()) + 1,
                   self.is_heap()
       {
           self.heap.append((priority, item));
           self._bubble_up(self.heap.length() - 1);
       }
   }

API Contract Validation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn validate_api_request(request)
       requires request.has_key("method"),
                request.method in ["GET", "POST", "PUT", "DELETE"],
                request.has_key("path"),
                request.path.starts_with("/api/"),
                request.has_key("headers"),
                "Content-Type" in request.headers
       ensures result.has_key("is_valid"),
               result.has_key("errors")
   {
       errors = [];
       
       # Validate authentication
       if !request.headers.has_key("Authorization") {
           errors.append("Missing Authorization header");
       }
       
       # Validate rate limiting
       if is_rate_limited(request.client_ip) {
           errors.append("Rate limit exceeded");
       }
       
       return {
           is_valid: errors.is_empty(),
           errors: errors
       };
   }

Advanced Contract Patterns
--------------------------

Contract Inheritance
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Shape {
       area: Float;
       
       invariant area >= 0;
       
       virtual fn calculate_area(self) -> Float
           ensures result >= 0
       {
           return self.area;
       }
   }
   
   class Circle extends Shape {
       radius: Float;
       
       invariant radius >= 0;
       
       fn calculate_area(self) -> Float
           ensures result == π * self.radius ^ 2
       {
           return π * self.radius * self.radius;
       }
   }
   
   class Rectangle extends Shape {
       width: Float;
       height: Float;
       
       invariant width >= 0;
       invariant height >= 0;
       
       fn calculate_area(self) -> Float
           ensures result == self.width * self.height
       {
           return self.width * self.height;
       }
   }

Conditional Contracts
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_data(data, strategy: String)
       requires data != null
       ensures if strategy == "aggregate" then result.has_key("summary"),
              if strategy == "analyze" then result.has_key("insights"),
              if strategy == "transform" then result.length() == data.length()
   {
       return match strategy {
           "aggregate" => {
               summary = calculate_summary(data);
               return {summary: summary};
           }
           "analyze" => {
               insights = generate_insights(data);
               return {insights: insights};
           }
           "transform" => {
               return data.map(transform_item);
           }
       };
   }

Contract Composition
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn safe_data_pipeline(raw_data, validators: [Validator], transformers: [Transformer])
       requires raw_data != null,
                all(validators.map(v => v != null)),
                all(transformers.map(t => t != null))
       ensures result.valid_data.length() <= raw_data.length(),
               result.invalid_data.length() <= raw_data.length(),
               result.valid_data.length() + result.invalid_data.length() == raw_data.length()
   {
       valid_data = [];
       invalid_data = [];
       
       for item in raw_data {
           is_valid = all(validators.map(validator => validator.validate(item)));
           
           if is_valid {
               transformed = item;
               for transformer in transformers {
                   transformed = transformer.apply(transformed);
               }
               valid_data.append(transformed);
           } else {
               invalid_data.append(item);
           }
       }
       
       return {
           valid_data: valid_data,
           invalid_data: invalid_data
       };
   }

Testing and Debugging
---------------------

Contract Violation Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Configure contract checking level
   set_contract_level("debug");  # Check all contracts
   set_contract_level("production");  # Check only critical contracts
   set_contract_level("off");    # Disable contract checking
   
   # Custom contract violation handler
   set_contract_violation_handler(fn(contract_type, message, stack_trace) {
       log_error($"Contract violation: {contract_type} - {message}");
       log_error($"Stack trace: {stack_trace}");
       
       if contract_type == "precondition" {
           throw PreconditionViolationError(message);
       } else if contract_type == "postcondition" {
           throw PostconditionViolationError(message);
       } else if contract_type == "invariant" {
           throw InvariantViolationError(message);
       }
   });

Contract Testing
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "withdraw precondition validation" {
       account = BankAccount(balance=100.0);
       
       # Should succeed
       account.withdraw(50.0);
       
       # Should violate precondition
       try {
           account.withdraw(150.0);  # Insufficient funds
           assert false;  # Should not reach here
       } catch e {
           assert e is PreconditionViolationError;
       }
   }
   
   test "factorial postcondition" {
       # Test that result is always >= 1
       for n in 0..10 {
           result = factorial(n);
           assert result >= 1;
       }
   }

Best Practices
--------------

Write Meaningful Contracts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good: Clear, meaningful contracts
   fn process_payment(amount: Float, payment_method: String)
       requires amount > 0,
                payment_method in ["credit_card", "paypal", "bank_transfer"]
       ensures result.has_key("transaction_id"),
               result.has_key("status"),
               result.status in ["success", "failed"]
   {
       # Implementation
   }
   
   # Avoid: Vague contracts
   fn process_payment(amount, method)
       requires amount > 0  # What about method validation?
   {
       # Implementation
   }

Keep Contracts Readable
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good: Readable conditions
   fn create_user_profile(name, age, email)
       requires [
           name.length() between 2 and 50,
           age between 13 and 150,
           email.matches(/^[^@]+@[^@]+\.[^@]+$/)
       ]
   {
       # Implementation
   }
   
   # Avoid: Complex, hard-to-read conditions
   fn create_user_profile(name, age, email)
       requires name.length() >= 2 and name.length() <= 50 and 
                age >= 13 and age <= 150 and 
                email.contains("@") and email.split("@")[1].contains(".")
   {
       # Implementation
   }

Use Contracts for Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Contracts serve as living documentation
   fn calculate_compound_interest(
       principal: Float, 
       annual_rate: Float, 
       years: Integer, 
       compounds_per_year: Integer
   ) -> Float
       requires principal >= 0,
                annual_rate >= 0,
                years >= 0,
                compounds_per_year >= 1
       ensures result >= principal  # Money should not decrease with positive rate
   {
       rate_per_period = annual_rate / compounds_per_year;
       periods = years * compounds_per_year;
       return principal * (1 + rate_per_period) ^ periods;
   }