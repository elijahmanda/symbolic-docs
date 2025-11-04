Dictionaries
============

Dictionaries are key-value stores that provide fast lookup, insertion, and deletion operations.

Dictionary Creation
-------------------

Basic Creation
~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Empty dictionary
   empty_dict = {};
   
   # With initial values
   person = {
       "name": "Alice",
       "age": 30,
       "city": "New York"
   };
   
   # Using different key types
   mixed_keys = {
       "string_key": "value",
       42: "number_key",
       true: "boolean_key"
   };
   
   # From list of pairs
   pairs = [["a", 1], ["b", 2], ["c", 3]];
   from_pairs = dict(pairs);

Dictionary Comprehension
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Simple comprehension
   squares = {x: x * x for x in 1..5};
   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
   
   # With condition
   even_squares = {x: x * x for x in 1..10 if x % 2 == 0};
   
   # Transforming keys and values
   lengths = {word: word.length() for word in ["apple", "banana", "cherry"]};

Dictionary Operations
---------------------

Accessing Values
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   person = {"name": "Alice", "age": 30};
   
   # Basic access
   name = person["name"];        # "Alice"
   
   # Safe access with default
   country = person.get("country", "USA");  # "USA"
   
   # Check existence
   has_age = "age" in person;    # true
   has_country = "country" in person;  # false

Modifying Dictionaries
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   person = {"name": "Alice"};
   
   # Add/update
   person["age"] = 30;           # {"name": "Alice", "age": 30}
   person["city"] = "Boston";    # Add new key
   
   # Update multiple values
   person.update({"age": 31, "country": "USA"});
   
   # Remove keys
   removed = person.remove("city");  # Remove and return value
   del person["country"];           # Remove without return
   
   # Clear all
   person.clear();                 # {}

Dictionary Methods
------------------

Key and Value Operations
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   inventory = {"apples": 10, "bananas": 5, "oranges": 8};
   
   # Keys and values
   keys = inventory.keys();    # ["apples", "bananas", "oranges"]
   values = inventory.values(); # [10, 5, 8]
   entries = inventory.entries(); # [["apples", 10], ["bananas", 5], ...]
   
   # Length and checks
   count = inventory.length();  # 3
   is_empty = inventory.is_empty();  # false

Advanced Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   defaults = {"color": "red", "size": "medium"};
   user_prefs = {"color": "blue"};
   
   # Merge dictionaries
   merged = defaults.merge(user_prefs);  # {"color": "blue", "size": "medium"}
   
   # Filter
   high_stock = inventory.filter((item, quantity) => quantity > 7);
   # {"apples": 10, "oranges": 8}
   
   # Map values
   doubled = inventory.map_values(quantity => quantity * 2);
   # {"apples": 20, "bananas": 10, "oranges": 16}

Default Dictionaries
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Dictionary with default values
   word_count = dict().with_default(0);
   for word in text.split() {
       word_count[word] += 1;  # No KeyError for new words
   }
   
   # Using get_or_create
   user_sessions = {};
   for user in active_users {
       session = user_sessions.get_or_create(user.id, () => create_session());
       session.update_activity();
   }

Practical Examples
------------------

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Config {
       defaults = {
           "database.host": "localhost",
           "database.port": 5432,
           "cache.enabled": true,
           "cache.ttl": 3600,
           "logging.level": "info"
       };
       
       user_config = {};
       
       fn load_config(file_path) {
           try {
               content = read_file(file_path);
               self.user_config = parse_json(content);
           } catch e {
               print("Using default configuration");
           }
       }
       
       fn get(key) {
           # User config overrides defaults
           return self.user_config.get(key) or self.defaults.get(key);
       }
       
       fn set(key, value) {
           self.user_config[key] = value;
       }
   }

API Response Processing
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_api_responses(responses) {
       aggregated = {
           "successful": [],
           "failed": [],
           "timings": {},
           "errors": {}
       };
       
       for response in responses {
           endpoint = response.endpoint;
           
           if response.status == 200 {
               aggregated["successful"].append(response);
               aggregated["timings"][endpoint] = response.duration;
           } else {
               aggregated["failed"].append(response);
               
               # Group errors by type
               error_type = response.error_type or "unknown";
               aggregated["errors"][error_type] = 
                   (aggregated["errors"][error_type] or 0) + 1;
           }
       }
       
       # Calculate statistics
       total_time = aggregated["timings"].values().sum();
       avg_time = total_time / aggregated["successful"].length();
       
       aggregated["stats"] = {
           "total_requests": responses.length(),
           "success_rate": aggregated["successful"].length() / responses.length(),
           "average_time": avg_time
       };
       
       return aggregated;
   }

Caching System
~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Cache {
       data = {};
       timestamps = {};
       max_size = 1000;
       ttl = 300;  # 5 minutes
       
       fn get(key) {
           if key in self.data {
               # Check if expired
               if time.now() - self.timestamps[key] > self.ttl {
                   self.remove(key);
                   return null;
               }
               
               # Update access time (LRU)
               self.timestamps[key] = time.now();
               return self.data[key];
           }
           return null;
       }
       
       fn set(key, value) {
           # Evict if needed
           if self.data.length() >= self.max_size {
               self.evict_oldest();
           }
           
           self.data[key] = value;
           self.timestamps[key] = time.now();
       }
       
       fn evict_oldest() {
           oldest_key = self.timestamps.entries()
               .sorted((a, b) => a[1] - b[1])
               .first()[0];
           self.remove(oldest_key);
       }
       
       fn remove(key) {
           del self.data[key];
           del self.timestamps[key];
       }
   }

Data Transformation
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn transform_data_for_visualization(raw_data) {
       # Group by category
       grouped = {};
       for item in raw_data {
           category = item.category or "uncategorized";
           if category not in grouped {
               grouped[category] = [];
           }
           grouped[category].append(item);
       }
       
       # Calculate summary statistics per category
       result = {};
       for category, items in grouped {
           values = items.map(item => item.value);
           
           result[category] = {
               "count": items.length(),
               "total": values.sum(),
               "average": values.sum() / values.length(),
               "min": values.min(),
               "max": values.max(),
               "items": items
           };
       }
       
       return result;
   }

Word Frequency Analysis
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_word_frequency(text) {
       words = text.lower()
           .split(/[^\w]+/)
           .filter(word => word != "");
       
       frequency = {};
       for word in words {
           frequency[word] = (frequency[word] or 0) + 1;
       }
       
       # Get top N words
       top_words = frequency.entries()
           .sorted((a, b) => b[1] - a[1])
           .take(20)
           .map(entry => {
               return {
                   "word": entry[0],
                   "count": entry[1],
                   "frequency": entry[1] / words.length()
               };
           });
       
       return {
           "total_words": words.length(),
           "unique_words": frequency.length(),
           "top_words": top_words,
           "word_frequency": frequency
       };
   }

Performance Tips
----------------

Use Dictionary Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - comprehension is optimized
   mapping = {x: x * x for x in 1..1000};
   
   # Less efficient
   mapping = {};
   for x in 1..1000 {
       mapping[x] = x * x;
   }

Use get() for Safe Access
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - safe access with default
   value = data.get("key", default_value);
   
   # Risky - may throw KeyError
   value = data["key"];  # Throws if key doesn't exist

Prefer update() for Multiple Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - single operation
   config.update({"timeout": 30, "retries": 3, "debug": true});
   
   # Less efficient - multiple operations
   config["timeout"] = 30;
   config["retries"] = 3;
   config["debug"] = true;

Use entries() for Iteration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - efficient iteration
   for key, value in data.entries() {
       process(key, value);
   }
   
   # Less efficient
   for key in data.keys() {
       value = data[key];
       process(key, value);
   }