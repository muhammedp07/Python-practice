n = int(input())
if n % 2 == 0:
    if n in range(2,5):
        print("Not Wierd")

    elif n in range(6,20):
        print("Wierd")

    elif n > 20:
        print("Not Weird")
else: 
    print("Weird")