# Algorithms

## Following the book "Algorithms"

### Algorithms

Multiplication

Division

Modular Exponentiation

Greatest Common Divisor

Primality Testing

Mergesort

# Python Programming Exercises

## Exercise 1

Question:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float

## Exercise 2

Task 1:

Check whether
x= 2.3
is a zero of the function:
f(x) = x^2+ 0.25x−5
(Evaluate the right-hand side expression and check if the result is near zero.)

Task 2:

Use the command ```range``` and a list comprehension to generate a list with 100
equidistantly spaced values between 0 and 1.

Task 3:

Set up a list ```yplot``` which contains the values ```arctan(x)``` for all the ```x``` in ```xplot```.

Task 4:

This is a 3rd-order Adams-Bashforth method which is used for solving
y′(t) =f(y).
Here we apply it to the function
f(y) =ay. 
When the program is done, the vector u is an approximation to the vector {y(nh)}1000n=0. If you have time over, plot both the approximation 
and the exact solution in the same figure and compare the result.

## Exercise 3

### Kata

The challenge is fairly simple: given a file containing one word per line, print out all the combinations of words that are anagrams; 
each line in the output contains all the words from the input that are anagrams of each other.

## Exercise 4

### Kata

Part One: Weather Data

In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002. 
Download this text file, then write a program to output the day number (column one) 
with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

Part Two: Soccer League Table

The file football.dat contains the results from the English Premier League for 2001/2. 
The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season 
(so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). 
Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.