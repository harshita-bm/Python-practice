# # simple calculator:

# print("Simple Calculator")
# while True:
#     n=input("Choose the operator:\n 1. + \t 2. - \t 3. * \t 4. / \n Enter your choice: ")
#     match n:
#         case "+":
#             a=int(input("a= "))
#             b=int(input("b= "))
#             c= a+b
#             print(c)
#         case "-":
#             a=int(input("a= "))
#             b=int(input("b= "))
#             c= a-b
#             print(c)
#         case "*":
#             a=int(input("a= "))
#             b=int(input("b= "))
#             c= a*b
#             print(c)
#         case "/":
#             a=int(input("a= "))
#             b=int(input("b= "))
#             c= a/b
#             print(c)
    
# #Weekdays:

# print("Weekday")
# while True:
#     s= input("Enter the alphabet:")
#     match s:
#         case "m":
#             print("Monday")
#         case "t":
#             print("Tuesday")
#         case "w":
#             print("Wednesday")
#         case "t":
#             print("Thursday")
#         case "f":
#             print("Friday")
#         case "s":
#             print("Saturday")
#         case _:
#             print("No weekday")


# Pizza
print("Pizza")
while True:
    n=int(input("Select toppins for your pizza \n 1.Chees, Onion, Paneer \n 2. Onion, Tomato, Corn \n Enetr your choice : "))
    i_price=100
    price = 0
    match n:
        case 1:
            price=i_price+100
            print("Your Pizza is ready!!!!")
            print("Total:",price)
        case 2:
            price=i_price+50
            print("Your Pizza is ready!!!!")
            print("Total:",price)
    
