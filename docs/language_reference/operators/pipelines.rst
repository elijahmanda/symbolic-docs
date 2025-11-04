Pipeline Operators
==================

Pipeline operators allow you to write clean, readable data transformation chains by passing values through a series of operations.

Forward Pipeline (|>)
---------------------

Basic Forward Pipeline
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Basic pipeline - pass data through functions
   result = data
       |> filter(x => x > 0)
       |> map(x => x * 2)
       |> reduce(+, 0);
   
   # Equivalent to:
   # result = reduce(+, map(x => x * 2, filter(x => x > 0, data)));

String Processing Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_text(text) {
       return text
           |> split_lines()
           |> map(line => line.trim())
           |> filter(line => line != "")
           |> map(line => line.upper())
           |> join_lines();
   }
   
   input_text = "
   Hello World
   
   This is a test
   
   Pipeline Example
   ";
   
   output = process_text(input_text);
   # "HELLO WORLD\nTHIS IS A TEST\nPIPELINE EXAMPLE"

Data Transformation Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_sales_data(raw_data) {
       return raw_data
           |> filter(record => record.amount > 0)
           |> map(record => {
               return {
                   date: record.date,
                   amount: record.amount,
                   category: record.category,
                   region: record.region
               };
           })
           |> group_by(record => record.category)
           |> map((category, records) => {
               total = records.map(r => r.amount).sum();
               count = records.length();
               return {
                   category: category,
                   total_sales: total,
                   average_sale: total / count,
                   transaction_count: count
               };
           })
           |> sorted((a, b) => b.total_sales - a.total_sales);
   }

Backward Pipeline (<|)
----------------------

Basic Backward Pipeline
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Backward pipeline - functions applied in reverse order
   result = process_result()
       <| transform_data()
       <| validate_input()
       <| raw_data;
   
   # Equivalent to:
   # result = process_result(transform_data(validate_input(raw_data)))

Mathematical Backward Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Mathematical expressions in backward style
   final_result = display()
       <| format_currency()
       <| calculate_total()
       <| apply_discount()
       <| subtotal;
   
   # Read as: start with subtotal, apply discount, calculate total, format, then display

Parallel Pipeline (||>)
-----------------------

Basic Parallel Pipeline
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process data through multiple pipelines in parallel
   results = data
       ||> process_analysis_1()   # Runs in parallel
       ||> process_analysis_2()   # Runs in parallel
       ||> process_analysis_3();  # Runs in parallel
   
   # All three analyses run concurrently
   # results contains [result1, result2, result3]

Data Enrichment Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn enrich_user_data(user_ids) {
       return user_ids
           ||> fetch_user_profiles()    # Parallel API calls
           ||> fetch_user_preferences()
           ||> fetch_user_activity();
   }
   
   # Usage
   user_ids = [1, 2, 3, 4, 5];
   enriched_data = await enrich_user_data(user_ids);
   # enriched_data = [profiles, preferences, activity]

Error-Handling Pipeline (|?>)
-----------------------------

Safe Pipeline with Error Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Pipeline stops on first error
   result = user_input
       |?> validate_format()     # Stops if invalid
       |?> parse_json()          # Stops if parse fails
       |?> validate_schema()     # Stops if schema invalid
       |?> save_to_database()    # Stops if save fails
       else handle_error;
   
   # If any step fails, handle_error is called with the error

Robust Data Processing
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_customer_data(raw_data) {
       return raw_data
           |?> validate_structure()
           |?> clean_data()
           |?> transform_fields()
           |?> deduplicate_records()
           |?> validate_business_rules()
           else | error => {
               log_error("Data processing failed", error);
               return fallback_data();
           };
   }

Practical Examples
------------------

Web Request Processing
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   async fn handle_http_request(request) {
       return request
           |> validate_authentication()
           |> parse_json_body()
           |> validate_schema()
           |> process_business_logic()
           |> format_response()
           else | error => {
               return error_response(error);
           };
   }
   
   async fn validate_authentication(req) {
       if !req.headers.contains("Authorization") {
           throw UnauthorizedError("Missing authentication");
       }
       # Verify token and return user context
       return {request: req, user: await verify_token(req.headers.Authorization)};
   }

Data Analysis Workflow
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_experiment_data(raw_readings) {
       return raw_readings
           # Data cleaning phase
           |> filter(reading => reading.quality == "good")
           |> map(reading => normalize_reading(reading))
           |> remove_outliers()
           
           # Analysis phase
           |> calculate_statistics()
           |> perform_hypothesis_test()
           |> calculate_confidence_intervals()
           
           # Reporting phase
           |> format_for_report()
           |> generate_visualizations()
           else | error => {
               log_experiment_error(error);
               return generate_error_report(error);
           };
   }

File Processing Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_log_files(files) {
       return files
           |> filter(file => file.exists())
           |> map(file => file.read_text())
           |> flat_map(content => content.split_lines())
           |> filter(line => line.contains("ERROR") or line.contains("WARNING"))
           |> map(line => parse_log_entry(line))
           |> group_by(entry => entry.level)
           |> map((level, entries) => {
               return {
                   level: level,
                   count: entries.length(),
                   examples: entries.take(5),
                   latest: entries.sorted_by(e => e.timestamp).last()
               };
           });
   }

E-commerce Order Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_order(order_data) {
       return order_data
           |?> validate_order_structure()
           |?> check_inventory()
           |?> calculate_pricing()
           |?> apply_promotions()
           |?> process_payment()
           |?> update_inventory()
           |?> send_confirmation()
           |?> schedule_shipping()
           else | error => {
               handle_order_failure(order_data, error);
               throw error;
           };
   }
   
   fn check_inventory(order) {
       for item in order.items {
           stock = get_inventory_level(item.product_id);
           if stock < item.quantity {
               throw OutOfStockError(item.product_id);
           }
       }
       return order;
   }

Machine Learning Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn build_ml_pipeline(training_data) {
       return training_data
           # Data preparation
           |> handle_missing_values()
           |> normalize_features()
           |> encode_categorical()
           |> split_train_test()
           
           # Model training (parallel)
           ||> train_random_forest()
           ||> train_gradient_boosting()
           ||> train_neural_network()
           
           # Model evaluation
           |> map(models => evaluate_models(models, test_data))
           |> select_best_model()
           |> tune_hyperparameters()
           
           # Final model
           |> train_final_model()
           else | error => {
               log_ml_error(error);
               return fallback_model();
           };
   }

Advanced Pipeline Patterns
--------------------------

Conditional Pipelines
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_data_conditionally(data, options) {
       return data
           |> (if options.clean then clean_data else identity)
           |> (if options.normalize then normalize else identity)
           |> (if options.filter then filter_outliers else identity)
           |> (if options.aggregate then aggregate_by_date else identity);
   }
   
   fn identity(x) = x;

Pipeline with Side Effects
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_with_logging(data) {
       return data
           |> tap(x => log_info("Starting processing", x))
           |> transform_step_1()
           |> tap(x => log_debug("After step 1", x))
           |> transform_step_2()
           |> tap(x => log_debug("After step 2", x))
           |> final_transform()
           |> tap(x => log_info("Processing complete", x));
   }
   
   fn tap(value, side_effect_fn) {
       side_effect_fn(value);
       return value;
   }

Nested Pipelines
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn complex_data_processing(raw_data) {
       return raw_data
           |> preprocess()
           |> branch(
               # Branch 1: Statistical analysis
               data => data
                   |> calculate_statistics()
                   |> generate_report(),
               
               # Branch 2: Machine learning
               data => data
                   |> prepare_features()
                   |> train_model()
                   |> evaluate_model()
           )
           |> combine_results();
   }
   
   fn branch(data, *pipelines) {
       return pipelines.map(pipe => pipe(data));
   }

Pipeline Composition
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Create reusable pipeline segments
   data_cleaning_pipeline = 
       filter(x => x != null)
       |> normalize()
       |> validate();
   
   analysis_pipeline =
       calculate_metrics()
       |> generate_insights()
       |> create_visualizations();
   
   full_pipeline = 
       data_cleaning_pipeline
       |> analysis_pipeline;
   
   # Usage
   result = raw_data |> full_pipeline;

Performance Considerations
--------------------------

Lazy Evaluation in Pipelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - lazy evaluation for large datasets
   result = large_dataset
       |> filter(x => x > 1000)      # Only processes matching elements
       |> map(x => expensive_op(x))  # Only called on filtered elements
       |> take(100)                  # Only processes first 100 results
       |> list();                    # Materialize at the end

Eager vs Lazy Pipelines
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Eager evaluation (immediate processing)
   eager_result = data.list()        # Convert to list first
       |> map(x => x * 2)            # Processes entire list
       |> filter(x => x > 10);       # Processes entire list
   
   # Lazy evaluation (on-demand processing)
   lazy_result = data                # Keep as iterator
       |> map(x => x * 2)            # No processing yet
       |> filter(x => x > 10)        # No processing yet
       |> take(50)                   # Only processes 50 elements
       |> list();                    # Now processes

Memory-Efficient Pipelines
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process data in chunks to reduce memory usage
   fn process_large_file(filename) {
       return read_file_chunks(filename, chunk_size=1000)
           |> flat_map(chunk => chunk.split_lines())
           |> map(line => parse_line(line))
           |> filter(record => record.is_valid())
           |> map(record => transform_record(record))
           |> batch(100)                    # Process in batches
           |> map(batch => save_batch(batch))
           |> reduce((success, total) => success + total, 0);
   }

Best Practices
--------------

Keep Pipelines Readable
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - clear, step-by-step transformation
   result = data
       |> clean_input()
       |> validate_format()
       |> extract_features()
       |> calculate_metrics()
       |> format_output();
   
   # Avoid - overly complex one-liners
   # result = data |> clean() |> validate() |> extract() |> calculate() |> format();

Use Descriptive Function Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - descriptive names at each step
   user_report = raw_data
       |> remove_incomplete_records()
       |> calculate_user_engagement()
       |> segment_by_activity_level()
       |> generate_recommendations()
       |> format_for_dashboard();
   
   # Avoid - unclear what each step does
   # result = data |> step1() |> step2() |> step3() |> step4();

Handle Errors Appropriately
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - proper error handling
   result = input_data
       |?> validate_structure()
       |?> clean_values()
       |?> apply_business_rules()
       else | error => {
           log_error("Pipeline failed", error);
           return get_fallback_data();
       };
   
   # Avoid - silent failures
   # result = data |> try_step1() |> try_step2() |> try_step3();

Use Parallel Pipelines for Independent Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - parallel independent operations
   user_insights = user_data
       ||> calculate_demographics()    # Independent
       ||> analyze_behavior()          # Independent
       ||> predict_preferences();      # Independent
   
   # Avoid - sequential independent operations
   # user_insights = user_data
   #    |> calculate_demographics()
   #    |> analyze_behavior()          # Waits for demographics
   #    |> predict_preferences();      # Waits for behavior analysis