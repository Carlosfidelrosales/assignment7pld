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
        print('\033[31mThe password length should be at least \033[1m15 characters\033[0m\033[31m. \033[36mPlease Try Again.\033[0m')
        val = False
    elif not any(type for type in password):
        print('\033[31mPassword should have at least \033[1mone capital letter\033[0m\033[0m. \033[36mPlease Try Again\033[0m')
        val = False
    elif not any(type.isdigit() for type in password):
        print('\033[31mPassword should have at \033[1mleast one number\033[0m\033[0m. \033[36mPlease Try Again\033[0m')
        val = False  
    elif not any(type in SpecialSymbols for type in password):
        print('\033[31mPassword should have at least \033[1mone of the special characters!@#$%^&*()_+-\033[0m \033[4m\033[0m\033[0m. \033[36mPlease Try Again.\033[0m')
        val = False
    else:
        return val

def enter_passwd():
    print("\033[33mWELCOME TO \033[1mCARLITO'S PASSWORD CHECKER!\033[33m\033[0m")
    password = input('\nEnter your \033[4mdesired password\033[0m: ')
    if (checker_password(password)):
        print("\n\033[92mCongratulations! Your Password is \033[1m\033[4mValid\033[0m\033[0m\033[0m!")
    else:
        print("\n\033[92mI'm sorry to say that your password is \033[1m\033[4mInvalid\033[0m\033[0m\033[0m!")        
enter_passwd()