x = int(input("Enter a number: "))

match x:
    case 0:
        print("x is equal to zero")
    case _ if x > 0:
        print("x is greater than zero")
    case _ if x < 0:
        print("x is less than zero")
