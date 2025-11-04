Classes and Objects
========================

Classes in Symbolic are used to define custom types and encapsulate data and behaviors. Classes support inheritance, initialization, and method definition, providing a powerful way to model real-world entities and behaviors.

Defining a Basic Class
-----------------------------

To define a class in Symbolic, use the `class` keyword followed by the class name. You can define properties and methods for the class. The `__init__` method is used for initialization, allowing you to define how an object of that class should be constructed. Methods are defined as functions within the class, with `self` representing the instance of the class.

Example: Basic Class Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    class Person {
        name = "Anonymous";

        __init__ = (self, name="Anonymous") -> {
            self.name = name;
        }

        greet = (self) -> {
            print("Hello, my name is", self.name);
        }
    }

    p = Person("Alice");
    p.greet();  # Output: Hello, my name is Alice

In this example, a `Person` class is defined with a `name` property and a `greet` method. The `__init__` method initializes the `name` property, with a default value of `"Anonymous"`. An instance of the class is created and the `greet` method is called to print the person's name.

Inheritance and Extending Classes
---------------------------------

Symbolic supports inheritance, allowing a class to extend another class and inherit its properties and methods. The `extends` keyword is used to define a subclass that inherits from a parent class. To call methods from the parent class, use the `super()` function.

Example: Inheritance
^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    class Employee extends (Person) {
        salary = 0;

        __init__ = (self, name="Anonymous", salary=0) -> {
            super().__init__(name);  # Call the parent class's __init__
            self.salary = salary;
        }

        setSalary = (self, amount) -> {
            self.salary = amount;
        }

        displayInfo = (self) -> {
            print(self.name, "has a salary of", self.salary);
        }
    }

    emp = Employee("Bob", 50000);
    emp.displayInfo();  # Output: Bob has a salary of 50000

In this example, the `Employee` class extends `Person`, adding a new `salary` property. The `__init__` method calls the parent class's `__init__` method using `super()`, and initializes the `salary` property. The `displayInfo` method prints the employee's name and salary.

Method Overriding
----------------------

You can override methods from the parent class to change or extend their behavior. The overridden method should have the same signature as the method in the parent class.

Example: Method Overriding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    class Manager extends (Employee) {
        __init__ = (self, name="Anonymous", salary=0, department="General") -> {
            super().__init__(name, salary);  # Initialize parent class
            self.department = department;
        }

        displayInfo = (self) -> {
            print(self.name, "manages the", self.department, "department with a salary of", self.salary);
        }
    }

    mgr = Manager("Eve", 70000, "HR");
    mgr.displayInfo();  # Output: Eve manages the HR department with a salary of 70000

In this example, the `Manager` class extends `Employee`, overriding the `displayInfo` method to include the department information.

Static Methods
------------------

Static methods belong to the class itself rather than an instance of the class. They are useful for utility functions that don't rely on instance-specific data. Static methods are defined using the `static` keyword and can be called without creating an instance of the class.

Example: Static Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: symbolic

    class MathHelper {
        __init__ = (self) -> {}

        static add = (a, b) -> a + b;

        static multiply = (a, b) -> a * b;
    }

    sum_result = MathHelper.add(5, 3);  # Output: 8
    product_result = MathHelper.multiply(4, 6);  # Output: 24

In this example, the `MathHelper` class defines two static methods: `add` and `multiply`. These methods can be called directly on the class without creating an instance.

Summary
-------

Symbolic's class system provides the following features:

1. **Basic Class Definition**: Define classes with properties and methods, and use `__init__` for initialization.
2. **Inheritance**: Extend classes using `extends` and inherit methods and properties from the parent class.
3. **Method Overriding**: Override parent class methods to customize behavior.
4. **Static Methods**: Define utility functions that can be called directly on the class, without an instance.
5. **Accessing Parent Methods**: Use `super()` to call parent class methods.

These features allow for flexible and powerful object-oriented programming in Symbolic.
