# #1
# ch=input("Enter a character:")
# if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
#     if ch in "aeiou" or ch in "AEIOU":
#         print("It is a vowel")
#     else:
#         print("It is a consonent")
# else:
#     print("Enter a character")

# #2
# n=int(input("Enter a number:"))
# if n>0 :
#     if n<10:
#         print("Number is less than 10")
#     else:
#         print("Number is +ve and greater than 10")
# else:
#     if n==0:
#         print("Zero")
#     else:
#         print("Negetive")
        
        
# #     3
# age= int(input("Enter the age:"))
# if age>18:
#     print("Age is above 18")
#     license= input("Has License : Yes / NO ?")
#     if license == "y" or license =="Y":
#         print("Owns Driving Licence")
#     elif license=="n" or license=="N":
#         print("No Driving Licence")
#     else:
#         print("Invalid")
# else:
#     print("Below 18")
        
#4
# num= int(input("Enter the number:"))
# if num>0:
#     print("Number is +ve")
#     if num%2==0:
#         print("Nuumber is even")
#     else:
#         print("Number is odd")
# else:
#     print("Number is -ve")

#5

mark=int(input("Enter the marks:"))
if mark>=40:
    print("Passed")
    if 75<mark<100:
        print("Scored above 75" )
    else:
        print("Above 45 and below 75")
else:
    print("Failed")