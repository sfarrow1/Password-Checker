import re
            
def check_password_strength(password):
    if len(password) < 12:
        return "Weak: Password must be 12 characters long."
    
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain atleast 1 uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain atleast 1 lowercase letter"
    
    if not re.search(r'[0-9]', password):
        return "Weak: Password must contain atleast 1 number"
    
    if not re.search(r'[!@#$%^&*()_,.?":{}<> ]', password):
        return "Weak: Password must contain atleast 1 special character"
    
    return "Strong: Password is strong!"

while True:
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
    if result == "Strong: Your password is strong!":
        break