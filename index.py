##input we need from the user 
# total rent 
# total food amount ordered for snackes
# electricity unit speed
# charge per unit
# person living in the flat 
# 
# output
# total amount you've to pay to the owner
# 

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input('Enter the charge per unit = '))
persons = int(input("Enter person living in the room = "))

total_bill = electricity * charge_per_unit

output = (total_bill + food + rent)//persons

print("Each person will pay - ",output)