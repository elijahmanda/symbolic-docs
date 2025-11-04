Type System
===========

Symbolic features a rich, flexible type system with type inference, union types, generics, and advanced type operations.

Type Annotations
----------------

Basic Type Annotations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Variable type annotations
   name: String = "Alice";
   age: Integer = 30;
   temperature: Float = 98.6;
   is_active: Boolean = true;
   
   # Function parameter and return type annotations
   fn calculate_area(length: Float, width: Float) -> Float {
       return length * width;
   }
   
   fn find_user(email: String) -> User | null {
       # Returns User or null
   }

Collection Type Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # List types
   numbers: [Integer] = [1, 2, 3, 4, 5];
   mixed_list: [String | Integer] = ["hello", 42, "world"];
   matrix: [[Float]] = [[1.0, 2.0], [3.0, 4.0]];
   
   # Dictionary types
   user_data: {String: Any} = {"name": "Alice", "age": 30};
   scores: {String: Float} = {"math": 95.5, "science": 88.0};
   
   # Set types
   unique_ids: {Integer} = {1, 2, 3, 4, 5};
   tags: {String} = {"urgent", "important", "review"};

Union Types
-----------

Basic Union Types
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Variables that can hold multiple types
   identifier: String | Integer = "user123";
   identifier = 123;  # Also valid
   
   result: Boolean | String = true;
   result = "success";  # Valid
   
   # Function with union return type
   fn parse_input(input: String) -> Integer | Float | String {
       try {
           return input.to_int();
       } catch e {
           try {
               return input.to_float();
           } catch e {
               return input;  # Return original string if not numeric
           }
       }
   }

Advanced Union Patterns
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Complex union types
   api_response: {String: Any} | [Any] | String | Integer;
   
   fn handle_response(response: api_response) {
       match response {
           {String: Any} => process_object(response);
           [Any] => process_array(response);
           String => process_string(response);
           Integer => process_number(response);
       }
   }
   
   # Optional types (shorthand for T | null)
   optional_name: String? = "Alice";
   optional_name = null;  # Valid
   
   fn find_user(id: Integer) -> User? {
       # Returns User or null
   }

Generic Types
-------------

Generic Functions
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn identity[T](value: T) -> T {
       return value;
   }
   
   fn first_element[T](list: [T]) -> T? {
       if list.is_empty() {
           return null;
       }
       return list[0];
   }
   
   fn merge_dicts[K, V](dict1: {K: V}, dict2: {K: V}) -> {K: V} {
       return dict1.merge(dict2);
   }

Generic Classes
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Box[T] {
       value: T;
       
       fn __init__(self, value: T) {
           self.value = value;
       }
       
       fn get(self) -> T {
           return self.value;
       }
       
       fn set(self, value: T) {
           self.value = value;
       }
   }
   
   class Pair[A, B] {
       first: A;
       second: B;
       
       fn __init__(self, first: A, second: B) {
           self.first = first;
           self.second = second;
       }
   }

Generic Protocols
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Container[T] {
       fn add(self, item: T);
       fn remove(self, item: T) -> Boolean;
       fn contains(self, item: T) -> Boolean;
   }
   