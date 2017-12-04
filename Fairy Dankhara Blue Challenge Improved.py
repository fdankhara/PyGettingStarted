def checkPet():
    pet = input("Do you have a pet? e.g. cat?")
    if pet == "cat":
        print("I like cats too! I have two")
    elif pet == "dog":
        print("Woof Woof")
    elif pet == "fish":
        print("Is that Nemo? Have you captured him away from Marlin again?!")
    elif pet == "horse":
        print("He/she should be a pony!!")
    elif pet == "bird":
        print("I WILL SET HIM FREE")
    elif pet == "bunny":
        print("Awwwwww! ADORABLE!!")

def checkAccess():
    attempt = 1
    password = ""
    accessGranted = 0;
    while(attempt < 4 and accessGranted == 0):
        password = input("Enter your password: ")
        if password =="abcd1234":
            print("Access Granted")
            accessGranted = 1;
        else:
            if (attempt < 3):
                print("Access Denied. Wrong Password!, Please retry")
            attempt = attempt + 1
    if (attempt > 3):
        print("Access Denied. Retries Exceeded")
        exit(0)
    
#checking change control
print("LOGIN PAGE")
checkAccess()
#if "Access Denied. Wrong Password!":
#else:
computer_name = "Destiny"
player_name = input("What is your name?")
print("Hello ", player_name, "nice to meet you")
print("My name is ", computer_name)
age = int(input("Enter your age"))
if age == 31:
    print ("Is that you Mr Tibble?")
else:
    print("I'm older than you")
checkPet()

