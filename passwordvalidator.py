#The password is valid if all criteria are met:
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

def checker_password(password):
      
    SpecialSymbols =['!', '@', '#', '$', '%', '^','&','*','(',')', '_', '+', '-', '/' ]
    val = True
      
    if len(password) < 15:
        print('The password length should be at least 15')
        val = False
    elif not any(type for type in password):
        print('Password should have at least one capital letter. Please Try Again')
        val = False
    elif not any(type.isdigit() for type in password):
        print('Password should have at least one number. Please Try Again')
        val = False  
    elif not any(type in SpecialSymbols for type in password):
        print('Password should have at least one special characters !@#$%^&*()_+-. Please Try Again. ')
        val = False
    else:
        return val

def enter_passwd():
    print("WELCOME TO CARLITO'S PASSWORD CHECKER!")
    password = input('\nEnter your desired password: ')
    if (checker_password(password)):
        print("\nCongratulations! Your Password is Valid!")
    else:
        print("\nI'm sorry to say that your password is Invalid!")        
enter_passwd()