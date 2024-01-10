from ast import Return


print("This programe will calculate the area of a Rectangle") 
L = int(input("Enter the Length of Rectangle: "))
if L < 0:
        print("The Length can never be Negetive")
        L = int(input("Enter the Length of Rectangle again: "))

B = int(input("Enter the Breadth of Rectangle: "))
if B < 0:
    print("The Breadth can Never be Negetive")
    B = int(input("Enter the Breadth of Rectangle again: "))

Area = L*B 
print("The Area of a Rectangle is", Area)


        
