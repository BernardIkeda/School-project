# Create a simple program which allows users to 
 # Buy item
 # View cart
# Remove from cart
# Make Purchace
#About Us
#Exit App

cart = []
customer_input = 0

while True:
    # First Interface
    customer_input = int(input("***Pella's Store***\n"
                               "1. Buy Item\n"
                               "2. View Cart\n"
                               "3. Remove Item from Cart\n"
                               "4. Make Purchase\n"
                               "5. About Us\n"
                               "6. Exit App\n"
                               "Enter an option: "))

    # Buying Item
    if customer_input == 1:
        buy = input("Enter Product Name: ")
        amount = int(input("Enter Quantity: "))
        c_o_1 = 10
        price = amount * c_o_1
        final_price = "$" + str(price)
        cart.append([amount, buy, final_price])
        print("Item purchased!")

    # Viewing Items
    elif customer_input == 2:
        if cart:
            print("Items in cart:")
            for item in cart:
                print(f"{item[0]} {item[1]} - {item[2]}")
        else:
            print("Your cart is empty!")

    # Removing items
    elif customer_input == 3:
        item_name = input("Enter Item name to remove: ")
        removed = False
        for item in cart:
            if item[1] == item_name:
                cart.remove(item)
                removed = True
                print(f"{item_name} removed from cart!")
                break

        if not removed:
            print(f"{item_name} not in cart!")

    # Making a purchase
    elif customer_input == 4:
        total_price = sum(int(item[2][1:]) for item in cart)
        if cart:
            print("===== Your Order Summary =====")
            for item in cart:
                print(f"{item[0]} {item[1]} - {item[2]}")
            print(f"Total: ${total_price} \n"
                  "Thank you for your purchase!")
            #print("Thank you for your purchase!")
            cart.clear()
        else:
            print("Your cart is empty!")

    # About Us
    elif customer_input == 5:
        print("===== About Us =====\n"
              "Welcome to our delightful shop, where quality meets affordability.\n"
              "Discover a wide range of products that cater to your every need.\n"
              "Embrace the joy of shopping as you explore our curated selection!.\n"
              "We hope you have a wonderful day! :) ")
       
    # Exiting the App
    elif customer_input == 6:
        print("Thank you for using Pella's Store!")

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
 