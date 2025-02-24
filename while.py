#1
# n=int(input("enter="))
# i=0
# sum=0
# while (i<n+1):
#     sum=sum+i
#     i+=1
# print(sum)

# #2
# num=int(input("enter="))
# i=1
# while i<11:
#     print(num,"*",i,"=",num*i)
#     i+=1

#3
num=int(input("Enter:"))
a=0
b=1
count=0

while count<num:
    print(a, b,  end=" ")
    a=b
    b=a+b
    count+=1