import random

order_review = True
loop = True
# Welcome Message
print("Thanks for contacting customer service.")

#Name and Age Variables
customer = input("What's your name? ")
print(f"It seems like you're having trouble with your order {customer}, ")
order_number = input("Please input your order number: ")


#the menu
def menu():
    print("\n\n=== How Can I Help You?  === ")
    print("1. Track Order")
    print("2. Reorder ")
    print("3. Refund Order")
    print("4. Exit.")
    print("       =================\n")


#the interface
def interface():
    service = True
    menu()
    menu_selection = input("Where would you like to go?(1-4): ")
    
    #Tracking Order
    if int(menu_selection) == 1:    
        track_order()
    #Reordering
    elif int(menu_selection) == 2:
        reorder()
    #Refunding Order
    elif int(menu_selection) == 3:
        refund()
    elif int(menu_selection) == 4:
        print(f"Thanks for contacting service, {customer}. Hope you enjoy your day!")
        service = False
    return service
                      


#Random Minutes
mins = random.randint(1,300)
#Universal Order Status ===========
status = [f"Your order will arive in {mins} minutes.", 
                f"Your order #{order_number} has been lost.", 
                "It appears our driver ate your order.", 
                f"Your order #{order_number} is being prepared"]
#Choosing from list
order_status = random.choice(status)
# ==================================


#OPTION 1
def track_order():
    print(f"\n{order_status}")
    if order_status == f"Your order #{order_number} has been lost." or "It appears our driver ate your order.":
        review()



#OPTION 2
def reorder():
    confirm = input("Would you like to re-order your order? (Y/N):")
    if confirm == "Y":
        if order_status == f"Your order will arive in {mins} minutes." or f"Your order #{order_number} is being prepared":
            confirm2 = input("Your order will be arriving soon, are you sure you want to reorder? (Y/N): ")
            if confirm2 == "N":
                return
        print("Successfully re-ordered your order.")
    

#OPTION 3
#Check the user's order status to see if they're eligible for a refund.
def refund():
        if order_status == f"Your order #{order_number} has been lost." or "It appears our driver ate your order.":
            print(order_status)
            print("Sorry for the unfortunate experience. It seems like you're eligble for a refund.")
            print("Your money will be transferred back in the next 1-5 business days.")
            review()
        else: 
            print("Sorry, it doesn't seem like you're eligible for a review.")


# Universal Review
def review():
    while order_review:
        complain = input("Would you like to file a complaint? (Y/N): ")
        if complain == "Y":
            stars = input("Rate your order 1-5 stars: ")
            print(f"You've rated your order {stars} stars.\n") 
            feedback = input("Write any additional feedback you have, or N/A if none: ")
            print("Thanks for the feedback!")
            break       
        elif complain == "N":
            break
        else:
            print("Sorry this is not a valid input.")



# This double loop method was from C2C
while loop:
    interface()
    loop = interface()

