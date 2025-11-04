While Loops
===========

While loops repeatedly execute a block of code as long as a condition remains true.

Basic While Loop
----------------

Simple Condition
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   count = 0;
   while count < 5 {
       print(count);
       count += 1;
   }
   # Output: 0, 1, 2, 3, 4

Condition with Function Call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Process until queue is empty
   while !queue.is_empty() {
       item = queue.pop();
       process(item);
   }

Infinite While Loop
-------------------

.. code-block:: symbolic

   # Server main loop
   while true {
       request = await server.accept();
       handle_request(request);
   }

   # Event processing loop
   while true {
       event = get_next_event();
       if event == "quit" {
           stop;
       }
       process_event(event);
   }

Do-While Equivalent (Repeat-Until)
----------------------------------

.. code-block:: symbolic

   # Execute at least once, then check condition
   repeat {
       guess = input("Guess a number: ");
       print($"You guessed: {guess}");
   } until guess == "42";

   # Password validation
   repeat {
       password = input("Enter password: ");
       is_valid = validate_password(password);
       if !is_valid {
           print("Invalid password. Try again.");
       }
   } until is_valid;

Practical Examples
------------------

Number Guessing Game
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn guessing_game() {
       secret_number = random(1, 100);
       attempts = 0;
       guessed = false;
       
       print("Guess the number between 1 and 100!");
       
       while !guessed {
           guess = input("Your guess: ").to_int();
           attempts += 1;
           
           if guess == secret_number {
               print($"Congratulations! You guessed it in {attempts} attempts.");
               guessed = true;
           } else if guess < secret_number {
               print("Too low! Try again.");
           } else {
               print("Too high! Try again.");
           }
       }
   }

Input Validation
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn get_valid_age() {
       age = null;
       while age == null {
           input_str = input("Enter your age: ");
           try {
               age = input_str.to_int();
               if age < 0 or age > 150 {
                   print("Please enter a valid age (0-150).");
                   age = null;
               }
           } catch e {
               print("Please enter a valid number.");
           }
       }
       return age;
   }

Data Processing Until Condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn process_until_threshold(data, threshold) {
       processed = [];
       total = 0;
       index = 0;
       
       while total < threshold and index < len(data) {
           value = data[index];
           processed.append(value);
           total += value;
           index += 1;
       }
       
       return processed;
   }

   numbers = [10, 20, 30, 40, 50, 60];
   result = process_until_threshold(numbers, 100);
   print(result);  # [10, 20, 30, 40] (sum = 100)

Simulation Loops
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn simulate_population_growth(initial_population, growth_rate, carrying_capacity, generations) {
       population = initial_population;
       year = 0;
       
       while year < generations and population > 0 and population < carrying_capacity * 2 {
           growth = population * growth_rate * (1 - population / carrying_capacity);
           population += growth;
           year += 1;
           
           print($"Year {year}: Population = {population:.0f}");
           
           if population <= 0 {
               print("Population went extinct!");
           }
       }
       
       return population;
   }

Menu System
~~~~~~~~~~~

.. code-block:: symbolic

   fn show_menu() {
       running = true;
       
       while running {
           print("\n=== Main Menu ===");
           print("1. View Profile");
           print("2. Edit Settings");
           print("3. View Reports");
           print("4. Exit");
           
           choice = input("Select an option: ");
           
           match choice {
               "1" => view_profile();
               "2" => edit_settings();
               "3" => view_reports();
               "4" => {
                   print("Goodbye!");
                   running = false;
               }
               _ => print("Invalid option. Please try again.");
           }
       }
   }

File Reading with Sentinel Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn read_until_sentinel(filename, sentinel = "END") {
       lines = [];
       line = null;
       
       # Conceptual file reading
       while line != sentinel {
           line = read_next_line();  # Would be file operation
           if line != sentinel {
               lines.append(line);
           }
       }
       
       return lines;
   }

Game Loop
~~~~~~~~~

.. code-block:: symbolic

   fn game_loop() {
       game_running = true;
       player_health = 100;
       enemy_health = 100;
       
       while game_running and player_health > 0 and enemy_health > 0 {
           # Display game state
           print($"Player Health: {player_health} | Enemy Health: {enemy_health}");
           
           # Get player action
           action = input("Attack (a) or Heal (h): ");
           
           # Process round
           if action == "a" {
               damage = random(10, 25);
               enemy_health -= damage;
               print($"You attack for {damage} damage!");
           } else if action == "h" {
               heal = random(15, 30);
               player_health = min(100, player_health + heal);
               print($"You heal for {heal} health!");
           }
           
           # Enemy turn
           if enemy_health > 0 {
               enemy_damage = random(8, 20);
               player_health -= enemy_damage;
               print($"Enemy attacks for {enemy_damage} damage!");
           }
           
           # Check win conditions
           if enemy_health <= 0 {
               print("You win!");
               game_running = false;
           } else if player_health <= 0 {
               print("Game Over!");
               game_running = false;
           }
       }
   }

Best Practices
--------------

Avoid Infinite Loops
~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - has exit condition
   attempts = 0;
   while !success and attempts < max_attempts {
       success = try_operation();
       attempts += 1;
   }
   
   # Dangerous - could run forever
   while true {
       # No break condition inside loop
   }

Use Loop Control Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Clear loop control
   done = false;
   while !done {
       result = process_data();
       if result == "complete" or error_occurred() {
           done = true;
       }
   }

Prefer For Loops for Known Iterations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good for known range - use for loop
   for i in 0..<len(items) {
       process(items[i]);
   }
   
   # Good for unknown iterations - use while
   while has_more_data() {
       data = get_next_chunk();
       process(data);
   }