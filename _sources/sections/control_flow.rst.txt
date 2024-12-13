Control Flow
===============

Control flow structures in Symbolic allow you to control the execution path based on conditions and loops. The available control flow structures include conditionals (`if`, `else`, `else if`, `match`) and loops, which enable you to execute code selectively or repetitively.

Conditionals
---------------

The following conditional structures are available in Symbolic:

- **`if`**: Executes code if a specified condition is true.
- **`else if`**: Specifies additional conditions if the previous `if` or `else if` conditions were false.
- **`else`**: Provides a fallback when none of the previous conditions are true.
- **`match`**: Provides a more flexible form of conditional branching, suitable for pattern matching.

`if`-`else` Statements
------------------------

The `if` and `else` statements allow you to execute different blocks of code depending on the evaluation of conditions.

Example:
    
.. code-block:: symbolic

    temperature = 25;

    if temperature < 0 {
        print("It's freezing cold.");
    } else if temperature < 20 {
        print("It's a bit chilly.");
    } else if temperature < 30 {
        print("The weather is pleasant.");
    } else {
        print("It's quite hot.");
    }

In this example, the program checks the value of `temperature` and executes the corresponding block based on its value. The conditions are evaluated from top to bottom, and the first one that evaluates as `true` is executed. If no condition matches, the code in the `else` block is executed.

`match`-`case` Statements
------------------------------

`match` and `case` allow for more advanced pattern matching, making it easy to handle multiple conditions based on different values.

Example:
^^^^^^^^^^^^^^^
.. code-block:: symbolic

    score = 80;

    match score {
        case < 50 -> print("Fail");
        case 50..75 -> print("Pass");
        case > 75 -> print("Distinction");
        default -> print("Invalid score");
    }

In this example, the `score` variable is evaluated against various patterns:
- If the score is less than 50, the message `"Fail"` is printed.
- If the score is between 50 and 75 (inclusive), the message `"Pass"` is printed.
- If the score is greater than 75, the message `"Distinction"` is printed.
- The `default` case is a fallback if no other pattern matches, ensuring that a valid message is always printed.

Loops
---------

Symbolic provides flexible looping mechanisms with `loop` and `while` constructs. These constructs allow for intuitive iteration over ranges, collections, or conditions, and support advanced flow control with `stop` and `skip`.

Loop
^^^^^^^^^
The `loop` construct is highly versatile, offering range-based iteration, custom initialization, and step increments. It can also iterate over collections or run infinitely until explicitly stopped.

Syntax
^^^^^^^^^^

1. **Range-Based Loop**  
   Iterates over a specified range with optional increments.  

   .. code-block:: symbolic

       loop i from <start> to <end> {
           # Code block
       }

2. **Custom Initialization and Increment**  
   Allows manual control over initialization, condition, and increment.  

   .. code-block:: symbolic

       loop <initialization>, <condition>, <increment> {
           # Code block
       }

3. **Infinite Loop**  
   Runs indefinitely until a `stop` is encountered.  

   .. code-block:: symbolic

       loop <initialization>, <increment> {
           # Code block
           if <condition> { stop; }
       }
       
       loop {
           # Code block
       }

4. **Iterating Collections**  
   Supports iterating over collections or ranges.  

   .. code-block:: symbolic

       loop [variable] from <collection> {
           # Code block
       }

Examples
^^^^^^^^^^^^^^

.. code-block:: symbolic

    # Loop from 1 to 10
    loop i from 1 to 10 {
        print("i =", i);
    }

    # Custom initialization, condition, and increment
    loop i = 0, i < 20, 2 {
        print("Even number:", i);
    }

    # Infinite loop with a break condition
    loop i = 0, 2 {
        print(i); # Inline comment
        if i == 6 { stop; }
    }

    # Iterating over a collection
    points = 1 to 5;
    loop [x] from points {
        print("Point:", x);
    }

While Loop
--------------
The `while` construct continues to execute a block as long as a given condition evaluates to `true`. This is useful for scenarios where the number of iterations is not predetermined.

Syntax
^^^^^^^^^^^

.. code-block:: symbolic

    while <condition> {
        # Code block
    }

Examples
^^^^^^^^^^^^^^

.. code-block:: symbolic

    count = 0;
    while count < 5 {
        print("Count =", count);
        count += 1;
    }

Control Flow
------------------
Symbolic provides built-in flow control mechanisms to manage loop execution:

- **`stop`**: Exits the loop prematurely.
- **`skip`**: Skips the current iteration and moves to the next.

Examples
^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    # Using stop
    loop i = 0, 1 {
        if i > 5 { stop; }
        print("i =", i);
    }

    # Using skip to ignore even numbers
    loop i = 0, i < 10, 1 {
        if i % 2 == 0 { skip; }
        print("Odd number:", i);
    }

Advanced Usage
^^^^^^^^^^^^^^^^^^^^^^
Symbolic's loops can handle a variety of complex scenarios, including dynamically defined ranges, infinite loops, and nested loops.

.. code-block:: symbolic

    # Dynamic range
    a = 3;
    b = 9;
    loop i from a to b {
        print("i =", i);
    }

    # Nested loops
    loop i from 1 to 3 {
        loop j from 1 to 3 {
            print("i =", i, ", j =", j);
        }
    }

    # Infinite loop with stop condition
    loop {
        print("Running...");
        if condition { stop; }
    }


Conditional Trigger and Action
----------------------------------

Symbolic supports the `whenever` construct, enabling actions to be triggered automatically when specified conditions are met. This feature is useful for monitoring and reacting to dynamic changes in state or values.

Syntax
^^^^^^^^^^^

.. code-block:: symbolic

    whenever <condition>; with id <identifier> {
        # Action block
    }

Key Features
^^^^^^^^^^^^^^^^^^^^

- **Dynamic Condition Monitoring**: Continuously evaluates the condition and executes the action block whenever it becomes `true`.
- **Unique Identifiers**: Use `id` to identify and manage specific triggers.
- **Termination**: Use `terminate <id>` to stop monitoring a trigger condition.

Example: Temperature Alert System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    temperature = 25;

    # Define a conditional trigger
    whenever temperature > 30; with id temp_check {
        alert("Temperature is too high!");

        # Terminate the trigger if a specific condition is met
        if switch.disabled() {
            terminate temp_check;
        }
    }

    # Modify the temperature to trigger the condition
    temperature += 35; # This will trigger the action since `temperature > 30`

Explanation
^^^^^^^^^^^^^^^

1. **Trigger Condition**: The `whenever` statement continuously monitors `temperature > 30`.
2. **Action Block**: Executes the defined actions (`alert` and conditional `terminate`) when the condition becomes `true`.
3. **Dynamic Updates**: Changes in the `temperature` value can dynamically activate the trigger.

Advanced Example: Multi-Condition Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    system_load = 50;
    disk_space = 80;

    whenever system_load > 75; with id load_check {
        alert("System load is critical!");
        if disk_space < 20 {
            terminate load_check;
            alert("System shutting down due to low disk space!");
        }
    }

    system_load += 30; # Triggers `load_check` when `system_load > 75`
    disk_space -= 70;  # Additional condition can further refine the trigger logic

Time Delay
---------------

Symbolic provides the `wait` command to introduce pauses or delays in program execution. The delay can be specified in various time units, allowing for precise control over timing.

Syntax
^^^^^^^^^^^^

.. code-block:: symbolic

    wait <time>[<unit>];

- `<time>`: A numerical value representing the duration.
- `<unit>`: Specifies the time unit. If omitted, seconds are assumed by default.

Supported Units
^^^^^^^^^^^^^^^^^^^^

- **Milliseconds**: `ms`
- **Seconds**: `s` or omit the unit
- **Minutes**: `min`
- **Hours**: `hr`
- **Days**: `days`
- **Weeks**: `wk`
- **Months**: `mo`
- **Years**: `years`

Examples
^^^^^^^^^^^^^

.. code-block:: symbolic

    # Wait for 10 milliseconds
    wait 10ms;

    # Wait for 5 seconds
    wait 5;

    # Alternative ways to specify seconds
    wait 6 seconds;

    # Wait for 10 minutes
    wait 10min;

    # Wait for 1 hour
    wait 1hr;

    # Wait for half a day
    wait 0.5 days;

    # Wait for 2 weeks
    wait 2wk;

    # Wait for 3 months
    wait 3mo;

    # Wait for 1 year
    wait 1year;


Advanced Example: Timed Execution with Wait
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    print("Starting process...");
    wait 2 seconds;
    print("Step 1 completed.");
    wait 5min;
    print("Process completed after a delay.");


Summary of Control Flow Statements
-------------------------------------------

- **`if`**: Executes a block of code if a condition is true.
- **`else if`**: Specifies additional conditions if the preceding conditions are false.
- **`else`**: Executes a block of code when no previous conditions are true.
- **`match`**: Provides a powerful way to match values to patterns and handle multiple conditions in a cleaner way.

