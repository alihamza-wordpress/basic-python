Password = "ali-khan121@#"

if len(Password) < 6:
    strength = "weak"
elif len(Password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("Password is: ",strength)