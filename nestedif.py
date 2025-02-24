# # Validation
# usn=input("Enetr username:")
# if usn=="harsh123":
#     pwd=input("Enter the password:")
#     if pwd=="harsh_123":
#         print("Login successful")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect username")
    
# #vowel only if it is uppercase
# a=input("Enter :")
# if a>='A' and a<='Z':
#     if (a in 'AEIOU'):
#         print("Vowel")
#     else:
#         print("Consonents")
# else:
#     print("Its is not uppercase")


# #divisible by 9 only if it is 2 digit
# val= int(input("Enter:"))
# if val>=-99 and val<=-10 or val>=10 and val<=99:
#     if val % 9 == 0:
#         print("divisible by 9")
#     else:
#         print("Not divisible")
# else:
#     print("Enter 2 digit")

## greatest among 4
print("Enter 4 integer numbers")
n1=int(input("1 "))
n2=int(input("2 "))
n3=int(input("3 "))
n4=int(input("4 "))
if n1>n2:
    if n1>n3:
        if n1>n4:
            print(n1," is greater")
        else:
            print(n4, "is greater")
    else:
        if n3>n4 :
            print(n3," is greater")
        else:
            print(n4,"is greater")           
else:
    if n2>n3 :
        if n2>n4:
            print(n2, "is greater")
        else:
            print(n4,"is greater")
    else:
        if n3>n4:
            print(n3," is greater")
        else:
            print(n4,"is greater")
        
            