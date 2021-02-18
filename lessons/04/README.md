#  Flow Control 2

## Repeating stuff

Homework from last time
```python
print("What your name? ")
user_name = input()
if user_name == "Tarako san":
    print("Welcome back, Tarako san")    
else:
    print("Access Denied")
```

What if we want the program to keep asking, until the user gets it right?
Something like:

```
> What's your name?
Min

> Try again
Ahhhh

> Try again
Tarako san

> Welcome back, Tarako san
```


## Repeating more stuff

![](img/countdown.gif)
The code could look like this 

```python
import time

print("10")
time.sleep(1)

print("9")
time.sleep(1)

print("8")
time.sleep(1)

print("7")
time.sleep(1)

print("6")
time.sleep(1)

print("5")
time.sleep(1)

print("4")
time.sleep(1)

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("1")
time.sleep(1)

print("00")
```

