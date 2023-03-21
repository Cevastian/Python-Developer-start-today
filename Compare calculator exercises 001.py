'''

score = int(input("Please input your score."))

if score >= 90  score <=100:
    print("You are 'A' grade!")
elif score >= 80 & score < 90:
    print("You are 'B' grade!")
elif score >= 70 & score < 80:
    print("You are a 'C' grade!")
elif score >= 60 & score < 70:
    print("You are 'D' grade!")
elif score >101:
    print("It is not an available score!")
else:
    print("You are 'E' grade!")


order_food = input('''
1. Hamburger : $15  2. Pizza : $23  3. Pork Cuttlet $18  4. Curry $20

1. Please input food order number : ''')
order_qty = int(input("2. Please input food quantities : "))

if order_food == '1':
    print("Your ordered food is Hamburger and quantities are %i and total ordered cost is $ %s" %(order_qty, 15 * order_qty ))
elif order_food == '2':
    print("Your ordered food is Pizza and quantities are %i and total ordered cost is $ %s" %(order_qty, 23 * order_qty ))
elif order_food == '3':
    print("Your ordered food is Pork Cuttlet and quantities are %i and total ordered cost is $ %s" %(order_qty, 18 * order_qty ))
elif order_food == '4':
    print("Your ordered food is Curry and quantities are %i and total ordered cost is $ %s" %(order_qty, 20 * order_qty ))
else:
    print("Please input available food order number!")
    
'''

order_add = 'Y'
add_count = 0
while order_add =='Y' or order_add == 'y':
    order_food = input('''
    1. Hamburger : $15  2. Pizza : $23  3. Pork Cuttlet $18  4. Curry $20

    1. Please input food order number : ''')
    order_qty = int(input("2. Please input food quantities : "))

    if order_food == '1':
        print("Your ordered food is Hamburger and quantities are %i and total ordered cost is $ %s" %(order_qty, 15 * order_qty ))
    elif order_food == '2':
        print("Your ordered food is Pizza and quantities are %i and total ordered cost is $ %s" %(order_qty, 23 * order_qty ))
    elif order_food == '3':
        print("Your ordered food is Pork Cuttlet and quantities are %i and total ordered cost is $ %s" %(order_qty, 18 * order_qty ))
    elif order_food == '4':
        print("Your ordered food is Curry and quantities are %i and total ordered cost is $ %s" %(order_qty, 20 * order_qty ))
    else:
        print("Please input available food order number!")
    
    order_add = input("Do you want to add more foods?")

    if order_add =='y' or order_add =='Y':
        if add_count > 2:
            print("We are sorry, adding food orders are only 2 times.")
        else:
            add_count += 1
            continue
    else:
        break