# Your code here

import yaml

with open ("products.yml", "r") as file:
    list_of_fruits = yaml.load(file, Loader = yaml.FullLoader)

number_of_customers = 0
profit = 0
biggest_expense = 0
customer_name = "noone"

while customer_name != "END":
    customer_name = input("Please enter the name of customer: ")

    if customer_name == "END":
        break

    number_of_customers += 1
    number_of_different_fruits = int(input("How many different fruits do you want to buy? "))
    
    list_of_fruits_names = []
    list_of_fruits_amounts = []
    list_of_fruits_payments = []
    for i in range (0, number_of_different_fruits):
        code_of_fruit = int(input("what is the code of your fruit? "))
        for fruits in list_of_fruits:
            if (fruits['code']) == code_of_fruit:
                name_of_fruit = fruits['name']
                price_of_fruit = fruits['price']
        
        list_of_fruits_names.append(name_of_fruit)
        print ("customer", customer_name, "is buying", name_of_fruit)

        amount_of_fruit = float(input("how many kilograms of your fruit do you want to buy?"))
        
        list_of_fruits_amounts.append(amount_of_fruit)
    
        payment = amount_of_fruit * price_of_fruit
        
        list_of_fruits_payments.append(payment)
    
    sum_of_expenses=sum(list_of_fruits_payments)
    
    if sum_of_expenses > biggest_expense:
        biggest_expense = sum_of_expenses
        customer_with_the_biggest_expenses = customer_name
    
    profit = sum(list_of_fruits_payments) + profit
    
    print ("This is the summary of "+customer_name+ "'s visit in Fruitshop")
    for a in range(0, number_of_different_fruits):
        print("Purchase number", [a], ":")
        print("Fruit name:", list_of_fruits_names[a])
        print("Amount of Fruit", list_of_fruits_amounts[a], "kg")
        print("Cost", list_of_fruits_payments[a], "$")
        print("")
    print("Total amount to be paid: ",sum(list_of_fruits_payments), "$")

print("")
print("Today's summary:")
print("Today's number of customers:", number_of_customers)
print("Today's profit:", profit, "$")
print("Our best customer today was:", customer_with_the_biggest_expenses, "and he spent", biggest_expense, "$")



    




