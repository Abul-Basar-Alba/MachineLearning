# Python Tutorial For Beginners (With Notes)

- [ ] **Chapter 0: What is Programming?**

Programming is a way to instruct the computer to perform various tasks using a programming language, just like we use Hindi or English to communicate with each other.

### What is Python?

Python is a simple and easy-to-understand language that feels like reading simple English. Its pseudo-code nature makes it easy to learn and understandable for beginners.

**Features of Python:**

- Easy to understand = Less development time
- Free and open source
- High-level language
- Portable – works on Windows/Linux/Mac
- Fun to work with :)

### Installation

Python can be easily installed from python.org. Download the installer for your platform and follow the setup process.

**Tip:** Install it like a game ☻

## Chapter 1: Modules, Comments & Pip

Let’s write our first Python program.

```python
# hello.py
print("Hello World")  # print is a function (more later)
```

Execute by running `python hello.py` in the terminal to see `Hello World` printed.

### Modules

A module is a file containing code written by someone else (usually) that can be imported and used in our programs.

### Pip

Pip is Python’s package manager. Use it to install modules.

Example: `pip install flask` installs the Flask module.

### Types of Modules

- **Built-in modules**: Pre-installed in Python (e.g., `os`, `abc`)
- **External modules**: Need to install using pip (e.g., `TensorFlow`, `flask`)

### Using Python as a Calculator

Run `python` in the terminal to open the REPL (Read-Eval-Print Loop) and perform calculations.

### Comments

Comments are used to add notes that the programmer does not want to execute, like marking the author’s name or date.

**Types of Comments:**

- Single line: `# This is a comment`
- Multi-line: `''' This is a comment '''` or `""" This is a comment """`

### Chapter 1 – Practice Set

1. Write a program to print the "Twinkle Twinkle Little Star" poem.
2. Use REPL to print the table of 5.
3. Install an external module and use it for an operation of your interest.
4. Write a program to print the contents of a directory using the `os` module.
5. Add comments to the program in problem 4.

```python
# Solution for Practice Set 1.1: Twinkle Twinkle Little Star
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')

# Solution for Practice Set 1.4: Print directory contents with os module
import os
# List all files and directories in the current directory
for item in os.listdir('.'):
    print(item)
```

## Chapter 2: Variables and Data Types

A variable is a name given to a memory location.

Example:

```python
a = 30           # Integer
b = "Harry"      # String
c = 71.22        # Float
```

**Keywords**: Reserved words in Python (e.g., `if`, `else`, `while`).

**Identifiers**: Names for classes, functions, or variables.

### Data Types

- Integers: `71`
- Floating point numbers: `88.44`
- Strings: `"Harry"`
- Booleans: `True`, `False`
- None: `None`

Python automatically identifies data types:

```python
a = 71          # class <int>
b = 88.44       # class <float>
name = "Harry"  # class <str>
```

### Variable Naming Rules

- Can contain alphabets, digits, and underscores.
- Must start with an alphabet or underscore.
- Cannot start with a digit.
- No whitespace allowed.

**Valid variable names**: `Harry`, `harry`, `one8`, `_akki`, `aakash`, `harry_bro`

### Operators in Python

- **Arithmetic**: `+`, `-`, `*`, `/`, etc.
- **Assignment**: `=`, `+=`, `-=`, etc.
- **Comparison**: `==`, `>=`, `<=`, `>`, `<`, `!=`, etc.
- **Logical**: `and`, `or`, `not`

### `type()` Function and Typecasting

```python
a = 31
print(type(a))  # <class 'int'>

b = "31"
print(type(b))  # <class 'str'>

# Typecasting
print(str(31))    # "31"
print(int("32"))  # 32
print(float(32))  # 32.0
```

### `input()` Function

Takes user input as a string:

```python
a = input("Enter name: ")  # If user enters "harry", a = "harry"
```

### Chapter 2 – Practice Set

1. Write a program to add two numbers.
2. Find the remainder when a number is divided by an integer Z.
3. Check the type of a variable assigned using `input()`.
4. Compare if `a` (34) is greater than `b` (80).
5. Calculate the average of two numbers entered by the user.
6. Calculate the square of a number entered by the user.

```python
# Solution for Practice Set 2.1: Add two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)

# Solution for Practice Set 2.5: Average of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Average:", (a + b) / 2)
```

## Chapter 3: Strings

Strings are sequences of characters enclosed in quotes:

```python
a = 'harry'        # Single quotes
b = "harry"        # Double quotes
c = '''harry'''    # Triple quotes
```

### String Slicing

```python
word = "amazing"
print(word[1:6:2])  # 'mzn'
print(word[:7])     # 'amazing'
print(word[0:])     # 'amazing'
```

### String Functions

```python
s = "harry"
print(len(s))            # 5
print(s.endswith("rry")) # True
print(s.count("r"))      # 2
print(s.capitalize())    # Harry
print(s.find("r"))       # 2
print(s.replace("rry", "ppy"))  # happy
```

### Escape Sequence Characters

Examples: `\n` (new line), `\t` (tab), `\'` (single quote), `\\` (backslash).

### Chapter 3 – Practice Set

1. Display a user-entered name followed by "Good Afternoon" using `input()`.
2. Fill a letter template with name and date.
3. Detect double spaces in a string.
4. Replace double spaces with single spaces.
5. Format a letter using escape sequence characters.

```python
# Solution for Practice Set 3.1: Good Afternoon
name = input("Enter your name: ")
print(f"Good Afternoon, {name}")

# Solution for Practice Set 3.2: Letter template
name = input("Enter name: ")
date = input("Enter date: ")
letter = f'''Dear {name},\n\nYou are selected!\n\n{date}'''
print(letter)
```

## Chapter 4: Lists and Tuples

### Lists

Lists store a set of values of any data type:

```python
friends = ['Apple', 'Akash', 'Rohan', 7, False]
```

**List Indexing**:

```python
L1 = [7, 9, 'harry']
print(L1[0])    # 7
print(L1[0:2])  # [7, 9]
```

**List Methods**:

```python
L1 = [1, 8, 7, 2, 21, 15]
L1.sort()       # [1, 2, 7, 8, 15, 21]
L1.reverse()    # [15, 21, 2, 7, 8, 1]
L1.append(8)    # Adds 8 at the end
L1.insert(3, 8) # Adds 8 at index 3
L1.pop(2)       # Removes element at index 2
L1.remove(21)   # Removes 21
```

### Tuples

Tuples are immutable:

```python
a = ()         # Empty tuple
a = (1,)       # Single-element tuple
a = (1, 7, 2)  # Multiple elements
```

**Tuple Methods**:

```python
a = (1, 7, 2)
print(a.count(1))  # 1
print(a.index(1))  # 0
```

### Chapter 4 – Practice Set

1. Store seven fruits in a list entered by the user.
2. Accept marks of 6 students and display them sorted.
3. Verify that a tuple cannot be changed.
4. Sum a list with 4 numbers.
5. Count zeros in the tuple `(7, 0, 8, 0, 0, 9)`.

```python
# Solution for Practice Set 4.1: Seven fruits
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print(fruits)

# Solution for Practice Set 4.4: Sum of list
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(4)]
print("Sum:", sum(numbers))
```

## Chapter 5: Dictionary and Sets

### Dictionary

A collection of key-value pairs:

```python
a = {
    "key": "value",
    "harry": "code",
    "marks": 100,
    "list": [1, 2, 9]
}
print(a["key"])  # value
print(a["list"]) # [1, 2, 9]
```

**Dictionary Methods**:

```python
a = {"name": "Harry", "from": "India", "marks": [92, 98, 96]}
print(a.items())  # List of (key, value) tuples
print(a.keys())   # List of keys
a.update({"friend": "Sam"})  # Updates dictionary
print(a.get("name"))  # Harry
```

### Sets

A collection of non-repetitive elements:

```python
S = set()
S.add(1)
S.add(2)
```

**Set Operations**:

```python
S = {1, 8, 2, 3}
print(len(S))           # 4
S.remove(8)            # Removes 8
print(S.pop())         # Removes and returns an arbitrary element
S.clear()              # Empties the set
print(S.union({8, 11})) # {1, 2, 3, 8, 11}
print(S.intersection({8, 11})) # {8}
```

### Chapter 5 – Practice Set

1. Create a dictionary of Hindi words with English translations and allow lookup.
2. Input eight numbers and display unique numbers.
3. Check if a set can have `18` (int) and `"18"` (str).
4. Find the length of a set after adding `20`, `20.0`, `"20"`.
5. Check the type of `S = {}`.
6. Create a dictionary with 4 friends’ names and favorite languages.
7. Analyze what happens if two friends have the same name or language.
8. Check if a list inside a set can be changed.

```python
# Solution for Practice Set 5.1: Hindi-English dictionary
d = {"salaam": "hello", "pyaar": "love", "dhanyavaad": "thank you"}
word = input("Enter Hindi word: ")
print("Translation:", d.get(word, "Not found"))

# Solution for Practice Set 5.2: Unique numbers
numbers = set()
for i in range(8):
    numbers.add(int(input(f"Enter number {i+1}: ")))
print(numbers)
```

## Chapter 6: Conditional Expressions

Conditional statements execute based on conditions.

**Syntax**:

```python
if condition1:
    print("yes")
elif condition2:
    print("No")
else:
    print("May be")
```

**Example**:

```python
a = 22
if a > 9:
    print("Greater")
else:
    print("lesser")
```

**Relational Operators**: `==`, `>=`, `<=`, `>`, `<`, `!=`

**Logical Operators**: `and`, `or`, `not`

### Chapter 6 – Practice Set

1. Find the greatest of four numbers.
2. Determine if a student passes (40% total, 33% in each subject).
3. Detect spam comments with keywords like “make a lot of money”.
4. Check if a username has less than 10 characters.
5. Check if a name is in a list.
6. Calculate student grade based on marks.
7. Check if a post mentions “Harry”.

```python
# Solution for Practice Set 6.1: Greatest of four numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
print("Greatest:", max(a, b, c, d))

# Solution for Practice Set 6.6: Student grade
marks = float(input("Enter marks: "))
if 90 <= marks <= 100:
    print("Ex")
elif 80 <= marks < 90:
    print("A")
elif 70 <= marks < 80:
    print("B")
elif 60 <= marks < 70:
    print("C")
elif 50 <= marks < 60:
    print("D")
else:
    print("F")
```

## Chapter 7: Loops in Python

### While Loop

```python
i = 0
while i < 5:
    print("Harry")
    i += 1
```

### For Loop

```python
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("Done")
```

### Range Function

```python
for i in range(0, 7):
    print(i)  # Prints 0 to 6
```

### Break and Continue

```python
for i in range(4):
    if i == 2:
        continue  # Skips iteration
    if i == 3:
        break    # Exits loop
    print(i)
```

### Pass Statement

```python
for item in [1, 7, 8]:
    pass  # Do nothing
```

### Chapter 7 – Practice Set

 1. Print a multiplication table using a for loop.
 2. Greet names starting with ‘S’ in a list.
 3. Print a multiplication table using a while loop.
 4. Check if a number is prime.
 5. Sum the first n natural numbers using a while loop.
 6. Calculate factorial using a for loop.
 7. Print star pattern (triangle).
 8. Print star pattern (increasing).
 9. Print star pattern (square).
10. Print multiplication table in reverse.

```python
# Solution for Practice Set 7.1: Multiplication table (for loop)
n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Solution for Practice Set 7.7: Star pattern (triangle)
n = 3
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

## Chapter 8: Functions and Recursion

### Function Syntax

```python
def func1():
    print("Hello")

func1()  # Function call
```

### Functions with Arguments

```python
def greet(name="stranger"):
    return f"Hello {name}"

print(greet("Harry"))  # Hello Harry
print(greet())        # Hello stranger
```

### Recursion

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### Chapter 8 – Practice Set

1. Find the greatest of three numbers using a function.
2. Convert Celsius to Fahrenheit.
3. Prevent `print()` from adding a newline.
4. Calculate the sum of first n natural numbers recursively.
5. Print a star pattern.
6. Convert inches to centimeters.
7. Remove and strip a word from a list.
8. Print a multiplication table.

```python
# Solution for Practice Set 8.1: Greatest of three numbers
def greatest(a, b, c):
    return max(a, b, c)

a, b, c = map(float, input("Enter three numbers: ").split())
print("Greatest:", greatest(a, b, c))

# Solution for Practice Set 8.2: Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Enter temperature in Celsius: "))
print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
```

## Project 1: Snake, Water, Gun Game

```python
import random

def play_game():
    choices = ["snake", "water", "gun"]
    computer = random.choice(choices)
    player = input("Enter snake, water, or gun: ").lower()
    if player not in choices:
        return "Invalid choice!"
    if player == computer:
        return f"Draw! Both chose {player}"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return f"You win! You: {player}, Computer: {computer}"
    else:
        return f"You lose! You: {player}, Computer: {computer}"

print(play_game())
```

## Chapter 9: File I/O

### Opening and Reading Files

```python
with open("this.txt", "r") as f:
    text = f.read()
    print(text)
```

### Writing Files

```python
with open("this.txt", "w") as f:
    f.write("This is nice")
```

### Chapter 9 – Practice Set

 1. Check if “twinkle” is in “poems.txt”.
 2. Update high score in “Hiscore.txt” based on `game()`.
 3. Generate multiplication tables (2 to 20) in separate files.
 4. Replace “Donkey” with “######” in a file.
 5. Replace multiple censored words.
 6. Check if “python” is in a log file.
 7. Find the line number of “python” in a log file.
 8. Copy “this.txt” to another file.
 9. Check if two files are identical.
10. Wipe a file’s contents.
11. Rename a file to “renamed_by_python.txt”.

```python
# Solution for Practice Set 9.1: Check for 'twinkle'
with open("poems.txt", "r") as f:
    if "twinkle" in f.read().lower():
        print("Twinkle is present")
    else:
        print("Twinkle is not present")

# Solution for Practice Set 9.3: Multiplication tables
for i in range(2, 21):
    with open(f"tables/table_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
```

## Chapter 10: Object-Oriented Programming

### Class and Object

```python
class Employee:
    company = "Google"
    def __init__(self, name):
        self.name = name
    def getSalary(self):
        print("Salary is not there")

harry = Employee("Harry")
print(harry.company)  # Google
```

### Static Method

```python
class Employee:
    @staticmethod
    def greet():
        print("Hello user")
```

### Chapter 10 – Practice Set

1. Create a `Programmer` class for Microsoft employees.
2. Create a `Calculator` class for square, cube, and square root.
3. Check if setting `object.a` changes the class attribute.
4. Add a static method to greet in the `Calculator` class.
5. Create a `Train` class with ticket booking and fare methods.
6. Try changing `self` to `slf` or `harry`.

```python
# Solution for Practice Set 10.2: Calculator class
class Calculator:
    def __init__(self, num):
        self.num = num
    def square(self):
        return self.num ** 2
    def cube(self):
        return self.num ** 3
    def square_root(self):
        return self.num ** 0.5
    @staticmethod
    def greet():
        print("Hello")

calc = Calculator(float(input("Enter number: ")))
print("Square:", calc.square())
print("Cube:", calc.cube())
print("Square Root:", calc.square_root())
calc.greet()
```

## Chapter 11: Inheritance & More on OOPs

### Inheritance

```python
class Employee:
    company = "Google"

class Programmer(Employee):
    def code(self):
        print("Coding...")
```

### Super Method

```python
class Programmer(Employee):
    def __init__(self, name):
        super().__init__(name)
```

### Property Decorators

```python
class Employee:
    def __init__(self, ename):
        self.ename = ename
    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self, value):
        self.ename = value
```

### Chapter 11 – Practice Set

1. Create classes for 2D and 3D vectors.
2. Create `Animals`, `Pets`, and `Dog` classes with a `bark` method.
3. Create an `Employee` class with salary and increment properties.
4. Create a `Complex` class with overloaded `+` and `*` operators.
5. Create a `Vector` class with overloaded `+` and `*` operators.
6. Override `__str__()` for a 3D vector.
7. Override `__len__()` for vector dimension.

```python
# Solution for Practice Set 11.1: 2D and 3D vectors
class C2DVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def __str__(self):
        return f"{self.i}i + {self.j}j"

class C3DVector(C2DVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v2 = C2DVector(1, 2)
v3 = C3DVector(1, 2, 3)
print(v2)  # 1i + 2j
print(v3)  # 1i + 2j + 3k
```

## Project 2: Number Guessing Game

```python
import random

def guess_number():
    number = random.randint(1, 100)
    guesses = 0
    while True:
        guess = int(input("Enter your guess: "))
        guesses += 1
        if guess == number:
            print(f"Correct! It took you {guesses} guesses.")
            break
        elif guess > number:
            print("Lower number please")
        else:
            print("Higher number please")

guess_number()
```
