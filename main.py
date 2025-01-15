
loop = True
# Welcome Message
print("Welcome to Minerva's Shop!")

#Name and Age Variables
customer = input("What's your name? ")
cAge = input(f"Nice to meet you {customer}, How old are you?:  ")
if int(cAge) < 18:
    print("Wow, you're a little bit young to be shopping here... but that's alright!")


#the menu
def menu():
    print("\n\n\n=== This is Minerva's Shop === ")
    print("1. Head over to food and drink section.")
    print("2. Head over to the clothes section. ")
    print("3. Come and checkout!")
    print("4. Exit the shop.")
    print("       =================\n")


#the interface
def interface():
    shopping = True
    menu()
    menu_selection = input("Where would you like to go?(1-4): ")
    
    if int(menu_selection) == 1:
        print("Option isn't implemented yet.")
    elif int(menu_selection) == 2:
        print("Option isn't implemented yet.")
    elif int(menu_selection) == 3:
        print("Option isn't implemented yet.")
    elif int(menu_selection) == 4:
        print(f"Thanks for shopping {customer}. Hope you enjoy your day!")
        shopping = False
    return shopping
                      
# This double loop method was from C2C
while loop:
    interface()
    loop = interface()
