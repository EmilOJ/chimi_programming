#  Python basics

## Variables

### Introduction
```python
>>> strength = 2
>>> name = "ぴょき"

>>> strength
>>> name
```

### Exercise 0.1 
Where is the information stored? (Try closing the terminal and reopening it)

```python
>>> strength = 2
>>> strength
>>> strength = 10 # LEVEL UP!!!!
>>> strength
>>> strength = strenght + 2 # LEVEL UP MOOOORE!!!
>>> strength
```

### Using variables
```python
>>> minsan_age = 32
>>> minchan_age = 31

>>> mins_age = minsan_age + minchan_age
>>> mins_age
```

```
>>> space = " "
>>> a_letter = "a"
>>> san = "san"
```

### Exercise 0.2

How can we get `"aaaaaaaaaa san"` (10 a's)? (*tip: remember what happens if you add 
strings?*)


## Intermezzo: Write and run code in an editor

- Install [VS Code](https://code.visualstudio.com/download)

Try running the following program

```python
name = "min san"
age = 32

# First this
print("Your name is " + name )

# Then this
print("And your age is " + age)
```

Use `str()` to convert the `int` to a `str`

```python
print("And your age is " + str(age))
```

## Variables (cont.)
### Exercise 0.3

```python
first_word = "san"
second_word = "min"
```

How can we switch the values so the below code prints "`Min san`"?

```python
print(first_word + " " + second_word)
```

[Check Sheets](https://docs.google.com/spreadsheets/)

### Variable names

```python
min = "Chimi"
MIN = "Emil"

# What do you think will be printed?
print(min)
print(MIN)
```

**Convention in python**

Convention in programming means *"we all agreed to do it like this, so please do like this"*
1. Use snake-case 
2. For constant values, use upper-case (`MIN_SAN`)

something-case???

1. `minSan` 
2. `min-san`
3. `MinSan` 
4. `min_san`
5. `MIN-SAN`

Which one is
- 🐍 Snake case 
- 🐫 Camel case 
- 🚆 Train case
- 🍢 Kebab case 
- 🐫⬆️ Upper camel case
### Exercise 0.4

```python
# which is better?
min_age = 32
MIN_AGE = 32

# which is better?
min_girlfriend = "chimi-chan"
MIN_GIRLFRIEND = "chimi-chan"
```
```python
# Does this work?
min1 = 1
min2 = 2 
```


### The `input()` function

```python
min_name = input()
print(min_name)
```

Let's add a prompt

```python
print("What's your name?") 
min_name = input()
print(f"Your name is " + min_name) 






# Note
# The above is the same as
print(f"Your name is {min_name}") 
```

### Exercise 0.5
```python
# What does this program print?
num1 = input() # 3
num2 = input() # 2
print(num1 + num2)
```

We can convert a `string` to an `int` with `int()`

```python
num1 = int(input()) # 3
num2 = int(input()) # 2
print(num1 + num2)
```

or

```python
num1 = input() # 3
num2 = input() # 2
print(int(num1) + int(num2))
```

# Homework

## HW1

Which of the following is a variable, and which is a string?

```python
"min"
min
```

## HW2

Name three data types

## HW3

What does the variable `min_age` contain after the following code runs?

```python
min_age = 32
min_age + 1
```

## HW4

What is printed in the following program?

```python
print('spam' + 'spamspam')
print('spam' * 3)
```

## HW5

Why does this program cause an error? How can you fix it?

```python
kani_san_eaten = 99 # Don't change this

# Fix this ↓
print('I have eaten ' + kani_san_eaten + ' kani-san.')
```

## HW6

Search online and find out how you can find the lenght of a string.
For example the string `"min-san"` has the length 7, because it has 7 characters

```python
min_string = "min-san"

# What you need to write on the rigth side below? (Writing `7` is not correct!)
min_string_lenght = ???

print(min_string_length)
```

## HW7

Write a program that asks for the user's age (e.g. `32`), and says `"You'll be 33 next year`.


