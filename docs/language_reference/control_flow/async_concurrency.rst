Async & Concurrency
===================

Symbolic provides comprehensive support for asynchronous programming and concurrent execution.

Async/Await Basics
------------------

Async Functions
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn fetch_user_data(user_id) {
       user = await getUser(user_id);
       posts = await getPosts(user_id);
       likes = await getLikes(user_id);
       
       return {
           user: user,
           posts: posts,
           likes: likes
       };
   }

Await Expressions
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn process_data() {
       # Sequential execution
       data1 = await fetch_from_source1();
       data2 = await fetch_from_source2();
       
       # Process after both complete
       result = process(data1, data2);
       return result;
   }

Parallel Execution
------------------

Concurrent Await
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn load_dashboard_data() {
       # Start all operations concurrently
       user_promise = getUserProfile();
       orders_promise = getRecentOrders();
       notifications_promise = getNotifications();
       
       # Wait for all to complete
       [user, orders, notifications] = await all [
           user_promise,
           orders_promise,
           notifications_promise
       ];
       
       return {
           user: user,
           orders: orders,
           notifications: notifications
       };
   }

Parallel Loops
~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn process_images_parallel(images) {
       results = [];
       
       parallel for image in images {
           processed = await apply_filters(image);
           results.append(processed);
       }
       
       return results;
   }

Structured Concurrency
----------------------

Nursery Pattern
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn monitor_system() {
       async using nursery() as n {
           n.start(monitor_cpu());
           n.start(monitor_memory());
           n.start(monitor_network());
           n.start(monitor_disk());
       }
       # All monitoring tasks complete or cancelled
       print("System monitoring stopped");
   }

Timeout Protection
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn fetch_with_timeout(url, timeout_ms = 5000) {
       async using nursery() as n {
           fetch_task = n.start(fetch_url(url));
           timeout_task = n.start(wait(timeout_ms));
           
           winner = await any [fetch_task, timeout_task];
           
           if winner == timeout_task {
               n.cancel_all();  # Cancel the fetch
               throw TimeoutError("Request timed out");
           }
           
           return fetch_task.result;
       }
   }

Practical Examples
------------------

Web API Client
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn fetch_weather_data(city) {
       try {
           # Fetch from multiple sources in parallel
           [open_weather, accu_weather, weather_com] = await all [
               fetch_open_weather(city),
               fetch_accu_weather(city),
               fetch_weather_com(city)
           ];
           
           # Combine and average results
           temperatures = [
               open_weather.temperature,
               accu_weather.temperature,
               weather_com.temperature
           ];
           
           avg_temp = temperatures.sum() / temperatures.length();
           
           return {
               temperature: avg_temp,
               sources: 3,
               confidence: "high"
           };
           
       } catch e {
           # Fallback to single source if others fail
           primary_data = await fetch_open_weather(city);
           return {
               temperature: primary_data.temperature,
               sources: 1,
               confidence: "medium"
           };
       }
   }

Database Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn update_user_recommendations(user_id) {
       async using transaction() as tx {
           try {
               # Parallel data fetching
               [view_history, purchase_history, similar_users] = await all [
                   get_view_history(user_id),
                   get_purchase_history(user_id),
                   find_similar_users(user_id)
               ];
               
               # Generate recommendations
               recommendations = generate_recommendations(
                   view_history,
                   purchase_history,
                   similar_users
               );
               
               # Save recommendations
               await save_recommendations(user_id, recommendations);
               
               # Commit transaction
               await tx.commit();
               return recommendations;
               
           } catch e {
               await tx.rollback();
               throw e;
           }
       }
   }

Real-time Data Processing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn process_sensor_stream(sensors) {
       # Create async channels for data flow
   temperature_chan = channel();
   humidity_chan = channel();
   pressure_chan = channel();
   
   # Start sensor readers
   async using nursery() as n {
       for sensor in sensors {
           n.start(sensor_reader(sensor, temperature_chan, humidity_chan, pressure_chan));
       }
       
       # Start processors
       n.start(temperature_processor(temperature_chan));
       n.start(humidity_processor(humidity_chan));
       n.start(pressure_processor(pressure_chan));
       
       # Start aggregator
       n.start(data_aggregator(temperature_chan, humidity_chan, pressure_chan));
   }
   }

   async fn sensor_reader(sensor, temp_chan, humid_chan, press_chan) {
       while sensor.is_active() {
           reading = await sensor.read();
           
           await all [
               temp_chan.send(reading.temperature),
               humid_chan.send(reading.humidity),
               press_chan.send(reading.pressure)
           ];
           
           await wait(sensor.interval);
       }
   }

File Processing Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn process_large_dataset(files, chunk_size = 1000) {
       results = channel();
       
       async using nursery() as n {
           for file in files {
               n.start(process_file(file, chunk_size, results));
           }
           
           # Collector
           n.start(async {
               all_results = [];
               while has_more_data(results) {
                   chunk_result = await results.receive();
                   all_results.extend(chunk_result);
               }
               return all_results;
           });
       }
   }
   
   async fn process_file(file, chunk_size, results_chan) {
       chunks = file.read_chunks(chunk_size);
       
       parallel for chunk in chunks {
           processed = await process_chunk(chunk);
           await results_chan.send(processed);
       }
   }

Web Server with Middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn web_server() {
       server = create_server();
       
       # Add middleware
       server.use(log_requests);
       server.use(authenticate);
       server.use(rate_limit);
       
       # Add routes
       server.get("/api/users", handle_get_users);
       server.post("/api/users", handle_create_user);
       server.get("/api/users/{id}", handle_get_user);
       
       # Start server
       await server.listen(8080);
   }
   
   async fn handle_get_users(request) {
       # Parallel database queries
       [users, total_count, filters] = await all [
           db.users.find().limit(100),
           db.users.count(),
           get_available_filters()
       ];
       
       return {
           users: users,
           pagination: {
               total: total_count,
               page: request.query.page,
               per_page: 100
           },
           filters: filters
       };
   }

Error Handling in Async Code
----------------------------

Async Try-Catch
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn resilient_operation() {
       try {
           data = await unreliable_api_call();
           return {success: true, data: data};
       } catch e {
           match e {
               NetworkError => {
                   print("Network issue, retrying...");
                   await wait(1000);
                   return await resilient_operation();  # Retry
               }
               TimeoutError => {
                   return {success: false, error: "Operation timed out"};
               }
               _ => {
                   return {success: false, error: "Unexpected error"};
               }
           }
       }
   }

Cancellation
~~~~~~~~~~~~

.. code-block:: symbolic

   async fn search_with_cancellation(query, cancellation_token) {
       try {
           # Pass cancellation token to async operations
           results = await all [
               search_database(query, cancellation_token),
               search_index(query, cancellation_token),
               search_external(query, cancellation_token)
           ];
           
           return combine_results(results);
           
       } catch e {
           if e is CancellationError {
               print("Search was cancelled");
               return [];
           }
           throw e;
       }
   }

Performance Patterns
--------------------

Batching
~~~~~~~~

.. code-block:: symbolic

   async fn batch_process_items(items, batch_size = 50) {
       results = [];
       
       for i in 0..<len(items), batch_size {
           batch = items[i..min(i + batch_size, len(items))];
           
           # Process batch in parallel
           batch_results = await all batch.map(process_item);
           results.extend(batch_results);
       }
       
       return results;
   }

Connection Pooling
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   db_pool = connection_pool(size=10);
   
   async fn execute_query(sql, params) {
       async using db_pool.get_connection() as conn {
           return await conn.execute(sql, params);
       }
   }

Caching with Async
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn get_cached_data(key, fallback_async_fn) {
       # Try cache first
       cached = cache.get(key);
       if cached != null {
           return cached;
       }
       
       # Cache miss - compute async
       data = await fallback_async_fn();
       
       # Store in cache
       cache.set(key, data, ttl=300);
       
       return data;
   }

Best Practices
--------------

Avoid Async Void
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - returns a task
   async fn process_data() {
       # work
   }
   
   # Avoid - fire and forget
   async fn log_async() {  # Implicitly returns void
       # logging
   }

Use Structured Concurrency
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - using nursery for task management
   async using nursery() as n {
       n.start(task1());
       n.start(task2());
   }
   
   # Avoid - unmanaged tasks
   task1();  # No way to cancel or await
   task2();

Handle Errors Gracefully
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn robust_operation() {
       try {
           return await operation();
       } catch e {
           # Log, retry, or provide fallback
           log_error(e);
           return fallback_value;
       }
   }