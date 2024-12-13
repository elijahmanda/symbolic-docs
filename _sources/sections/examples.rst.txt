Examples
==========

Fibonacci Sequence
---------------------------
A recursive function to calculate Fibonacci numbers.

.. code-block:: symbolic

    fibonacci = (n) -> n <= 1 ? n : fibonacci(n-1) + fibonacci(n-2);
    print("Fibonacci of 10 =", fibonacci(10));

Hexadecimal Conversion
--------------------------------
Converts an integer to its hexadecimal representation.

.. code-block:: symbolic

    toHex = (num) -> {
        digits = "0123456789ABCDEF";
        if num < 16 {
            return digits[num];
        }
        return toHex(num // 16) + digits[num % 16];
    };
    print("Hex of 255 =", toHex(255));

Prime Number Checker
-----------------------------------
Checks whether a number is prime.

.. code-block:: symbolic

    isPrime = (n) -> {
        if n <= 1 { return false; }
        loop i from 2 to n-1 {
            if n % i == 0 { return false; }
        }
        return true;
    };
    print("Is 17 prime?", isPrime(17));
    print("Is 20 prime?", isPrime(20));

Factorial Function
-----------------------
Calculates the factorial of a number using recursion.

.. code-block:: symbolic

    factorial = (n) -> n <= 1 ? 1 : n * factorial(n - 1);
    print("Factorial of 5 =", factorial(5));

Palindrome Checker
-----------------------
Checks if a string is a palindrome.

.. code-block:: symbolic

    isPalindrome = (s) -> s == s.reverse();
    print("Is 'madam' a palindrome?", isPalindrome("madam"));
    print("Is 'hello' a palindrome?", isPalindrome("hello"));

GCD (Greatest Common Divisor)
----------------------------------------
Finds the greatest common divisor of two numbers.

.. code-block:: symbolic

    gcd = (a, b) -> {
        while b != 0 {
            temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };
    print("GCD of 56 and 98 =", gcd(56, 98));

Sum of Digits
-----------------------
Calculates the sum of digits of a number.

.. code-block:: symbolic

    sumOfDigits = (n) -> n < 10 ? n : n % 10 + sumOfDigits(n // 10);
    print("Sum of digits of 1234 =", sumOfDigits(1234));

Counting Vowels in a String
------------------------------------
Counts the number of vowels in a string.

.. code-block:: symbolic

    countVowels = (s) -> {
        vowels = "aeiouAEIOU";
        letters = s.split();
        return letters.filter((chr) -> chr in vowels, inplace=true).length;
    };
    print("Number of vowels in 'Hello World' =", countVowels("Hello World"));

Fibonacci Sequence Generator (Iterative)
----------------------------------------------
An iterative version of the Fibonacci sequence generator.

.. code-block:: symbolic

    fibonacciIterative = (n) -> {
        a = 0;
        b = 1;
         loop i from 0 to n-1 {
            temp = a;
            a = b;
            b = temp + b;
        }
        return a;
    };
    print("Fibonacci of 10 (iterative) =", fibonacciIterative(10));

Anagram Checker
-----------------------------
Checks if two strings are anagrams of each other.

.. code-block:: symbolic

    areAnagrams = (s1, s2) -> s1.sort() == s2.sort();
    print("Are 'listen' and 'silent' anagrams?", areAnagrams("listen", "silent"));

Reverse String
-----------------------------
Reverses a string.

.. code-block:: symbolic

    reverseString = (s) -> {
        result = "";
        loop i from s.length-1 to 0, -1 {
            result = result + s[i];
        }
        return result;
    };
    print("Reversed 'Hello' =", reverseString("Hello"));

Character Frequency in a String
--------------------------------------
Counts the frequency of each character in a string.

.. code-block:: symbolic

    charFrequency = (s) -> {
        freq = {};
        loop c from s {
            if c in freq { freq[c] += 1; } 
            else { freq[c] = 1; }
        }
        return freq;
    };
    print("Character frequencies in 'hello' =", charFrequency("hello"));

Merge Sort Algorithm
------------------------------
An implementation of the merge sort algorithm.

.. code-block:: symbolic

    mergeSort = (arr) -> {
        if arr.length <= 1 { return arr; }
        mid = arr.length // 2;
        left = mergeSort(arr[0..mid]);
        right = mergeSort(arr[mid..-1]);
        return merge(left, right);
    };

    merge = (left, right) -> {
        result = [];
        while left.length > 0 and right.length > 0 {
            if left[0] < right[0] {
                result = result + left[0];
                left = left[1..-1];
            } else {
                result = result + right[0];
                right = right[1..-1];
            }
        }
        return result + left + right;
    };

    print("Sorted array =", mergeSort([38, 27, 43, 3, 9, 82, 10]));

Reverse Words in a Sentence
-----------------------------------
Reverses the words in a sentence while maintaining the order of the characters in each word.

.. code-block:: symbolic

    reverseWords = (s) -> {
        words = s.split();
        return words.reverse().join(" ");
    };
    print("Reversed words in 'Hello World' =", reverseWords("Hello World"));

Matrix Multiplication
-----------------------------
Multiplies two matrices.

.. code-block:: symbolic

    matrixMultiply = (a, b) -> {
        result = [];
        loop i from 0 to length(a)-1 {
            row = [];
            loop j from 0 to length(b[0])-1 {
                sum = 0;
                loop k from 0 to length(b)-1 {
                    sum += a[i][k] * b[k][j];
                }
                row = row + sum;
            }
            result = result + row;
        }
        return result;
    };

    A = [[1, 2], [3, 4]];
    B = [[5, 6], [7, 8]];
    print("Matrix multiplication result =", matrixMultiply(A, B));

Custom List Operations
-----------------------------
Implements basic list operations such as adding and removing items.

.. code-block:: symbolic

    class CustomList {

        __init__ = (self) -> {
            self.items = [];
        };

        add = (self, item) -> {
            self.items.append(item);
        };

        remove = (self, item) -> {
            self.items.filter((x) -> x != item);
        };

        printItems = (self) -> {
            print(self.items);
        };
    };

    myList = CustomList();
    myList.add(1);
    myList.add(2);
    myList.add(3);
    myList.printItems();
    myList.remove(2);
    myList.printItems();

Convert Decimal to Binary
-------------------------------------
Converts a decimal number to its binary representation.

.. code-block:: symbolic

    toBinary = (num) -> {
        if num == 0 { return "0"; }
        binary = "";
        while num > 0 {
            binary = (num % 2) + binary;
            num = num // 2;
        }
        return binary;
    };
    print("Binary of 15 =", toBinary(15));

Check Armstrong Number
---------------------------------
Checks whether a number is an Armstrong number (a number equal to the sum of its digits raised to the power of the number of digits).

.. code-block:: symbolic

    isArmstrong = (n) -> {
        digits = toString(n).split();
        power = digits.length;
        sum = 0;
        loop d from digits {
            sum += Int(d) ** power;
        }
        return sum == n;
    };
    print("Is 153 an Armstrong number?", isArmstrong(153));


