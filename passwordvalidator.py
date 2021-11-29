#The password is valid if all criteria are met:
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

import re #Adding re to satisfy the needs of the if, elif, else statements.

print("\033[33mWELCOME TO \033[1mCARLITO'S PASSWORD CHECKER!\033[33m\033[0m")

# Printing the criterias so that the user can have a guide on typing password.
Criterias = "\033[1m\033[36mYour password must have : \n A. Atleast 15 characters long; \n B. Atleast one capital letter; \n C. Atleast one number; \n D. Atleast one special character.\033[0m\033[0m"
print(f"{Criterias}") 

    # The program will ask for input from the user
password = input('\n\033[41mEnter your \033[4mdesired password\033[0m: \033[0m') 
    
    # Special Symbols Supported By The Program: ['!', '@', '#', '$', '%', '^','&','*','(',')', '_', '+', '-', '/', '=' ]
    
while True:     
    if len(password) < 15:
        print('\033[31mThe password length should be at least \033[1m15 characters\033[0m\033[31m. \033[36mPlease Try Again.\033[0m')
        pswd = 0
        break
    elif not re.search("[A-Z]", password):
        print('\033[31mPassword should have at least \033[1mone capital letter\033[0m\033[0m. \033[36mPlease Try Again\033[0m')
        pswd = 0
        break
    elif not re.search("[0-9]", password):
        print('\033[31mPassword should have at \033[1mleast one number\033[0m\033[0m. \033[36mPlease Try Again\033[0m')
        pswd = 0
        break
    elif not re.search("[!@#$%^&*()_+-/]", password):
        print('\033[31mPassword should have at least \033[1mone of the special characters ! @ # $ % ^ & * ( ) _ + - / =\033[0m \033[4m\033[0m\033[0m. \033[36mPlease Try Again.\033[0m')
        pswd = 0
        break
    else:
        pswd = 1
        print("\n\033[92m>>Congratulations! Your Password is \033[1m\033[4mValid\033[0m\033[0m\033[92m!<<\033[0m\033[0m\n")
        break 
if pswd == 0:
    print("\n\033[92m>>I'm sorry to say that your password is \033[1m\033[4mInvalid\033[0m\033[0m\033[0m!<<\033[0m\033[0m\n")
