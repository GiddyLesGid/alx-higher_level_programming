
Aysuarex
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x12-javascript-warm_up/
Latest commit
@Aysuarex
Aysuarex
…
on Sep 6, 2022
Git stats
Files
Type
Name
Commit time
. .
0-javascript_is_amazing.js
7 months ago
0-javascript_is_amazing.js
1-multi_languages.js
7 months ago
1-multi_languages.js
10-factorial.js
7 months ago
10-factorial.js
100-let_me_const.js
7 months ago
100-let_me_const.js
101-call_me_moby.js
7 months ago
101-call_me_moby.js
102-add_me_maybe.js
7 months ago
102-add_me_maybe.js
103-object_fct.js
7 months ago
103-object_fct.js
11-second_biggest.js
7 months ago
11-second_biggest.js
12-object.js
7 months ago
12-object.js
13-add.js
7 months ago
13-add.js
2-arguments.js
7 months ago
2-arguments.js
3-value_argument.js
7 months ago
3-value_argument.js
4-concat.js
7 months ago
4-concat.js
5-to_integer.js
7 months ago
5-to_integer.js
6-multi_languages_loop.js
7 months ago
6-multi_languages_loop.js
7-multi_c.js
7 months ago
7-multi_c.js
8-square.js
7 months ago
8-square.js
9-add.js
7 months ago
9-add.js
README.md
7 months ago
README.md
README.md
Javascript - Warm up
This was the first JavaScript project I completed at ALX. Tasks involved writing various introductory-level JavaScript scripts on Node.js.

Tests ✔️
tests: Folder of test files. Provided by ALX.
Function Prototypes 💾
Prototypes for functions written in this project:

File	Prototype
13-add.js	exports.add = (a, b)
101-call_me_moby.js	function (x, theFunction)
102-add_me_maybe.js	function (number, theFunction)
Tasks 📃
0. First constant, first print

0-javascript_is_amazing.js: JavaScript script that creates a constant variable myVar with the value 'Javascript is amazing'.
Usage: ./0-javascript_is_amazing.js
1. 3 languages

1-multi_languages.js: JavaScript script that prints three lines.
Usage: ./1-multi_languages.js
Line 1: 'C is fun'.
Line 2: 'Python is cool'.
Line 3: 'Javascript is amazing'.
2. Arguments

2-arguments.js: JavaScript script that prints a message depending on the number of arguments passed.
Usage: ./2-arguments.js <arg 1> <arg 2> ...
If no arguments are passed, prints 'No argument'.
If one argument is passed, prints 'Argument found'.
Otherwise, prints 'Arguments found'.
3. Value of my argument

3-value_argument.js: JavaScript script that prints the first argument passed to it.
Usage: ./3-value_argument.js <arg>
If no argument is passed, prints 'No argument'.
4. Create a sentence

4-concat.js: JavaScript script that prints two arguments passed in the format <arg 1> is <arg 2>.
Usage: ./4-concat.js <arg1> <arg2>
5. An Integer

5-to_integer.js: JavaScript script that prints My number: <first argument converted in integer> if the first pased argument can be converted to an integer.
Usage: ./5-to_integer.js
If the argument cannot be converted to an integer, prints 'Not a number'.
6. Loop to languages

6-multi_languages_loop.js: JavaScript script that prints three lines using an array and a loop.
Usage: ./6-multi_languages_loop.js
First line: 'C is fun'.
Second line: 'Python is cool'.
Third line: 'Javascript is awesome'.
7. I love C

7-multi_c.js: JavaScript script that prints x times 'C is fun'.
Usage: ./7-multi_c.js <x>
If the first argument cannot be converted to a number, prints 'Missing number of occurrences'.
8. Square

8-square.js: JavaScript script that prints a square.
Usage: ./8-square.js <size>
If the first argument cannot be converted to a number, prints 'Missing size'.
Uses the X character to print the square.
9. Add

9-add.js: JavaScript script that prints the addition of two numbers passed as arguments.
Usage: ./9-add.js <number 1> <number 2>
Prototype: function add(a, b)
10. Factorial

10-factorial.js: JavaScript script that computes and prints a factorial.
Usage: ./10-factorial.js <number to compute factorial of>
11. Second biggest!

11-second_biggest.js: JavaScript script that locates the second largest number in the list of provided arguments.
Usage: ./11-second_biggest.js <arg 1> <arg 2> ...
If no arguments are passed or the number of arguments is 1, prints 0.
12. Object

12-object.js: Update of the following script that replaces the value 12 with 89.
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
13. Add file

13-add.js: JavaScript function add that returns the addition of two numbers.
14. Const or not const

100-let_me_const.js: JavaScript script that modifies the value of myVar in the following file to 333.
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
15. Call me Moby

101-call_me_moby.js: JavaScript function that executes x times a given function.
16. Add me maybe

102-add_me_maybe.js: JavaScript function that increments a given number and calls a given function.
17. Increment object

103-object_fct.js: Update of the following JavaScript script adding a new function incr that increments the number value.
#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
