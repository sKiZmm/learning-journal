# Day 8 – 10-25-2025

## 🕐 10:29 PM - Python
**Platform:** [Code Basics](https://code-basics.com/)

**What I Learned:**
- Ternary operator
- Match Operator
- While Loop
- Data Aggregation (Numbers)
- Data Aggregation (Strings)
- Traversing Strings

**Notes:**
> [First Test:](../CodeBasics%20Tests/ternary_operator.py) `Implement a function flip_flop() that takes a string as input and, if that string is 'flip', returns the string 'flop'. Otherwise, the function should return 'flip'.` Easier than the previous ones.

> [Second Test:](../CodeBasics%20Tests/match.py) `Implement the function get_number_explanation(), which takes a number as input and returns an explanation for that number. If there is no explanation for the number, return just a number. Explanations are available only for the following numbers:`

> [Third Test:](../CodeBasics%20Tests/while.py) `Modify the function print_reversed_numbers() so that it prints the numbers in reverse order. To do this, go from the upper bound to the lower bound. In other words, you should initialize the counter with the maximum value, and in the loop body, you should iterate it backwards down to the lower limit.` Accidentally created an infinite loop lol.

> [Fourth Test:](../CodeBasics%20Tests/aggregation_numbers.py) `Implement a function called multiply_numbers_from_range() that multiplies numbers in a specified range, including range boundaries.` Exact same as the teacher's solution, except the variables of course. Pretty nice!

> [Fifth Test:](../CodeBasics%20Tests/aggregation_strings.py) `Implement a function called join_numbers_from_range() that combines all the numbers from a range into a string` Continuous code with no errors, got it in first try! Quite the achievement, good work me.

> [Sixth Test:](../CodeBasics%20Tests/iteration_over_string.py) `Implement a function called print_reversed_word_by_symbol() that prints a word passed to it character by character, as in the example from the theory, but in reverse order.` Code works, but the test on site is different.

> [Alternative Sixth Test:](../CodeBasics%20Tests/iteration_over_string_alt.py) `Based on the tests, I'm supposed to add spaces to the word, so lets do it!` This took a while but I got it!

---

## 🕐 11:39 PM - Break

---

# 10-26-2025
## 🕐 04:02 AM - Python

**Platform:** [Code Basics](https://code-basics.com/)

**Notes:**
> [Conditions Inside The Body Loop](../CodeBasics%20Tests/conditions_inside_loops.py) `The function from the theory is case-sensitive. I.e., A' anda' are different characters from its point of view. Write a version of this function that isn't case-sensitive.` I though my code wasn't working and was confused, turns out VSCode was bugging.

> [Synctatic Sugar](../CodeBasics%20Tests/synctatic_sugar.py) `Implement a function called filter_string() that takes a string and a character as input, and returns a new string with the character removed from every point in the string. Try not to use the built-in methods for working with the string in your solution.` Made it more complicated, but hey it works!

> [Return from Cycles](../CodeBasics%20Tests/return_from_loops.py) `Implement a function is_contains_char() that checks case-sensitively if a string contains a specified letter.` This was easy hehe

> [Cycle For](../CodeBasics%20Tests/for.py) `In a previous lesson, we already wrote the filter_string() function. Recall that it takes a string and a character as input and returns a new string in which the passed character at all its positions is removed. This time, implement this function using the for loop. An additional condition: the case of the character to be eliminated does not matter.` A little harder but it's all good

> [For loop and range function](../CodeBasics%20Tests/for_in_range.py) `Implement the print_table_of_squares(from, to) function that prints squares of numbers to the screen. It first from and last to a number prints the string square of <number> is <result>` Code works, but tests are different again ugh.

> ```python
> def test():
>     assert fizzbuzz(1) == "1"
>     assert fizzbuzz(3) == "1 2 Fizz"
>     assert fizzbuzz(5) == "1 2 Fizz 4 Buzz"
>     assert fizzbuzz(15) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
> ```

> Code above is the test, I don't even know what the fuck the fizzbuzz function is. Gonna have to rely on ChatGPT for this one, just to find the instructions. `print/return a sequence from 1 to n, replacing multiples of 3 with “Fizz”, multiples of 5 with “Buzz”, and multiples of both 3 and 5 with “FizzBuzz”.` said GPT. [FizzBuzz](../CodeBasics%20Tests/fizz_buzz.py) Had to use GPT again to figure out why my code wasn't passing the test, even though it was right. Turns out I was using print() instead of return smh.

> CodeBasics Python Course Completed! Yippee!

---

## 🕐 5:21 AM - Break

---