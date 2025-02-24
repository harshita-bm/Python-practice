#single, double , triple or more
# num = int(input("Enter:"))
# if num>=-9 and num<=9:
#     print("single digit")
# elif (num>=-99 and num<=-10)or (num>=10 and num<=99):
#     print("Double digit")
# elif (num>=-999 and num<=-100)or (num>=100 and num<=999):
#     print("Triple digit")
# else:
#     print("More than that")


#lowercase, uppercase, digit or special character
# s=input("enter:")
# if s>='A' and s<='Z':
#     print("Uppercase")
# elif s>='a' and s<='z':
#     print("lowercase")
# elif s>='0' and s<='9':
#     print("numeric")
# else:
#     print("special character")

#  #divisible by 5 or 9 or by both or not divisible by both
# i=int(input("Enter:"))
# if i % 5==0:
#     print("divisible by 5")
# elif i % 9==0:
#     print("Divisible by 9")
# elif i % 5 ==0 and i % 9 ==0:
#     print("divisible by both 5 and 9")
# else:
#     print("not divisible by both 5 and 9")
    
    
# greatest among 4
print("Enter 4 integer numbers")
n1=int(input("1 "))
n2=int(input("2 "))
n3=int(input("3 "))
n4=int(input("4 "))
if n1>n2 and n1>n3 and n1>n4:
    print(n1,"is greater")
elif n2>n1 and n2>n3 and n2>n4:
    print(n2,"is greater")
elif n3>n1 and n3>n2 and n1>n4:
    print(n3,"is greater")
else:
    print(n4,"is greater")