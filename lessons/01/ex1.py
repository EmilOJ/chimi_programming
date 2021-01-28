passwordFile = open("SecretPasswordFile.txt")
secretPassword = passwordFile.read()

print("Enter your password san")
typedPassword = input()

if typedPassword == secretPassword:
    print("Access granted")
    if typedPassword == "12345":
        print("That's a pretty shitty password san.")
else:
    print("Access denied")