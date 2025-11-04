Error Handling
==============

Error handling in Symbolic allows you to gracefully manage runtime errors using the `try` and `catch` keywords. You can catch specific types of exceptions and provide custom handling for each case.

Basic Error Handling
-----------------------

In Symbolic, use the `try` block to wrap potentially error-prone code, followed by a `catch` block to handle errors. You can catch specific error types or use a default handler for unexpected errors.

.. code-block:: symbolic

    try {
        num = Number("abc");
        print(num);
    } catch e {
        ValueError -> print("Invalid number format.");
        default -> print("Error occurred:", e);
    }

In this example, the `try` block attempts to convert the string `"abc"` to a number. Since this is not a valid number format, the `catch` block handles the error by checking for the specific `ValueError` and printing an appropriate message. If an error of a different type occurs, the default handler will be triggered.

Catching Specific Error Types
---------------------------------

You can catch specific error types and handle them accordingly. This helps ensure that only the relevant errors are caught, while others are left to propagate.

.. code-block:: symbolic

    try {
        a = 10 / 0;  # Division by zero
    } catch e {
        ZeroDivisionError -> print("Cannot divide by zero.");
        default -> print("An unexpected error occurred:", e);
    }

In this case, the division by zero will raise a `ZeroDivisionError`, which is specifically caught and handled with a custom message. Any other error will trigger the default handler.

Multiple Catch Blocks
--------------------------

Symbolic supports multiple `catch` blocks, allowing you to handle different error types separately.

.. code-block:: symbolic

    try {
        file = open("non_existent_file.txt");
    } catch e {
        FileNotFoundError -> print("File not found.");
        PermissionError -> print("Permission denied.");
        default -> print("An error occurred:", e);
    }

This example demonstrates how to catch different types of errors, such as `FileNotFoundError` or `PermissionError`, with specific messages for each, while a general `default` block handles any other errors.

Re-Throwing Errors
-----------------------

You can re-throw an error to allow it to propagate after catching it. This can be useful if you want to log or handle an error but still let it propagate.

.. code-block:: symbolic

    try {
        result = someFunction();
    } catch e {
        print("An error occurred:", e);
        throw e;  # Re-throws the caught error
    }

Here, after catching an error, it is logged, and then the `throw` keyword is used to re-throw the error, which allows it to propagate further up the call stack.

Finally Block (Optional)
----------------------------

Symbolic supports the `finally` block, which executes regardless of whether an error was thrown or not. This is useful for cleanup operations.

.. code-block:: symbolic

    try {
        file = open("important_file.txt");
    } catch e {
        print("Error occurred:", e);
    } finally {
        print("Closing file...");
        file.close();
    }

In this example, the `finally` block ensures that the file is always closed, regardless of whether an error occurred during the file operation.

Key Points:
---------------------
- **Error Handling with Try-Catch**: Use `try` and `catch` blocks to manage runtime errors.
- **Specific Error Handling**: Catch specific error types like `ValueError`, `ZeroDivisionError`, etc., to handle different situations.
- **Multiple Catch Blocks**: Use multiple `catch` blocks to handle different types of errors with custom messages.
- **Re-Throwing Errors**: You can re-throw an error after catching it to propagate it further.
- **Finally Block**: The `finally` block always executes, regardless of whether an error occurred or not, making it ideal for cleanup tasks.
