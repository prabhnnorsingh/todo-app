# Code to find if a password is strong or not.

password = input("Enter your password:-")
result = []
if len(password) > 8:
    result.append(True)
else:
    result.append(False)

digit =False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)


uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)


if all(result) == True:
    print("Strong Password")
else:
    print('Weak Password')