def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation......")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")
while True:
    choice=input("Enter Choice(1/2/3/4)")
    if choice in('1','2','3','4'):
        num1=int(input("Enter first num"))
        num2=int(input("Enter Second num"))
        if choice=='1':
            print("add",add(num1,num2))
        elif choice=='2':
            print("sub",sub(num1,num2))
        elif choice=='3':
            print("Mult",Mult(num1,num2))
        elif choice=='4':
            print("div",div(num1,num2))
    else:
        print("invalid input")