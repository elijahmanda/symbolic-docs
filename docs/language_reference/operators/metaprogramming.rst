Metaprogramming
===============

Metaprogramming in Symbolic allows programs to examine and modify their own structure and behavior at runtime.

Annotations
-----------

Function Annotations
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   @deprecated("Use new_function instead")
   @timing
   @cache(ttl=300)
   fn old_function(x) {
       return x * 2;
   }

   @validate_input(types=[Integer, Float])
   @retry(max_attempts=3)
   @log_arguments
   fn api_call(url, data) {
       # Function implementation
   }

Class Annotations
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   @serializable
   @author("Alice Developer")
   @version("1.2.0")
   class User {
       @required
       name: String;
       
       @range(0, 150)
       age: Integer;
       
       @email_format
       email: String;
   }

   @singleton
   @thread_safe
   class DatabaseConnection {
       @lazy
       connection_pool = create_pool();
   }

Custom Annotations
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Define custom annotation
   annotation timing {
       fn __apply__(target) {
           original = target;
           return fn (...args) {
               start = time.now();
               result = original(...args);
               duration = time.now() - start;
               print($"${target.name} took ${duration}ms");
               return result;
           };
       }
   }

   annotation cache {
       fn __init__(ttl=300) {
           self.ttl = ttl;
       }
       
       fn __apply__(target) {
           cache_data = {};
           return fn (...args) {
               key = hash(args);
               if key in cache_data {
                   value, timestamp = cache_data[key];
                   if time.now() - timestamp < self.ttl {
                       return value;
                   }
               }
               result = target(...args);
               cache_data[key] = (result, time.now());
               return result;
           };
       }
   }

Reflection
----------

Type Inspection
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn inspect_value(value) {
       type_name = value.type_name();
       methods = value.methods();
       attributes = value.attributes();
       is_callable = value.is_callable();
       
       print($"Type: {type_name}");
       print($"Methods: {methods}");
       print($"Attributes: {attributes}");
       print($"Callable: {is_callable}");
   }

   fn analyze_function(func) {
       name = func.name;
       parameters = func.parameters;
       return_type = func.return_type;
       source_code = func.source;
       
       print($"Function: {name}");
       print($"Parameters: {parameters}");
       print($"Returns: {return_type}");
       print($"Source: {source_code}");
   }

Runtime Modification
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Add methods at runtime
   class Calculator {
       fn add(a, b) = a + b;
   }

   # Add multiplication method dynamically
   Calculator.multiply = (a, b) => a * b;

   calc = Calculator();
   print(calc.multiply(5, 3));  # 15

   # Modify existing method
   original_add = Calculator.add;
   Calculator.add = (a, b) => {
       print($"Adding {a} and {b}");
       return original_add(a, b);
   };

Macros
------

Code Generation
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   macro vector_operations(type_name) {
       return quote {
           class $(type_name) {
               fn __init__(self, x, y, z) {
                   self.x = x;
                   self.y = y;
                   self.z = z;
               }
               
               fn __add__(self, other) {
                   return $(type_name)(
                       self.x + other.x,
                       self.y + other.y,
                       self.z + other.z
                   );
               }
               
               fn dot(self, other) {
                   return self.x * other.x + self.y * other.y + self.z * other.z;
               }
               
               fn magnitude(self) {
                   return (self.x^2 + self.y^2 + self.z^2).sqrt();
               }
           }
       };
   }

   # Use macro to generate Vector3D class
   Vector3D = vector_operations("Vector3D");

   v1 = Vector3D(1, 2, 3);
   v2 = Vector3D(4, 5, 6);
   print(v1 + v2);  # Vector3D(5, 7, 9)

Domain-Specific Languages
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   macro sql_query {
       fn select(*columns) {
           return fn (table) {
               return fn (where_condition = null) {
                   query = "SELECT " + columns.join(", ") + " FROM " + table;
                   if where_condition != null {
                       query += " WHERE " + where_condition;
                   }
                   return query;
               };
           };
       }
   }

   # Usage
   with sql_query {
       users_query = select("id", "name", "email")("users")("age > 18");
       print(users_query);  # "SELECT id, name, email FROM users WHERE age > 18"
   }

Dynamic Code Evaluation
-----------------------

String Evaluation
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Evaluate expressions from strings
   expression = "2 + 3 * 4";
   result = eval(expression);
   print(result);  # 14

   # Create functions dynamically
   function_string = "(x) => x * x + 2*x + 1";
   dynamic_function = eval(function_string);
   print(dynamic_function(5));  # 36

   # Template-based code generation
   fn create_getter(attribute_name) {
       code = "
           fn get_$(attribute_name)(self) {
               return self.$(attribute_name);
           }
       ";
       return eval(code);
   }

Runtime Code Modification
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class DynamicClass {
       # Empty class to be modified at runtime
   }

   # Add methods dynamically
   method_names = ["save", "load", "update", "delete"];
   for method_name in method_names {
       method_code = "
           fn $(method_name)(self, *args) {
               print('Calling $(method_name) with args: ' + args.to_string());
               return 'result from $(method_name)';
           }
       ";
       DynamicClass[method_name] = eval(method_code);
   }

   obj = DynamicClass();
   print(obj.save("data"));  # "Calling save with args: ['data']"

Practical Examples
------------------

Validation Framework
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   annotation validate {
       fn __init__(*validators) {
           self.validators = validators;
       }
       
       fn __apply__(target) {
           return fn (...args) {
               # Run validators before function execution
               for validator in self.validators {
                   validator(args);
               }
               return target(...args);
           };
       }
   }

   annotation not_null {
       fn __apply__(target) {
           return fn (...args) {
               for arg in args {
                   if arg == null {
                       throw "Argument cannot be null";
                   }
               }
               return target(...args);
           };
       }
   }

   @validate(not_null)
   @cache(ttl=60)
   fn expensive_operation(data) {
       # Only called with valid data, and results are cached
       return complex_calculation(data);
   }

API Route Generation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   macro rest_controller {
       fn (model_class) {
           class_name = model_class.name + "Controller";
           
           return quote {
               class $(class_name) {
                   @route("/$(model_class.name.lower())s")
                   fn index() {
                       return $(model_class).all();
                   }
                   
                   @route("/$(model_class.name.lower())s/{id}")
                   fn show(id) {
                       return $(model_class).find(id);
                   }
                   
                   @route("/$(model_class.name.lower())s", method="POST")
                   fn create(data) {
                       return $(model_class).create(data);
                   }
               }
           };
       }
   }

   # Generate REST controller for User model
   UserController = rest_controller(User);

Configuration System
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   macro config_section {
       fn (section_name) {
           return quote {
               class $(section_name)Config {
                   fn __init__(self) {
                       self._values = {};
                   }
                   
                   fn __getattr__(self, name) {
                       if name in self._values {
                           return self._values[name];
                       }
                       # Look in environment variables
                       env_var = "${section_name.upper()}_${name.upper()}";
                       if env_var in environ {
                           return environ[env_var];
                       }
                       return null;
                   }
                   
                   fn __setattr__(self, name, value) {
                       if name.startswith("_") {
                           super().__setattr__(name, value);
                       } else {
                           self._values[name] = value;
                       }
                   }
               }
           };
       }
   }

   # Generate configuration sections
   DatabaseConfig = config_section("database");
   CacheConfig = config_section("cache");

   db_config = DatabaseConfig();
   db_config.host = "localhost";
   print(db_config.port);  # Checks DATABASE_PORT environment variable

Best Practices
--------------

Use Metaprogramming Judiciously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - clear benefit
   @cache(ttl=300)
   fn expensive_database_query() {
       # Results cached for 5 minutes
   }
   
   # Avoid - unnecessary complexity
   fn dynamically_generated_simple_function() {
       # Overly complex for simple task
   }

Document Generated Code
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   macro generated_class {
       fn (name) {
           return quote {
               # AUTO-GENERATED CLASS - DO NOT EDIT MANUALLY
               # Generated from macro: generated_class
               class $(name) {
                   # Class implementation...
               }
           };
       }
   }

Security Considerations
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Dangerous - arbitrary code execution
   user_input = get_user_input();
   result = eval(user_input);  # Potential security risk!
   
   # Safer - restricted evaluation
   safe_globals = {"sqrt": sqrt, "sin": sin, "cos": cos};
   result = eval(user_input, safe_globals);  # Only safe functions available

Performance Impact
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Runtime code generation has cost
   fn create_many_functions() {
       for i in 0..<1000 {
           # Each eval call has overhead
           dynamic_fn = eval("(x) => x + $(i)");
       }
   }
   
   # Consider precompilation for performance-critical code