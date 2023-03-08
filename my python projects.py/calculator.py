def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def subtraction(a,b):
   answer = a-b
   print(str(a) + "-" + str(b) + "=" + str(answer))

def multiplication(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def division(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))


print("A.addition")
print("B.subtraction")
print("C.multplication")
print("D.division")

choice = input("enter your choice:")

if choice == "A":
    print("addition")
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    add (a,b)

elif choice == "B":
    print("subtraction")
    a = int (input("enter the first number:"))
    b = int (input("enter the second number:"))
    subtraction(a,b)

elif choice == "C": 
    print("multiplication")
    a = int (input("enter the first number"))
    b = int (input("enter the second number"))
    multiplication(a,b)

elif choice == "D":
    print("division")
    a = int (input("enter the first number"))
    b = int (input("enter the second number"))
    division(a,b)

elif choice == "E":
    print ("This is the end of the program")
    quit()

     
