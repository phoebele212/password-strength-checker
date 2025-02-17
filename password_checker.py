def check_password_strength(password):
    # list to store the not passed checks
    issues = []

    # 1. check if password is long enough
    if (len(password) < 8):
        issues.append("Password is too short! Must be at least 8 characters!")
    
    # 2. check if password has at least one special digit
    if not any(char in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~" for char in password):
        issues.append("Password should contain at least one special character (!@#$%^&*...)!")
   
    # 3. check if password has both upper and lower case letters
    if not any(char.islower() for char in password):
        issues.append("Password should contain at least one lowercase letter.")
    if not any(char.isupper() for char in password):
        issues.append("Password should contain at least one uppercase letter.")
   
    # 4. check if the password contain a number in it 
    if not any(char.isdigit() for char in password):
        issues.append("Password should contain at least a number in it!")

    # print out the messages after the user input
    if issues:
        print("\n".join(issues))
        print("Please try enter with a stronger password!")
        return False
    else:
        print("Password is strong!")
        return True
    
# looping until the user inputs the strong password
while True:
    password = input("Enter a password to check its strength: ")
    if check_password_strength(password):
        break
