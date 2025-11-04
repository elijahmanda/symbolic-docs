Testing
=======

Symbolic provides a comprehensive testing framework with unit tests, property-based testing, integration tests, and advanced testing patterns.

Unit Testing
------------

Basic Test Cases
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Simple function to test
   fn add(a: Integer, b: Integer) -> Integer {
       return a + b;
   }
   
   # Test cases
   test "addition of positive numbers" {
       result = add(2, 3);
       assert result == 5;
   }
   
   test "addition with zero" {
       assert add(0, 5) == 5;
       assert add(5, 0) == 5;
       assert add(0, 0) == 0;
   }
   
   test "addition of negative numbers" {
       assert add(-2, -3) == -5;
       assert add(-2, 3) == 1;
       assert add(2, -3) == -1;
   }

Test Organization
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Test suite for math operations
   test suite "Math Operations" {
       test "addition" {
           assert add(2, 3) == 5;
       }
       
       test "subtraction" {
           assert subtract(5, 3) == 2;
       }
       
       test "multiplication" {
           assert multiply(4, 5) == 20;
       }
       
       test "division" {
           assert divide(10, 2) == 5;
       }
   }
   
   # Nested test suites
   test suite "String Operations" {
       test suite "Validation" {
           test "empty string" {
               assert is_valid_string("") == false;
           }
           
           test "valid string" {
               assert is_valid_string("hello") == true;
           }
       }
       
       test suite "Transformation" {
           test "uppercase" {
               assert "hello".upper() == "HELLO";
           }
           
           test "lowercase" {
               assert "HELLO".lower() == "hello";
           }
       }
   }

Assertions
----------

Basic Assertions
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "basic assertions" {
       value = 42;
       
       # Equality
       assert value == 42;
       assert value != 0;
       
       # Comparison
       assert value > 40;
       assert value >= 42;
       assert value < 50;
       assert value <= 42;
       
       # Type checking
       assert value is Integer;
       assert value is not String;
       
       # Boolean conditions
       assert true;
       assert !false;
       assert (value > 0) and (value < 100);
   }

Collection Assertions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "collection assertions" {
       numbers = [1, 2, 3, 4, 5];
       empty_list = [];
       
       # List assertions
       assert numbers.length() == 5;
       assert numbers.contains(3);
       assert !numbers.contains(10);
       assert numbers[0] == 1;
       assert numbers[-1] == 5;
       
       # Empty checks
       assert empty_list.is_empty();
       assert !numbers.is_empty();
       
       # Set assertions
       unique_numbers = set(numbers);
       assert unique_numbers.length() == 5;
       assert unique_numbers == {1, 2, 3, 4, 5};
   }

String Assertions
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "string assertions" {
       text = "Hello, World!";
       empty_string = "";
       
       # Content assertions
       assert text == "Hello, World!";
       assert text != "Goodbye";
       assert text.contains("World");
       assert !text.contains("Mars");
       
       # Pattern matching
       assert text.matches(/^Hello/);
       assert text.matches(/World!$/);
       
       # Case and formatting
       assert text.upper() == "HELLO, WORLD!";
       assert text.lower() == "hello, world!";
       
       # Empty checks
       assert empty_string.is_empty();
       assert !text.is_empty();
   }

Exception Assertions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "exception assertions" {
       # Test that function throws expected exception
       assert_throws DivideByZeroError {
           divide(10, 0);
       }
       
       # Test with specific error message
       assert_throws ValueError, "Invalid input" {
           process_input(null);
       }
       
       # Test no exception is thrown
       assert_no_throw {
           safe_operation();
       }
   }

Property-Based Testing
----------------------

Generative Testing
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test property "addition is commutative" {
       forall (a: Integer, b: Integer) {
           assert add(a, b) == add(b, a);
       }
   }
   
   test property "multiplication distributes over addition" {
       forall (a: Integer, b: Integer, c: Integer) {
           left = multiply(a, add(b, c));
           right = add(multiply(a, b), multiply(a, c));
           assert left == right;
       }
   }

Custom Generators
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Define custom data generators
   generator positive_integers() {
       return random(1, 1000);
   }
   
   generator valid_emails() {
       domains = ["example.com", "test.org", "demo.net"];
       local_parts = ["user", "admin", "test", "demo"];
       domain = domains.random_choice();
       local_part = local_parts.random_choice();
       return $"{local_part}@{domain}";
   }
   
   generator lists_of_integers() {
       length = random(0, 10);
       return [random(-100, 100) for _ in 0..<length];
   }
   
   test property "sorting preserves length" {
       forall numbers: lists_of_integers() {
           sorted = numbers.sorted();
           assert sorted.length() == numbers.length();
       }
   }

Advanced Property Testing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test property "sorting produces ordered list" {
       forall numbers: lists_of_integers() {
           sorted = numbers.sorted();
           
           # Check ordering
           for i in 0..<(sorted.length() - 1) {
               assert sorted[i] <= sorted[i + 1];
           }
           
           # Check element preservation
           assert set(sorted) == set(numbers);
       }
   }
   
   test property "reverse is involutive" {
       forall items: lists_of_integers() {
           reversed_once = items.reverse();
           reversed_twice = reversed_once.reverse();
           assert reversed_twice == items;
       }
   }

Integration Testing
-------------------

API Testing
~~~~~~~~~~~

.. code-block:: symbolic

   test suite "User API Integration" {
       setup {
           # Start test server
           server = start_test_server();
           client = HttpClient(base_url="http://localhost:8080");
       }
       
       teardown {
           # Cleanup
           server.stop();
       }
       
       test "create user" {
           user_data = {
               name: "Test User",
               email: "test@example.com",
               password: "secure123"
           };
           
           response = client.post("/api/users", user_data);
           
           assert response.status == 201;
           assert response.data.has_key("id");
           assert response.data.name == "Test User";
       }
       
       test "get user" {
           # First create a user
           create_response = client.post("/api/users", {...});
           user_id = create_response.data.id;
           
           # Then retrieve it
           get_response = client.get($"/api/users/{user_id}");
           
           assert get_response.status == 200;
           assert get_response.data.id == user_id;
       }
   }

Database Testing
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test suite "Database Operations" {
       setup {
           # Setup test database
           db = TestDatabase();
           db.connect();
           db.create_tables();
       }
       
       teardown {
           # Cleanup test database
           db.drop_tables();
           db.disconnect();
       }
       
       test "user creation" {
           user = User(
               name="Test User",
               email="test@example.com",
               created_at=time.now()
           );
           
           # Save to database
           saved_user = db.users.save(user);
           
           # Verify save
           assert saved_user.id != null;
           assert saved_user.name == "Test User";
           
           # Verify retrieval
           retrieved = db.users.find(saved_user.id);
           assert retrieved == saved_user;
       }
       
       test "user deletion" {
           user = create_test_user();
           user_id = user.id;
           
           # Delete user
           db.users.delete(user_id);
           
           # Verify deletion
           assert db.users.find(user_id) == null;
       }
   }

Mocking and Stubbing
--------------------

Function Mocking
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "payment processing with mock" {
       # Create mock payment gateway
       mock_gateway = mock(PaymentGateway);
       
       # Setup mock behavior
       mock_gateway.expect_call("process_payment")
           .with_args(amount=100.0, currency="USD")
           .returns({success: true, transaction_id: "tx_123"});
       
       # Test with mock
       processor = PaymentProcessor(gateway=mock_gateway);
       result = processor.process_order(100.0, "USD");
       
       # Verify expectations
       assert result.success == true;
       assert result.transaction_id == "tx_123";
       mock_gateway.verify();  # Ensure all expected calls were made
   }

Stub Objects
~~~~~~~~~~~~

.. code-block:: symbolic

   test "user service with stubs" {
       # Create stub database
       stub_db = stub(Database);
       stub_db.stub_method("find_user")
           .returns(User(name="Test User", email="test@example.com"));
       
       # Create service with stub
       user_service = UserService(database=stub_db);
       user = user_service.get_user_profile(123);
       
       # Verify service behavior
       assert user.name == "Test User";
       assert user.email == "test@example.com";
   }

Advanced Testing Patterns
-------------------------

Parameterized Tests
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   test "addition with parameters" with [
       [2, 3, 5],
       [0, 5, 5],
       [-2, 3, 1],
       [10, -5, 5]
   ] as (a, b, expected) {
       result = add(a, b);
       assert result == expected;
   }
   
   test "string concatenation" with [
       ["hello", "world", "helloworld"],
       ["", "test", "test"],
       ["a", "b", "ab"]
   ] as (str1, str2, expected)