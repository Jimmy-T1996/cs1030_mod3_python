"""
Program: Challenge1
Author: Jaime Torres
Last Date Modified: 7/7/2024
Purpose: The purpose of this program is to produce a purchase receipt for the
store, "RARE Groceries Market". This program will create a list and calculation
of items purchased, with an item count and sales tax.

Author note: The course book and modules were not always helpful/clear and
I struggled to grasp some of the concepts explained. I used information sourced
from google, youtube, etc. to fill the gap on what I couldn't understand to get
a working product.

"""
#Below are preset values that will be utilized in calculating purchase total and receipt output.
salestax = 4.8  #tax rate of area set by Uncle Sam
storename = "RARE Groceries Market"  #name of fictional store
itemnames = []  #these items are inputs by the user, the "[]" allows for a blank value to exist until user fills it.
itemprices = []  #these prices are also inputs by the user



while True: #this starts a loop until conditions listed are met.
    itemname = input("Enter the name of item (Type --> 'n' <-- to quit adding items)") #all inputs will be called here to start loop.
    if itemname == "n": #this represents "no more items if the user tells loop to stop."
        break #when "n" is entered, the loop is closed. THIS TERMINATES LOOP.
    elif itemname == "":
        print("No item added.") #if nothing is entered (""), the user is let known here and returned to "itemname".
        continue
        #^this "continue" is to prevent the ("") from being added to append list. "continue" sends the user back to the beginning of the loop
        #instead of finishing the loop. Without this, adding ("") to the append list will inflate the calulated subtotal and add to the items list.
    else:
        itemprice = float(input(f"Please enter the price of {itemname}: $"))
        #"f" and "{}" in print function is used to bring last item name entered so the user is
        #aware of what to input for the price. These NEEDS to be a float to allow decimals for currency (real number).
    
    itemnames.append(itemname)
    #using an append list named, "itemnames", will make a saved list for items entered at "itemname".
    itemprices.append(itemprice)
    #using another append list named, "itemprices", will also save the prices at "itemprice".
    #***END OF LOOP BODY***
    
print () #this is only to visually seperate the loop body and receipt on output.
print ()
# below is the output function for customer recipt
def receipt(storename, itemnames, itemprices, salestax): #function is defined and calls for the preset values assigned at the beginning of the code.
    total = sum(itemprices) #this will add all prices that were added to the itemprices list.
    taxforpurchase = (salestax / 100) * total #this isolates the tax amount for this specific purchase.
    totalandtax = total + taxforpurchase #this adds the isolated tax to the total. This is the end-total.
#the print body below will create a header and list that is formatted with store and tax info
    print(f"------{storename}------") #store name is used for header
    print("Items Entered:")
    print("---------------")
    for name, price in zip(itemnames, itemprices):
        #^The "for", "in", "zip", code will pull several list of items at once(in different append lists). "for" values must be in same order of "in" values to match (x,y order).
        #(2) "for" loops did not work simultaneously previously. "itemnames.append" and "itemprices.append" are pulled here when called to print.
        print(f"{name}: ${price:.2f}")  # This prints each item / price input in the order entered, with "f" and ".2f" to create 2 decimal places on output.
    print("----------------------------") #This is aesthetic and allows for a customer friendly receipt.
    print(f"Number of Items:{len(itemnames)}") #using "f", "len" and "{itemnames}", the exact # of inputs in itemnames.append are shown.
    print("----------------------------") 
    print(f"Subtotal: ${total:.2f}") #this is the before-tax total
    print(f"Sales Tax ({salestax}%): ${taxforpurchase:.2f}")
    #^this line is the Sales tax percent and tax total for this purchase.
    #{salestax} and {taxforpurchase} are called for the print.
    print(f"Total: ${totalandtax:.2f}") #this is the end-total after tax.
    print("----------------------------") 
    print("☺ Thank you for your business! ☺")
#the calculation for the purchase is displayed and the .2f format ensures decimal count only goes to 2 decimals, round function did not work originally.
receipt(storename, itemnames, itemprices, salestax)
#^This calls the function to display the receipt with full print body as one action.
#***END OF CODE***
