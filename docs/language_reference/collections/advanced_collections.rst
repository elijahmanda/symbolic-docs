Advanced Collections
====================

Symbolic provides advanced collection types and patterns for specialized use cases.

Deques (Double-Ended Queues)
----------------------------

Basic Deque Operations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   from collections import deque;
   
   # Create deque
   dq = deque([1, 2, 3]);
   
   # Add elements
   dq.append(4);           # Add to right: [1, 2, 3, 4]
   dq.append_left(0);      # Add to left: [0, 1, 2, 3, 4]
   
   # Remove elements
   right = dq.pop();       # Remove from right: 4
   left = dq.pop_left();   # Remove from left: 0
   
   # Access elements
   first = dq[0];          # 1
   last = dq[-1];          # 3

Deque Practical Examples
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_task_queue(tasks) {
       queue = deque(tasks);
       completed = [];
       
       while queue.length() > 0 {
           # Process from front
           task = queue.pop_left();
           result = execute_task(task);
           
           if result == "retry" {
               # Move to back of queue
               queue.append(task);
           } else {
               completed.append((task, result));
           }
           
           # Limit processing time
           if completed.length() >= 1000 {
               break;
           }
       }
       
       return completed;
   }
   
   fn sliding_window_maximum(numbers, window_size) {
       if numbers.length() < window_size {
           return [];
       }
       
       result = [];
       dq = deque();
       
       for i in 0..<numbers.length() {
           # Remove elements outside window
           if dq.length() > 0 and dq[0] <= i - window_size {
               dq.pop_left();
           }
           
           # Remove smaller elements
           while dq.length() > 0 and numbers[dq[-1]] <= numbers[i] {
               dq.pop();
           }
           
           dq.append(i);
           
           # Record maximum for full windows
           if i >= window_size - 1 {
               result.append(numbers[dq[0]]);
           }
       }
       
       return result;
   }

DefaultDict
-----------

Automatic Default Values
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   from collections import defaultdict;
   
   # Defaultdict with factory function
   word_count = defaultdict(() => 0);
   for word in text.split() {
       word_count[word] += 1;  # No KeyError for new words
   }
   
   # Defaultdict with list factory
   grouped_data = defaultdict(() => []);
   for item in data {
       grouped_data[item.category].append(item);
   }
   
   # Defaultdict with set factory
   unique_values = defaultdict(() => set());
   for record in records {
       unique_values[record.type].add(record.value);
   }

DefaultDict Examples
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn group_students_by_grade(students) {
       grades = defaultdict(() => []);
       
       for student in students {
           grade = calculate_grade(student.score);
           grades[grade].append(student);
       }
       
       return grades;
   }
   
   fn build_inverted_index(documents) {
       index = defaultdict(() => set());
       
       for doc_id, content in documents.entries() {
           words = extract_words(content);
           for word in words {
               index[word].add(doc_id);
           }
       }
       
       return index;
   }

OrderedDict
-----------

Maintaining Insertion Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   from collections import ordered_dict;
   
   # Create ordered dictionary
   config = ordered_dict();
   config["database"] = "localhost";
   config["port"] = 5432;
   config["username"] = "admin";
   config["password"] = "secret";
   
   # Order is preserved
   for key in config.keys() {
       print(key);  # database, port, username, password (insertion order)
   }
   
   # Move to end
   config.move_to_end("database");
   # Now order: port, username, password, database

OrderedDict Examples
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class LRUCache {
       capacity = 100;
       cache = ordered_dict();
       
       fn get(key) {
           if key in self.cache {
               # Move to end (most recently used)
               value = self.cache[key];
               self.cache.move_to_end(key);
               return value;
           }
           return null;
       }
       
       fn set(key, value) {
           if key in self.cache {
               # Update existing
               self.cache[key] = value;
               self.cache.move_to_end(key);
           } else {
               # Add new, evict if needed
               if self.cache.length() >= self.capacity {
                   # Remove least recently used (first item)
                   self.cache.pop_left();
               }
               self.cache[key] = value;
           }
       }
   }
   
   fn process_tasks_in_order(tasks) {
       # Maintain task execution order
       task_queue = ordered_dict();
       
       for task in tasks {
           task_queue[task.id] = task;
       }
       
       # Process in insertion order
       while task_queue.length() > 0 {
           task_id, task = task_queue.pop_left();
           execute_task(task);
       }
   }

Counter
-------

Element Counting
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   from collections import counter;
   
   # Basic counting
   words = ["apple", "banana", "apple", "cherry", "banana", "apple"];
   word_counts = counter(words);
   print(word_counts["apple"]);   # 3
   print(word_counts["banana"]);  # 2
   
   # Update counts
   word_counts.update(["apple", "date"]);
   print(word_counts["apple"]);   # 4
   print(word_counts["date"]);    # 1
   
   # Most common elements
   top_2 = word_counts.most_common(2);
   # [("apple", 4), ("banana", 2)]

Counter Examples
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn find_anagrams(words) {
       anagram_groups = defaultdict(() => []);
       
       for word in words {
           # Use sorted characters as key
           key = tuple(word.lower().sorted());
           anagram_groups[key].append(word);
       }
       
       # Filter groups with multiple words
       return anagram_groups.entries()
           .filter((key, group) => group.length() > 1)
           .map((key, group) => group);
   }
   
   fn analyze_network_packets(packets) {
       packet_types = counter();
       source_ips = counter();
       destination_ports = counter();
       
       for packet in packets {
           packet_types[packet.type] += 1;
           source_ips[packet.source_ip] += 1;
           destination_ports[packet.destination_port] += 1;
       }
       
       return {
           "common_types": packet_types.most_common(5),
           "busy_ips": source_ips.most_common(10),
           "popular_ports": destination_ports.most_common(10)
       };
   }

ChainMap
--------

Multiple Context Search
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   from collections import chain_map;
   
   # Create layered configuration
   defaults = {"color": "red", "size": "medium"};
   user_prefs = {"color": "blue", "theme": "dark"};
   session_settings = {"language": "en"};
   
   config = chain_map(session_settings, user_prefs, defaults);
   
   # Search order: session -> user -> defaults
   print(config["color"]);    # "blue" (from user_prefs)
   print(config["size"]);     # "medium" (from defaults)
   print(config["theme"]);    # "dark" (from user_prefs)

ChainMap Examples
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class ScopedVariables {
       scopes = [{}];
       
       fn enter_scope() {
           self.scopes.insert(0, {});
       }
       
       fn exit_scope() {
           if self.scopes.length() > 1 {
               self.scopes.pop_left();
           }
       }
       
       fn set(name, value) {
           self.scopes[0][name] = value;
       }
       
       fn get(name) {
           for scope in self.scopes {
               if name in scope {
                   return scope[name];
               }
           }
           return null;
       }
   }
   
   fn resolve_configuration(layers) {
       # layers: [most_specific, ..., most_general]
       config = chain_map(*layers);
       
       # Access searches from most specific to most general
       return {
           key: config[key]
           for key in config.keys()
       };
   }

NamedTuple
----------

Structured Data with Names
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   from collections import named_tuple;
   
   # Define named tuple type
   Point = named_tuple("Point", ["x", "y"]);
   Person = named_tuple("Person", ["name", "age", "profession"]);
   
   # Create instances
   p1 = Point(10, 20);
   p2 = Point(x=5, y=15);
   person = Person("Alice", 30, "Engineer");
   
   # Access by name or index
   print(p1.x);        # 10
   print(p1[0]);       # 10
   print(person.name); # "Alice"

NamedTuple Examples
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Database record types
   User = named_tuple("User", ["id", "username", "email", "created_at"]);
   Product = named_tuple("Product", ["sku", "name", "price", "category"]);
   Order = named_tuple("Order", ["id", "user_id", "total", "status"]);
   
   fn process_user_data(raw_data) {
       users = [];
       for record in raw_data {
           user = User(
               id=record[0],
               username=record[1],
               email=record[2],
               created_at=parse_date(record[3])
           );
           users.append(user);
       }
       
       # Access with meaningful names
       for user in users {
           if user.email.contains("@company.com") {
               process_employee(user);
           }
       }
       
       return users;
   }
   
   # Scientific data points
   DataPoint = named_tuple("DataPoint", [
       "timestamp", "value", "quality", "sensor_id"
   ]);
   
   fn analyze_sensor_data(points) {
       valid_points = points.filter(p => p.quality == "good");
       
       values = valid_points.map(p => p.value);
       timestamps = valid_points.map(p => p.timestamp);
       
       return {
           "average": values.sum() / values.length(),
           "min": values.min(),
           "max": values.max(),
           "duration": timestamps.max() - timestamps.min()
       };
   }

Advanced Patterns
-----------------

Composite Collections
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class MultiIndexCollection {
       primary_index = {};
       secondary_indices = {};
       
       fn __init__(self, primary_key, *secondary_keys) {
           self.primary_key = primary_key;
           for key in secondary_keys {
               self.secondary_indices[key] = defaultdict(() => set());
           }
       }
       
       fn add(self, item) {
           primary_value = item[self.primary_key];
           self.primary_index[primary_value] = item;
           
           for key_name, index in self.secondary_indices.entries() {
               value = item[key_name];
               index[value].add(primary_value);
           }
       }
       
       fn get_by_primary(self, value) {
           return self.primary_index.get(value);
       }
       
       fn get_by_secondary(self, key_name, value) {
           if key_name in self.secondary_indices {
               primary_keys = self.secondary_indices[key_name].get(value, set());
               return [self.primary_index[pk] for pk in primary_keys];
           }
           return [];
       }
   }
   
   # Usage: User collection indexed by id, email, and department
   users = MultiIndexCollection("id", "email", "department");
   users.add({"id": 1, "name": "Alice", "email": "alice@x.com", "department": "eng"});
   users.add({"id": 2, "name": "Bob", "email": "bob@x.com", "department": "sales"});
   
   alice = users.get_by_primary(1);
   engineering_users = users.get_by_secondary("department", "eng");

Cached Collections
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class CachedCollection {
       data = [];
       cache = {};
       cache_ttl = 300;  # 5 minutes
       
       fn __init__(self, initial_data = []) {
           self.data = initial_data;
       }
       
       fn query_with_cache(self, query_fn, cache_key) {
           now = time.now();
           
           if cache_key in self.cache {
               cached_value, timestamp = self.cache[cache_key];
               if now - timestamp < self.cache_ttl {
                   return cached_value;
               }
           }
           
           # Compute and cache
           result = query_fn(self.data);
           self.cache[cache_key] = (result, now);
           return result;
       }
       
       fn invalidate_cache(self, pattern = null) {
           if pattern == null {
               self.cache.clear();
           } else {
               keys_to_remove = self.cache.keys()
                   .filter(key => key.matches(pattern));
               for key in keys_to_remove {
                   del self.cache[key];
               }
           }
       }
   }

Performance Collections
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class PriorityQueue {
       heap = [];
       
       fn push(self, item, priority) {
           self.heap.append((priority, item));
           self._bubble_up(len(self.heap) - 1);
       }
       
       fn pop(self) {
           if self.heap.is_empty() {
               return null;
           }
           
           # Swap root with last element
           self._swap(0, len(self.heap) - 1);
           priority, item = self.heap.pop();
           
           if !self.heap.is_empty() {
               self._bubble_down(0);
           }
           
           return item;
       }
       
       fn _bubble_up(self, index) {
           # Implementation details...
       }
       
       fn _bubble_down(self, index) {
           # Implementation details...
       }
   }

Best Practices
--------------

Choose the Right Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Use Case: Frequency counting
   # Good: Counter
   word_freq = counter(words);
   
   # Use Case: LRU caching
   # Good: OrderedDict
   cache = ordered_dict();
   
   # Use Case: Stack/Queue operations
   # Good: Deque
   stack = deque();
   
   # Use Case: Layered configuration
   # Good: ChainMap
   config = chain_map(user_settings, defaults);

Consider Memory vs Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Memory efficient but slower access
   large_list = (1..1000000).list();
   
   # Faster access but more memory
   large_set = set(1..1000000);
   large_dict = {x: x for x in 1..1000000};

Use Specialized Collections for Specific Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Don't reinvent the wheel
   from collections import counter, deque, defaultdict;
   
   # Instead of manual implementation:
   # word_count = {};
   # for word in words:
   #     word_count[word] = (word_count[word] or 0) + 1
   
   # Use:
   word_count = counter(words);