print("Hii I am caluclator, how can I help you?")
response1=input()
if response=="add":
   num1=int(input("Enter first num"))
   num2=int(input("Enter second num"))
   print(num1+num2)
elif response=="sub":
    num1=int(input("Enter first num"))
    num2=int(input("Enter second num"))
    print(num1-num2)
elif response=="mult":
    num1=int(input("Enter first num"))
    num2=int(input("Enter second num"))
    print(num1*num2)
elif response=="div":
    num1=int(input("Enter first num"))
    num2=int(input("Enter second num"))
    print(num1/num2)
else:
    print("I can't perform that action")