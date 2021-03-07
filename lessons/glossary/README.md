# Min Glossary


**assignment** A statement that assigns a value to a variable. 

```python
a = 2
```

**boolean expression** An expression whose value is either True or False.

```python
# This is a boolean expression
24 - 3 >= 1 

# This is another boolean expression
name == "Tarako san"
```

**branch** One of the alternative sequences of statements in a conditional statement.

```python
if guess == 1:
    # This is one branch
    print("1")
elif guess == 2:
    # This is another branch
    print("2"):
else:
    # This is a third branch
    print("3?")
```

**comparison operator** One of the operators that compares its operands: `==`, `!=`, `>`, `<`, `>=`, and `<=`.

**concatenate** To join two operands end to end. 

```python
# concatenating 3 strings:
"min" + " " + "san"
```

**condition** The boolean expression in a conditional statement that determines which branch is executed.

```python
# 'guess == 1' and 'guess == 2' are conditions
if guess == 1:
    print("1")
elif guess == 2:
    print("2"):
else:
    print("3?")
```

**conditional statement** A statement that controls the flow of execution depending on some condition. (e.g. `if`, `elif`, `else`)

**comment** Information in a program that is meant for other programmers (or anyone reading the code) and has no effect on the execution of the program. 

```python
# I'm a comment (I get ignored by the program)
a = "I'm a string. I get run by the program" 
```

**evaluate** To simplify an expression by performing the operations in order to yield a single value. 

```python
# When an assignment is run, first the right-hand side is evaluated. So,
a = 1 + 2

# becomes
a = 3

# and then the computer performs the assignment.
```

**expression** A combination of variables, operators, and values that represents a single result value. 

```python
apples = 2
pears = 6

fruits = apples + pears #The right side "apples + pears" is an expression and it evaluates to 8
```

**floating point** (`float`) A type that represents numbers with fractional parts (e.g. `3.1415`). 


**integer** A type that represents whole numbers. (`-2, -1, 0, 1, 2, 3, 4` etc.) 

**keyword** A reserved word that is used by the compiler to parse a program; you cannot use keywords like `if`, `def`, and `while` as variable names. 

**logical operator** One of the operators that combines boolean expressions: `and`, `or`, and `not`.

**nested conditional** A conditional statement that appears in one of the branches of another conditional statement.

```python
if weather == "sunny":
    # this is a nested conditional
    if temperature > 20:
        print("it's summer")
    else:
        print("it's spring")
else:
    # this is also a nested conditional 
    if temperature > 20:
        print("it's autumn")
    else:
        print("it's winter")
```

**operand** One of the values on which an operator operates.

```python
# Here 1 and 2 are the operands
1 + 2
```

**operator** A special symbol that represents a simple computation like addition, multiplication, or string concatenation (like `*`, `+`, `-` etc.). 

**statement** A section of code that represents a command or action. 

```python
# This is an if-statement
if a == 3:

# This is a variable assignment statement
a = 3

# This is a print statement
print("hej :D")
```

**string** A type that represents sequences of characters. (E.g. `"aaaaaahhh min san"`j)

**traceback** A list of the functions that are executing, printed when an exception occurs.

```bash
# When you run your program and get an error like this:
File "/Users/emiljohansen/Downloads/HM4.1.py", line 17
    else abs(guess - secretNumber) == 1:
         ^
SyntaxError: invalid syntax


# This part is the traceback (it shows what was run)
File "/Users/emiljohansen/Downloads/HM4.1.py", line 17
```

**type** A category of values. The types we have seen so far are integers (type `int`), floating-point numbers (type `float`), booleans (type `bool`) and strings (type `str`). 

**value** One of the basic units of data, like a number or string, that a program manipulates. 

```python
# This is a value, and it's of type int
1

# This is a value, and it's of type str
"hej"

# This is a value, and it's of type bool
True

# The value of the variable `a` is False, and it's of type bool
a = False
```

**variable** A name that refers to a value. 

```python
# `a` is a variable, and it has value 2
a = 2

# now it has value 3
a = 3

# now it has value 6
a = a + a
```
